import streamlit as st
import pandas as pd
from user_streamlit import users
from inventario import inventario
from fpdf import FPDF
import datetime

def menu_inv(verficacion):
    st.title("Inventario")

    pes1, pes2, pes3 = st.tabs(["Stock", "Certificaciones","Ingresar material"])

    with pes1:
        st.header("Stock de la clinica")

        with st.form("formulario_stock"):

            medicamento = st.text_input("Ingrese el nombre del medicamento o inicial.").strip()
            stk = st.number_input("Ingrese el numero de Stock.")

            col1,col2,col3,col4 = st.columns(4)
            with col1:
                bt_one = st.form_submit_button("Ver producto")
            with col2:
                bt_all = st.form_submit_button("Ver Stock Completo")
            with col3:
                mayq = st.form_submit_button("Stock mayor o igual que")
            with col4:
                menq = st.form_submit_button("Stock menor o igual que")
            
            if bt_one:
                if not medicamento:
                    st.warning("Ingrese al menos una inicial.")
                else:
                    up = inventario()
                    auxone = True
                    result = up.consultar_producto(medicamento,auxone)
                    
                    if len(result) >0:
                        one = pd.DataFrame(result)
                        one = one[["nombre","stock_total","descripcion","presentacion","marca","precio por unidad"]]
                        st.dataframe(one, use_container_width=True,hide_index=True)

                    else:
                       st.error("No se encontro ningun producto con esa/s inicial/es.")

            if bt_all:
                i = inventario()
                auxsk1 = True
                resultado = i.consultar_stock(auxsk1)

                if len(resultado) >0:
                    df = pd.DataFrame(resultado)
                    df = df[["nombre","stock_total","descripcion","presentacion","marca","precio por unidad"]]
                    st.dataframe(df, use_container_width=True,hide_index=True)

                else:
                   st.error("Stock vacio.")

            if mayq:
                mayq = inventario()
                resultado = mayq.stock_mayor(stk)

                if len(resultado) >0:
                    df = pd.DataFrame(resultado)
                    df = df[["nombre","stock_total","descripcion","presentacion","marca","precio por unidad"]]
                    st.dataframe(df, use_container_width=True,hide_index=True)

                else:
                   st.error("Stock vacio.")

            if menq:
                menq = inventario()
                resultado = menq.stock_menor(stk)

                if len(resultado) >0:
                    df = pd.DataFrame(resultado)
                    df = df[["nombre","stock_total","descripcion","presentacion","marca","precio por unidad"]]
                    st.dataframe(df, use_container_width=True,hide_index=True)
                else:
                   st.error("Stock vacio.")
    with pes2:
        st.header("Certificaciones")

        i = inventario()

        resultado = i.consultar_certificaciones()

        if len(resultado) >0:
            st.dataframe(resultado, use_container_width=True)

        else:
            st.warning("No hay certificaciones que mostrar.")

    with pes3:
        if verficacion:
            st.header("Registrar medicamento.")
            with st.form("formulario_medicina"):
                recet = ["Si","No"]
                diccionario = {
                    "Si":True,
                    "No":False
                }
                st.write("Datos del medicamento")

                colnom,colsus = st.columns(2)
                with colnom:
                    nombre = st.text_input("Ingrese el nombre del medicamento.").strip()
                    descripcion = st.text_input("Descripción").strip()
                    unidad = st.text_input("Unidad de medida (ej:caja,frasco,etc.)").strip()
                    cod_b = st.text_input("Codigo de barras").strip()
                    stock_t = st.number_input("Stock total")
                with colsus:
                    sustancia = st.text_input("Ingrese el nombre de la sustancia activa.").strip()
                    presentacion = st.text_input("Presentacion (ej: Frasco con 60 tabletas.)").strip()
                    marca = st.text_input("Marca").strip()
                    recetado = st.selectbox("Necesita receta",recet)
                    recetado_fin = diccionario[recetado]
                    precio = st.number_input("Precio por unidad")

                st.write("Datos del Lote")
                hoy = datetime.date.today()
                clot,fccol,cntcol = st.columns(3)
                with clot:
                    cod_lot = st.text_input("Codigo de lote").strip()
                with fccol:
                    fecha_cad = st.date_input("Fecha de caducidad",value=hoy,min_value=hoy,format="DD/MM/YYYY")
                with cntcol:
                    cnt_dis = st.text_input("Cantidad disponible").strip()

                st.write("Datos del proveedor")
                colprov, colempro = st.columns(2)
                with colprov:
                    prov = st.text_input("Nombre del Proveedor").strip()
                with colempro:
                    em_prov = st.text_input("Email proveedor").strip()

                btn_insert = st.form_submit_button("Insertar medicamento.")
                if btn_insert:
                    if cod_b.isdigit() and nombre and descripcion and unidad and cod_b and stock_t and sustancia and presentacion and marca and recetado and precio:
                        i = inventario()
                        resultado = i.agregar_medicamento(nombre,sustancia,descripcion,presentacion,marca,cod_b,recet,recetado_fin,stock_t,unidad,precio, 
                                                            cod_lot,fecha_cad,cnt_dis,prov,em_prov)

                        if resultado==True:
                            st.success("Medicamento agregado de forma exitosa.")
                        else:
                            st.error("No se puedo agregar el medicamento")
                    else:
                        st.warning("Favor de llenar los campos de forma correcta.")
        else:
            st.write("Lo siento este apartado solo esta disponible para administradores.")

def comprar_medicina():
    if 'carrito' not in st.session_state:
        st.session_state.carrito = []

    st.title("Farmacia Pit Duncan")
    pest1,pest2 = st.tabs(["Tienda","Carrito"])
    
    with pest1:
        st.header("Tienda")
        with st.form("formulario_comprar_med"):
            
            medicamento = st.text_input("Ingrese el nombre del medicamento o inicial para buscar.").strip()

            col1, col2 = st.columns(2)

            with col1:
                bt_one = st.form_submit_button("Ver producto")

            with col2:
                bt_all = st.form_submit_button("Ver Stock Completo")

            nom_medicamento = st.text_input("Nombre del medicamento a comprar.",placeholder="ej. Amoxil 500mg").strip()
            cantidad = st.number_input("Ingrese la cantidad a comprar.",min_value=0,step=1)
            btn_agregar = st.form_submit_button("Agregar al carrito")

            if bt_one:
                if not medicamento:
                    st.warning("Ingrese al menos una inicial.")
                else:
                    up = inventario()
                    auxone1 = False
                    result = up.consultar_producto(medicamento,auxone1)
                    
                    if len(result) >0:
                        one = pd.DataFrame(result)
                        one = one[["nombre","descripcion","presentacion","marca","precio por unidad"]]
                        st.dataframe(one, use_container_width=True,hide_index=True)

                    else:
                       st.error("No se encontro ningun producto con esa/s inicial/es.")
            if bt_all:
                i = inventario()
                auxsk = False
                resultado = i.consultar_stock(auxsk)

                if len(resultado) >0:
                    df = pd.DataFrame(resultado)
                    df = df[["nombre","descripcion","presentacion","marca","precio por unidad"]]
                    st.dataframe(df, use_container_width=True,hide_index=True)

                else:
                   st.error("Stock vacio.")

            if btn_agregar:
                if nom_medicamento and cantidad:
                    up = inventario()
                    auxone1 = True
                    result = up.consultar_producto(nom_medicamento,auxone1)

                    if result:
                        dato = list(result)[0]
                        precio = float(dato['precio por unidad'])
                        cant = int(cantidad)
                        subtotal = precio * cant

                        prod_carrito = {
                                "producto":dato['nombre'],
                                "descripcion":dato['descripcion'],
                                "presentacion":dato['presentacion'],
                                "marca":dato['marca'],
                                "precio por unidad":precio,
                                "cantidad a comprar":cant,
                                "subtotal":subtotal
                        }

                        st.session_state.carrito.append(prod_carrito)
                        st.toast("Se agrego el producto al carrito.")
                    else: 
                        st.error("No se encontro el producto")
                else:
                    st.warning("Favor de llenar los campos correspondientes para agregar al carrito.")
    
    if 'pdf_efectivo_listo' not in st.session_state:
        st.session_state.pdf_efectivo_listo = None

    if 'pdf_plinea_listo' not in st.session_state:
        st.session_state.pdf_plinea_listo = None

    with pest2:
        st.header("Carrito")

        if len(st.session_state.carrito)>0:
            df_carrito = pd.DataFrame(st.session_state.carrito)
            st.dataframe(df_carrito,use_container_width=True,hide_index=True)

            total = df_carrito['subtotal'].sum()
            st.write(f"Total: ${total:,.2f}")

            if st.button("Vaciar carrito"):
                st.session_state.carrito = []
                st.rerun()

            with st.form("Pagos"):
                st.header("Pagos")
                pesta1,pesta2 = st.tabs(["Pago en linea","Pago en efectivo"])
                hoy = datetime.date.today()
                with pesta1:

                    num_tarjeta = st.text_input("Numero de tarjeta").strip()
                    nom_prop = st.text_input("Nombre del propietario").strip()

                    column1,column2 = st.columns(2)

                    with column1:
                        fecha_cad = st.date_input("Fecha de caducidad",value=hoy,min_value=hoy,format="DD/MM/YYYY")
                    
                    with column2:
                        cvv = st.text_input("Ingrese CVV").strip()

                    btn_linea = st.form_submit_button("Pagar")

                    if btn_linea:
                        if num_tarjeta.isdigit() and len(num_tarjeta)==16 and nom_prop and cvv.isdigit() and len(cvv)==3:
                            i = inventario()
                            
                            for index,row in df_carrito.iterrows():
                                prod = row['producto']
                                canti = row['cantidad a comprar']

                                resultado = i.min_stock(prod,canti)

                                if resultado == True:
                                    
                                    pdf_bytes_ln = generar_ticket_pdf(
                                        carrito=st.session_state.carrito,
                                        total=total,
                                        tipo_pago="Pago en linea",
                                    )

                                    st.session_state.pdf_plinea_listo = pdf_bytes_ln
                                    st.success("Compra realizada favor de descargar su ticket.")

                                #st.session_state.carrito = []
                                else:
                                    st.error("Error al procesar su compra, porfavor intentelo mas tarde.")
                        else:
                            st.warning("Favor de llenar los campos correspondientes de forma correcta para realizar el pago en linea.")

                with pesta2:
                    btn_efe = st.form_submit_button("Hacer orden",key="btn_bajo")
                    if btn_efe:
                                        
                        pdf_bytes_efe = generar_ticket_pdf(
                            carrito=st.session_state.carrito,
                            total=total,
                            tipo_pago="Pago en efectivo",
                        )

                        st.session_state.pdf_efectivo_listo = pdf_bytes_efe
                        st.success("Orden generada, por favor descargar el PDF.")

            col_descargas1, col_descargas2 = st.columns(2)
        
            with col_descargas1:
                if st.session_state.pdf_plinea_listo is not None:
                    st.download_button(
                        label="Descargar Ticket Online",
                        data=st.session_state.pdf_plinea_listo,
                        file_name="Ticket_Clinica_PitDuncan_Online.pdf",
                        mime="application/pdf"
                    )

            with col_descargas2:
                if st.session_state.pdf_efectivo_listo is not None:    
                    st.download_button(
                        label="Descargar Orden de Pago",
                        data=st.session_state.pdf_efectivo_listo,
                        file_name="Orden_Pago_PitDuncan.pdf",
                        mime="application/pdf"
                    )

        else:
            st.info("El carrito esta vacio")

def generar_ticket_pdf(carrito, total, tipo_pago, nombre_cliente="Cliente Mostrador"):
    # Configuración básica del PDF (A4 vertical)
    pdf = FPDF()
    pdf.add_page()
    
    # --- ENCABEZADO ---
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "CLÍNICA PIT DUNCAN", ln=True, align='C')
    
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, "Ticket de Compra", ln=True, align='C')
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pdf.cell(0, 5, f"Fecha: {fecha}", ln=True, align='C')
    
    pdf.ln(10) # Espacio vacio
    
    # --- DATOS DEL CLIENTE ---
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, f"Cliente: {nombre_cliente}", ln=True)
    pdf.ln(5)

    # --- TABLA DE PRODUCTOS ---
    # Encabezados
    pdf.set_fill_color(200, 200, 200)
    pdf.cell(80, 8, "Producto", 1, 0, 'L', True)
    pdf.cell(30, 8, "Cant.", 1, 0, 'C', True)
    pdf.cell(40, 8, "Precio Unit.", 1, 0, 'R', True)
    pdf.cell(40, 8, "Subtotal", 1, 1, 'R', True) # El 1, 1 al final hace el salto de línea
    
    # Filas del carrito
    pdf.set_font("Arial", size=10)
    for item in carrito:
        nombre = item['producto']
        # Recortamos el nombre si es muy largo para que no rompa el ticket
        if len(nombre) > 35: 
            nombre = nombre[:32] + "..."
            
        cant = str(item['cantidad a comprar'])
        precio = f"${item['precio por unidad']:,.2f}"
        sub = f"${item['subtotal']:,.2f}"
        
        pdf.cell(80, 8, nombre, 1)
        pdf.cell(30, 8, cant, 1, 0, 'C')
        pdf.cell(40, 8, precio, 1, 0, 'R')
        pdf.cell(40, 8, sub, 1, 1, 'R')

    # --- TOTAL ---
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(150, 10, "TOTAL A PAGAR:", 0, 0, 'R')
    pdf.cell(40, 10, f"${total:,.2f}", 1, 1, 'R')

    # --- MENSAJE CONDICIONAL (La parte importante) ---
    pdf.ln(15)
    pdf.set_font("Arial", 'B', 14)
    
    if tipo_pago == "Pago en linea":
        pdf.set_text_color(0, 128, 0) # Verde
        pdf.cell(0, 10, "ESTATUS: PAGADO", ln=True, align='C')
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, "Instrucción: Muestre este ticket en la tienda para recibir sus productos. No es necesario realizar ningún pago adicional.", align='C')
    else:
        pdf.set_text_color(180, 0, 0) # Rojo oscuro
        pdf.cell(0, 10, "ESTATUS: PENDIENTE DE PAGO", ln=True, align='C')
        pdf.set_font("Arial", size=11)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 6, "Instrucción: Pase a caja y presente este ticket para realizar el pago y recibir sus productos.", align='C')

    # Retornar los bytes del PDF
    return pdf.output(dest='S').encode('latin-1')