#Aqui llamamos a otros archivos y sus funciones y otras librerias
import streamlit as st
import pandas as pd
from src.services.users import users
import datetime
from fpdf import FPDF
from src.services.pacientes import pacientes
from src.services.facturas import facturas
from src.services.inventario import inventario

#Funcion para ingresar, dar de baja, ver datos e historial de los usuarios.
def menu():
    st.title("Pacientes")
    #Creamos las pestañas para esta ventana
    pes1, pes2, pes3 ,pes4 = st.tabs(["Ingresar paciente", "Dar de baja paciente", "Ver pacientes","Historial del paciente"])

    with pes1:
        st.header("Alta de paciente")
        with st.form("alta_paciente"):
            hoy=datetime.date.today() #guardamos la fecha de hoy para usarla despues en el campo de la fecha
            fecha_min = datetime.date(1900,1,1) #ponemos una fecha para ponerla como fecha minima porque el date_input solo recorre 10 años atras
            colnom,colap,colam = st.columns(3) #sirve para acomodar los widgets en columnas, aqui creamos 3 columnas
            with colnom: #Primera columna
                nombre = st.text_input("Nombre del paciente", key="alta_nombre").strip()
                #Este es para la fecha, aqui es donde usamos hoy, el valor predefinido es la fecha de hoy, max_value sirve para elegir la fecha de hoy o
                #fechas anteriores, no puedo elegir la fecha de mañana, el formato solo sirve para darle una nueva forma a la fecha, key lo tienen todos los
                #widgets porque es un identificador para que el st.tabs no se equivoque al momento de saber que widget le pertenece a que pestaña.
                DOB = st.date_input("Fecha de nacimiento",value=hoy,min_value=fecha_min,max_value=hoy,format="DD/MM/YYYY", key="alta_dob")
            with colap:#Segunda columna
                ap = st.text_input("Apellido paterno del paciente", key="alta_ap").strip()
                tel = st.text_input("telefono", key="alta_tel").strip()
            with colam:#Tercer columna
                am = st.text_input("Apellido materno del paciente", key="alta_am").strip()
                email = st.text_input("correo electronico", key="alta_email").strip()

            st.write("**Direccion del paciente**") #Sirve nada mas para escribir un texto y los asteristos sirve para resaltarlo como las negritas del word

            cd_col,col_col = st.columns(2) #Aqui mas columnas para acomodar widgets, no comento nada mas porque es lo mismo que hace 20 lineas.
            with cd_col:
                cd = st.text_input("ciudad", key="alta_cd").strip()
            with col_col:
                col = st.text_input("colonia", key="alta_col").strip()
            calle = st.text_input("calle", key="alta_calle").strip()

            columna1,columna2,columna3 = st.columns(3) #Mas columnas
            with columna1:
                #Placeholder sirve para poner un pretexto en el campo, sirve para darle indicaciones al usuario de que puede poner en el campo
                #help es parecido que placeholder solo que aqui es un pequeño simbolo de un signo de interrogacion que aparece arriba a la 
                #derecha pero tienes que colocarte arriba de el para saber que contiene.
                nint = st.text_input("N.O interior", key="alta_nint",placeholder="Importe leer la ayuda (?)",help="Si el paciente no tiene numero interior favor de colocar SNI").strip()
            #De aqui a la linea 70 es basicamente lo mismo
            with columna2:
                numext = st.text_input("N.O exterior", key="alta_next").strip()
            with columna3:
                cp = st.text_input("codigo postal", key="alta_cp").strip()
            
            st.write("**Contacto de emergencia del paciente**")

            nc = st.text_input("nombre del contacto", key="alta_nc").strip()
            colpa,coltelc = st.columns(2)
            with colpa:
                pa = st.text_input("parentesto", key="alta_pa").strip()
            with coltelc:
                telc = st.text_input("telefono contacto", key="alta_telc").strip()
            
            st.write("**datos medicos del paciente**")
            colts,colaler = st.columns(2)
            with colts:
                ts = st.text_input("tipo de sangre", key="alta_ts").strip()
            with colaler:
                alergias = st.text_input("alergias", key="alta_alergias").strip()

            p = pacientes() #llamamos a la funcion pacientes del archivo pacientes
            #Aqui usamos el st.form_submit_button porque no deja colocar st.button dentro de un st.form
            btn_ingresar = st.form_submit_button("Ingresar", key="btn_ingresar")
            if btn_ingresar: #Solo se activa si se presiona el boton de la linea 74
                #Aqui hace varias verificacion, son mas que nada a los campos que llevan numeros, se usa isdigit() para verificar que lo que tiene el campo
                #son solo numeros, uso len() para los telefonos para que no se pasen de 10 digitos, existe el number_input el problema es que este campo
                #te lo genera con botones extra entonces para este paso no los use.
                if tel.isdigit() and len(tel)==10 and numext.isdigit() and cp.isdigit() and telc.isdigit() and len(telc)==10:
                    #llama a una de las funciones de persona y se le mandan sus respectivos parametros
                    resultado = p.dar_de_alta_paciente(nombre,ap,am,DOB,tel,email,calle,nint,numext,col,cp,cd,nc,pa,telc,ts,alergias)

                    if resultado: #Si regresa true manda un mensaje de exito o si regresa false manda error
                        st.success("Paciente ingresado")
                    else:
                        st.error("No se pudo ingresar al paciente.")
                else:
                    st.warning("Favor de rellenar todos los campos de forma adecuado")#en caso de que una de las verificaciones de campo falle manda un mensaje
    with pes2: #Lo de esta pestaña se basicamente lo mismo en varios aspectos la unica direfencia es que da de baja a un paciente, voy a saltar a la linea 106.
        st.header("Baja de paciente")
        with st.form("baja_paciente"):
            nombre1 = st.text_input("Nombre del paciente", key="baja_nombre").strip()
            ap1 = st.text_input("Apellido paterno del paciente", key="baja_ap").strip()
            am1 = st.text_input("Apellido materno del paciente", key="baja_am").strip()

            p1 = pacientes()
            btn_baja = st.form_submit_button("Dar de baja", key="btn_baja")
            if btn_baja:
                 resultado1 = p1.dar_de_baja_paciente(nombre1,ap1,am1)

                 if resultado1: # Si es True
                     st.success(f"{nombre1} {ap1} {am1} ha sido dado de baja del sistema")
                 else:
                     st.error("No se pudo dar de baja al Paciente")

    with pes3: #Algunas partes de esta pestaña son iguales, voy a saltar a la linea 125
        st.header("Ver pacientes")

        with st.form("forma_paciente"):
            nombre = st.text_input("Nombre del paciente",key="mas_baja_nom").strip()
            ap = st.text_input("Apellido paterno del paciente",key="mas_baja_app").strip()
            am = st.text_input("Apellido materno del paciente",key="mas_baja_apm").strip()
            colu1, colu2 = st.columns(2)

            with colu1:
                btn_one = st.form_submit_button("Buscar paciente.",key="mas_baja_one")
            with colu2:
                btn_all = st.form_submit_button("Ver todos los pacientes.",key="mas_baja_all")
            
            if btn_all: #boton para mostrar todos los pacientes
                p2 = pacientes()
                result = p2.mostrar_pacientes()
                
                if len(result) >0: #Verificamos que result si tenga algo en caso de que no....
                    one = pd.DataFrame(result) #Aqui ocupamos pandas aqui lo que hace panda es agarrar los datos de resultado y hacerlo una tabla.
                    #Aqui elegirmos que columnas queremos de esa tabla que nos hizo panda, sirve por ejemplo cuando nos regresa el _id como eso no le insteresa
                    #al usuario podemos quitarlo nada mas no eligiendo ese campo
                    one = one[["nombre","apellido paterno","apellido materno","fecha de nacimiento","telefono","email","Direccion","Contacto de emergencia","fecha de registro","activo"]]
                    #Aqui el dataframe solo sirve para mostrarle la tabla al usuario, el dataframe se streamlit genera por defecto un id
                    #hidex sirve para no mostrar ese id 
                    st.dataframe(one, use_container_width=True,hide_index=True) 
                else:
                   st.error("No se encontro ningun paciente") #Va a mandar un error si result no tiene nada.

            if btn_one:#Boton para mostrar un paciente, este if es basicamente lo mismo que lo que esta entre la linea 124 y la 133, salto a la linea 146
                p3 = pacientes()
                result = p3.mostrar_un_paciente(nombre,ap,am)
                
                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","apellido paterno","apellido materno","fecha de nacimiento","telefono","email","Direccion","Contacto de emergencia","fecha de registro","activo"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun paciente")
    with pes4:#Esta pestaña (linea 146-181) es lo mismo que vismo en las otras pestañas, salto a la linea 183
        st.header("Historial del paciente")
        with st.form("historial_paciente"):
            nombre = st.text_input("Nombre del paciente",key="aunmas_baja_nom").strip()
            ap = st.text_input("Apellido paterno del paciente",key="aunmas_baja_app").strip()
            am = st.text_input("Apellido materno del paciente",key="aunmas_baja_apm").strip()

            p = pacientes()
            col1,col2 = st.columns(2)

            with col1:
                btn_busc = st.form_submit_button("Buscar",key="aunmas_baja_btn")
            with col2:
                btn_td = st.form_submit_button("Ver todos los datos",key="aunmas_baja_btnt")

            if btn_busc:
                result = p.consultar_datos_medicos(nombre, ap, am)

                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","apellido paterno","apellido materno","tipo de sangre","alergias"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun paciente")

            if btn_td:
                result = p.consultar_tdsDts()

                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","apellido paterno","apellido materno","tipo de sangre","alergias"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun paciente")

def generar_recetita():
    #Crea una variable en memoria para guardar el PDF cuando este se genera. Si la pagina se recarga se va a mantener.
    if 'pdf_receta_listo' not in st.session_state:
        st.session_state.pdf_receta_listo = None
    st.title("Receta medica")
    with st.form("form_receta"):
        #Entre la linea 190 y 200 solo le pedimos unos datos al usuario para colocarlos en la receta, .strftime solo sirve para darle formato a la fecha.
        fecha = datetime.date.today().strftime('%d/%m/%Y')#fecha actual
        paciente = st.text_input("Nombre del paciente").strip()

        colum1,colum2 = st.columns(2)
        with colum1:
            edad = st.text_input("Edad del paciente").strip()
        with colum2:
            peso = st.text_input("Peso del paciente").strip()
        
        diagnostico = st.text_input("Diagnostico").strip()
        
        # Datalist de medicinas
        inv_service = inventario()
        lista_meds = inv_service.consultar_stock(False)
        nombres_meds = [med.get('nombre', 'Sin Nombre') for med in lista_meds] if lista_meds else []
        medicamentos_vinculados = st.multiselect("Medicamentos recetados (vinculación)", options=nombres_meds)
        
        tratamiento = st.text_area("Tratamiento/Instrucciones", height=300).strip()
        
        # Datalist de doctores
        user_service = users()
        lista_users = user_service.mostrar_usuarios()
        nombres_docs = [u.get('user', 'Desconocido') for u in lista_users] if lista_users else []
        doctor = st.selectbox("Doctor a cargo", options=[""] + nombres_docs)

        pdf = FPDF() #Creas el documento PDF
 
        pdf.add_page() #Agregas una hoja al documento

        pdf.set_font("Arial",'B', size=16) #Los parametros dentro son 3 e indican la fuente (arial), el estilo (negritas) y el tamaño (16)

        pdf.set_xy(60,15) #Mueves el cursor o el lapiz por llamarle de alguna forma a ciertas coordenadas (x,y)
        #Los primeros numeros son para indicar que tan grande quieres la caja que va a contener el texto, ln es para hacer un salto de linea para que el siguiente
        #texto quede abajo y no al lado, align para alinea ya sea izquierda(como es este caso), centro o derecha.
        pdf.cell(200, 3, txt="Clinica Privada Pit Ducan", ln=True, align='L')
        pdf.set_xy(75,30)
        pdf.cell(200, 3, txt="Receta Medica", ln=True, align='L')

        btn_genr = st.form_submit_button("Generar receta")
        if btn_genr: #El pdf solo se va a hacer cuando se pulse el boton 
            if edad.isdigit() and peso.isdigit() and paciente and doctor: #verificamos unos campos para que todo este en regla dentro del PDF
                #Basicamente de aqui a la linea 257 es lo mismo, nada mas cambia la posicion del cursor/lapiz y el texto que se va a escribir, nada mas explico algo en la linea 246 y 248
                pdf.set_font("Arial", size=11)
                pdf.set_xy(10, 45)
                pdf.cell(0, 10, txt=f"Fecha:{fecha}", ln=True, align='L')

                pdf.set_xy(10, 55) 
                pdf.set_font("Arial", 'B', size=11) 
                pdf.cell(40, 10, txt="Paciente:", align='L')
                pdf.set_font("Arial", size=11) 
                pdf.cell(0, 10, txt=paciente, ln=True, align='L')


                pdf.set_font("Arial", 'B', size=11)
                pdf.cell(15, 10, txt="Edad:", align='L')
                pdf.set_font("Arial", size=11)
                pdf.cell(30, 10, txt=f"{edad} años", align='L') 

                pdf.set_font("Arial", 'B', size=11)
                pdf.cell(15, 10, txt="Peso:", align='L')
                pdf.set_font("Arial", size=11)
                pdf.cell(30, 10, txt=f"{peso} kg", ln=True, align='L')

                pdf.set_xy(10, 75)
                pdf.set_font("Arial", 'B', size=11)
                pdf.cell(25, 10, txt="Diagnóstico:", align='L')
                pdf.set_font("Arial", size=11)

                pdf.set_xy(35, 78) 
                pdf.multi_cell(0, 5, txt=diagnostico) #Esta es una celda que puede almacenar mucho texto, si ve que el texto es muy largo, hace un salto de linea automatic
                #Genera un rectangulo, (X,Y) son para indicarle donde se va a colocar la esquina superior izquierda, apartir de ese punto se usa W y H para indicar
                #que el tamaño, y lo ultimo es el estilo ahi se le esta indicando que solo dibuje el borde y que lo deje vacio.
                pdf.rect(x=10, y=100, w=190, h=130,style="")  

                pdf.set_xy(15, 105)
                pdf.set_font("Arial", 'I', size=10) 
                
                # Armar el texto del tratamiento incluyendo medicinas seleccionadas
                texto_tratamiento = tratamiento
                if medicamentos_vinculados:
                    texto_tratamiento += "\n\nMedicamentos Recetados:\n- " + "\n- ".join(medicamentos_vinculados)
                
                pdf.multi_cell(0, 5, txt=f"Tratamiento / Instrucciones:\n{texto_tratamiento}")

                pdf.line(70, 255, 150, 255)
                pdf.set_font("Arial", size=12)
                pdf.set_xy(90,260)
                pdf.cell(200, 3, txt=f"Dr. {doctor}", ln=True, align='L')

                #este try sirve para indicar que intente buscar la imagen en la ruta, si no la encuentro el programa no muere y simplemente sigue sin la imagen
                #en caso de que la encuentre, se colocan las coordenadas y la w es para decir que quiero que mida 4mm la h no importa la calcula sola.
                try:
                    pdf.image(r"C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas\Proyecto_final V3\Proyecto\Logo Clinica.png", x=160, y=10, w=40)
                except:
                    pass
                
                # Datos ocultos al PDF generado (para verificar que es una receta real, simulado con texto blanco pequeño)
                pdf.set_font("Arial", size=1)
                pdf.set_text_color(255, 255, 255)
                pdf.set_xy(10, 285)
                firma_secreta = f"VALID_RECETA_{paciente}_{doctor}_{fecha}_SECRET123"
                pdf.cell(0, 1, txt=firma_secreta, ln=True)
                pdf.set_text_color(0, 0, 0)
                
                #Sirve para no guardar el PDF en un el disco duro de forma directa, 
                pdfm = pdf.output(dest='S')
                pdf_bytes_receta = pdfm.encode('latin-1')

                if pdf_bytes_receta:

                    st.session_state.pdf_receta_listo = pdf_bytes_receta
                    st.success("Receta generada, por favor descargar el PDF.")
                    
                else:
                    st.error("Hubo un error al generar el PDF.")
            else:
                st.error("Alguno de los campos esta mal llenado o no se a llenado.")

    if st.session_state.pdf_receta_listo is not None:
        st.download_button(
            label="Descargar receta",
            data=st.session_state.pdf_receta_listo,
            file_name=f"Receta para {paciente}.pdf",
            mime="application/pdf"
        )

def generar_factura():
    if 'pdf_factura_listo' not in st.session_state:
        st.session_state.pdf_factura_listo = None
    st.title("Generar Factura")

    with st.form("form_factura"):
        st.subheader("Datos de Facturación")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Datos del Cliente (Paciente)**")
            paciente = st.text_input("Nombre del Paciente").strip()
            direccion_pac = st.text_input("Dirección Paciente").strip()
            correo_pac = st.text_input("Correo Electrónico").strip()
            
        with col2:
            st.markdown("**Datos del Servicio**")
            
            # Datalist de doctores también en factura
            user_service = users()
            lista_users = user_service.mostrar_usuarios()
            nombres_docs = [u.get('user', 'Desconocido') for u in lista_users] if lista_users else []
            doctor = st.selectbox("Médico Tratante", options=[""] + nombres_docs)
            
            concepto = st.text_input("Descripción del Servicio").strip()
            costo = st.number_input("Total a Pagar ($)", min_value=0.0, value=500.0, step=50.0)

        enviado = st.form_submit_button("Generar y Guardar Factura")

    if enviado:
        if not paciente or not doctor or not concepto:
            st.warning("Por favor ingrese al menos el nombre del paciente, del doctor y el concepto.")
        else:
            fecha_str = datetime.date.today().strftime('%d/%m/%Y')
            folio = datetime.datetime.now().strftime('%H%M%S') 
            nombre_archivo_pdf = f"Factura_{folio}_{paciente}.pdf"

            pdf = FPDF()
            pdf.add_page()

            try:
                pdf.image(r"C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas\Proyecto_final V3\Proyecto\Logo Clinica.png", x=160, y=10, w=35)
            except:
                pass

            pdf.set_font("Arial", 'B', 16)
            pdf.set_text_color(44, 62, 80)
            pdf.set_xy(10, 15)
            pdf.cell(0, 10, "CLÍNICA PRIVADA PIT DUCAN", ln=True)
            
            pdf.set_font("Arial", size=9)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 5, "Andador Vikingos 102 El Morro, Boca del Rio", ln=True)
            pdf.cell(0, 5, "Tel: 22291416534 | Email: contacto@clinicapit.com", ln=True)

            pdf.ln(10)
            pdf.set_font("Arial", 'B', 24)
            pdf.set_text_color(0, 90, 120)
            pdf.cell(0, 10, "FACTURA", ln=True, align='C')
            
            pdf.set_font("Arial", size=10)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 5, f"Folio: {folio}  |  Fecha: {fecha_str}", ln=True, align='R')

            pdf.line(10, 60, 200, 60)

            y_bloques = 70
            
            pdf.set_xy(10, y_bloques)
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(90, 8, "FACTURAR A:", ln=True)
            pdf.set_font("Arial", size=10)
            pdf.cell(90, 5, f"Cliente: {paciente}", ln=True)
            pdf.cell(90, 5, f"Dirección: {direccion_pac}", ln=True)
            pdf.cell(90, 5, f"Email: {correo_pac}", ln=True)

            pdf.set_xy(110, y_bloques)
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(90, 8, "EMISOR / MÉDICO:", ln=True)
            pdf.set_x(110)
            pdf.set_font("Arial", size=10)
            pdf.cell(90, 5, f"Dr. {doctor}", ln=True)
            pdf.set_x(110)
            pdf.cell(90, 5, "Especialidad: Medicina General", ln=True)

            pdf.set_y(120)
            
            pdf.set_fill_color(0, 90, 120)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(130, 8, "Descripción", border=1, fill=True)
            pdf.cell(60, 8, "Importe", border=1, ln=True, align='C', fill=True)

            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Arial", size=10)
            pdf.cell(130, 10, concepto, border=1)
            pdf.cell(60, 10, f"$ {costo:.2f}", border=1, ln=True, align='R')

            pdf.set_font("Arial", 'B', 10)
            pdf.cell(130, 10, "SUBTOTAL", border=1, align='R')
            pdf.cell(60, 10, f"$ {costo:.2f}", border=1, ln=True, align='R')
            
            pdf.cell(130, 10, "IVA (16%)", border=1, align='R')
            iva = costo * 0.16
            pdf.cell(60, 10, f"$ {iva:.2f}", border=1, ln=True, align='R')

            pdf.set_fill_color(220, 220, 220) # Gris clarito para el total final
            pdf.cell(130, 10, "TOTAL NETO", border=1, align='R', fill=True)
            pdf.cell(60, 10, f"$ {costo + iva:.2f}", border=1, ln=True, align='R', fill=True)

            pdf.set_y(250)
            pdf.set_font("Arial", 'I', 8)
            pdf.cell(0, 5, "Gracias por su preferencia.", ln=True, align='C')
            pdf.cell(0, 5, "Este documento es una representación impresa de un servicio médico.", ln=True, align='C')

            pdfm = pdf.output(dest='S')
            pdf_bytes = pdfm.encode('latin-1')

            f = facturas()
            guardado = f.guardar_factura(paciente, doctor, concepto, costo + iva, nombre_archivo_pdf)

            if guardado:
                st.session_state.pdf_factura_listo = pdf_bytes
                st.success("Factura generada, por favor descargar el PDF.") 
            else:
                st.error("El PDF se creó, pero hubo un error al guardar en MongoDB.")
                
    if st.session_state.pdf_factura_listo is not None:
        st.download_button(
            label="Descargar factura",
            data=st.session_state.pdf_factura_listo,
            file_name=f"Factura para {paciente}.pdf",
            mime="application/pdf"
        )