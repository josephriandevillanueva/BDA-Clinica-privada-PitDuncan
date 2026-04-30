# Replication Guide Report

This report provides a comprehensive breakdown of the Clínica Privada Pit Duncan application. It details all available menus, user actions, workflows, feature redundancies, and areas of improvement based on a thorough analysis of the project files.

## 1. User Roles & Access Management
The application supports three distinct types of users, each with unique access rights routed from `main.py`:
- **Public / Client**: Accesses the app without authentication. Can book appointments and buy medicines.
- **Doctor**: Authenticated user. Can manage patients, view appointments, generate prescriptions, and generate invoices.
- **Administrator**: Authenticated user (username contains "admin"). Can manage the system's users and full inventory.

---

## 2. All Possible Menus & Views

### Main Menu (`menu_principal`)
- **Login**: Routes to authentication screen.
- **Generar Cita**: Routes to public appointment booking.
- **Comprar Medicina**: Routes to public pharmacy.

### Administrator Menu (`menu_admin`)
- **Usuarios**: Opens `menu_user()` with tabs to Create, Delete, and List users.
- **Inventario**: Opens `menu_inv()` with tabs for Stock queries, Certifications, and Material Registration.

### Doctor Menu (`menu_medicos`)
- **Prescribir Receta**: Opens `generar_recetita()` to create a PDF prescription.
- **Pacientes**: Opens `menu()` with tabs to Create, Delete, View, and Check History of patients.
- **Generar Factura**: Opens `generar_factura()` to create a PDF invoice.
- **Citas**: Opens `menu_citas(aux=True)` to view scheduled appointments.

### Public Store (`comprar_medicina`)
- **Tienda**: Browse catalog, filter by text, add to cart.
- **Carrito**: Modify quantities, remove items, select payment method (Online / Cash), upload prescription PDF (if required), checkout to generate PDF tickets.

---

## 3. All Possible User Actions & Workflows

### Workflow 1: Public Pharmacy Shopping
1. User clicks **Comprar Medicina** from the main menu.
2. User browses the **Tienda** tab, filtering the catalog dataframe by name.
3. User selects a medicine from the dropdown, enters quantity, and clicks **Agregar al carrito**.
4. User switches to the **Carrito** tab.
5. *Action*: User can adjust quantities via number input or delete items from the cart.
6. *Condition*: If any item in the cart has `recetado == True`, the system displays a warning and forces the user to upload a PDF prescription.
7. If the user attempts to pay without the PDF, the system blocks the transaction with an error.
8. User selects **Pago en linea** (enters CC details) or **Pago en efectivo**.
9. System subtracts items from the database inventory.
10. System generates and offers a downloadable PDF ticket (Green "PAGADO" for online, Red "PENDIENTE DE PAGO" for cash).

### Workflow 2: Public Appointment Booking
1. User clicks **Generar Cita** from the main menu.
2. User fills out Name, Specialist required, Date, and Time.
3. System saves the appointment to the database and confirms success.
*(Note: Public users can see the "Ver citas" tab but are blocked by a message asking them to log in).*

### Workflow 3: Doctor Operations
1. Doctor logs in (username does not contain "admin").
2. Directed to **Menú de Médicos**.
3. *Action - Prescription*: Clicks **Prescribir Receta**. Fills out patient data, selects medicines dynamically fetched from the inventory collection, writes instructions, and generates a PDF.
4. *Action - Billing*: Clicks **Generar Factura**. Enters patient data, selects doctor from active users, enters service cost, and generates a PDF invoice, saving the record in the `facturas` collection.
5. *Action - Patient Management*: Uses tabs to add new patients, delete them, or view medical history (blood type, allergies).
6. *Action - View Appointments*: Clicks **Citas**, enters a patient name or views all appointments currently registered in the database.

### Workflow 4: Admin Operations
1. Admin logs in (username contains "admin").
2. Directed to **Menú de Administrador**.
3. *Action - User Management*: Creates new doctors/admins, or deletes them.
4. *Action - Inventory Management*: Adds new medicines to the database (specifying lot, provider, prescription requirement), or queries existing stock by name, > / < quantities.

---

## 4. Differences Between Similar Menus & Redundancies

### Redundancy in CRUD Operations
- `admin_view.py` (Usuarios) and `doctor_view.py` (Pacientes) implement almost identical tab structures for Create, Read, and Delete operations.
- **UX Difference**: The `Pacientes` viewer filters specific pandas dataframe columns using `df[["nombre", "apellido..."]]` to hide the `_id`, whereas the `Usuarios` viewer just dumps the raw dataframe directly into the UI. This creates an inconsistent presentation of data tables.

### Conditional UI Rendering (`appointments_view.py`)
- The `menu_citas` view uses a boolean `aux` flag to determine if the user is a Doctor (`True`) or Public (`False`).
- **UX Difference**: Instead of completely hiding the "Ver citas" tab from public users, the tab is rendered, but clicking it reveals a text message: *"Para ver este apartado necesita iniciar sesion."* This is bad UX. If a user doesn't have access, the tab shouldn't exist.

### Search Mechanisms
- **Inventory Admin**: To search stock, admins must click specific buttons ("Ver producto", "Stock mayor que").
- **Inventory Public Store**: The public store uses a dynamic `st.text_input` filter that automatically filters the dataframe using pandas `.str.contains()`.
- **Takeaway**: The public store search is much more modern and fluid. The admin stock search feels rigid and redundant.

---

## 5. Areas of Improvement (UX & Possibilities)

### 1. Hardcoded Paths & Environment Variables
- **Critical Issue**: In `doctor_view.py`, the PDF generation relies on a hardcoded absolute path for the clinic logo (`C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas...`). This will immediately crash or fail to load images on any other machine. It must be refactored to use relative paths (e.g., `src/static/img/logo.png`).

### 2. Form Validation & Data Integrity
- Phone numbers and zip codes only check `.isdigit()` and `len() == 10`.
- Emails are not validated with regex.
- User creation does not check if the username already exists in the database.
- Payment form accepts any 16-digit number and 3-digit CVV, but lacks basic Luhn algorithm validation for credit cards.

### 3. Role-Based Access Control (RBAC)
- **Current logic**: The app checks `if "admin" in user.lower():` to grant administrator access.
- **Improvement**: This is highly insecure and unscalable. The `usuarios` MongoDB collection should have a dedicated `rol` field (e.g., `"rol": "admin"` or `"rol": "doctor"`).

### 4. Component Modularization
- The PDF generation code using `FPDF` is repeated entirely from scratch in three different places: `generar_recetita` (doctor), `generar_factura` (doctor), and `generar_ticket_pdf` (store).
- **Improvement**: Create a dedicated `pdf_service.py` utility that handles headers, footers, and logos to enforce a unified brand identity across all documents and reduce code duplication.

### 5. UI/UX Polish
- **Tab Hiding**: Update the Streamlit logic to dynamically generate the list of tabs based on user permissions, rather than rendering empty tabs with "Access Denied" messages.
- **Cart State**: The session state for `carrito` does not persist if the user navigates back to the main menu and then returns to the store.
- **Error Messages**: Minor typos in user feedback (e.g., "No se puedo agregar el medicamento" in `inventory_view.py`).
