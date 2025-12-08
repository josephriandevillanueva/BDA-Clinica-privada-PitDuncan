import streamlit as st
import pandas as pd
from user_streamlit import users
from datetime import datetime
from fpdf import FPDF
from user_streamlit import users
from pacientes import pacientes
from facturas import facturas

def menu():
    st.title("Pacientes")

    pes1, pes2, pes3 = st.tabs(["Ingresar paciente", "Dar de baja paciente", "Ver pacientes"])

    with pes1:
        st.header("Alta de paciente")

        nombre = st.text_input("Nombre del paciente", key="alta_nombre")
        ap = st.text_input("Apellido paterno del paciente", key="alta_ap")
        am = st.text_input("Apellido materno del paciente", key="alta_am")
        
        DOB = st.date_input("Fecha de nacimiento", key="alta_dob")
        tel = st.text_input("telefono", key="alta_tel")
        email = st.text_input("correo electronico", key="alta_email")
        
        st.write("**Direccion del paciente**")
        calle = st.text_input("calle", key="alta_calle")
        nint = st.text_input("N.O interior", key="alta_nint")
        next = st.text_input("N.O exterior", key="alta_next")
        col = st.text_input("colonia", key="alta_col")
        cp = st.text_input("codigo postal", key="alta_cp")
        cd = st.text_input("ciudad", key="alta_cd")
        
        st.write("**Contacto de emergencia del paciente**")
        nc = st.text_input("nombre del contacto", key="alta_nc")
        pa = st.text_input("parentesto", key="alta_pa")
        telc = st.text_input("telefono contacto", key="alta_telc") 
        
        st.write("**datos medicos del paciente**")
        ts = st.text_input("tipo de sangre", key="alta_ts")
        alergias = st.text_input("alergias", key="alta_alergias")

        p = pacientes()

        if st.button("Ingresar", key="btn_ingresar"):
             resultado = p.dar_de_alta_paciente(nombre,ap,am,DOB,tel,email,calle,nint,next,col,cp,cd,nc,pa,telc,ts,alergias)

             if resultado:
                 st.success("Paciente ingresado")
             else:
                 st.error("No se pudo ingresar al paciente.")

    with pes2:
        st.header("Baja de paciente")

        nombre1 = st.text_input("Nombre del paciente", key="baja_nombre")
        ap1 = st.text_input("Apellido paterno del paciente", key="baja_ap")
        am1 = st.text_input("Apellido materno del paciente", key="baja_am")

        p1 = pacientes()

        if st.button("Dar de baja", key="btn_baja"):
             resultado1 = p1.dar_de_baja_paciente(nombre1,ap1,am1)

             if resultado1: # Si es True
                 st.success(f"{nombre1} {ap1} {am1} ha sido dado de baja del sistema")
             else:
                 st.error("No se pudo dar de baja al Paciente")

    with pes3:
        st.header("Ver pacientes")

        with st.form("forma_paciente"):
            nombre = st.text_input("Nombre del paciente",key="mas_baja_nom").strip()
            ap = st.text_input("Apellido paterno del paciente",key="mas_baja_app").strip()
            am = st.text_input("Apellido materno del paciente",key="mas_baja_apm").strip()

            btn_all = st.form_submit_button("Ver todos los pacientes.",key="mas_baja_all")
            btn_one = st.form_submit_button("Buscar paciente.",key="mas_baja_one")

            if btn_all:

                p2 = pacientes()
                result = p2.mostrar_pacientes()
                
                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","apellido paterno","apellido materno","fecha de nacimiento","telefono","email","Direccion","Contacto de emergencia","fecha de registro","activo"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun paciente")

            if btn_one:
                p3 = pacientes()
                result = p3.mostrar_un_paciente(nombre,ap,am)
                
                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","apellido paterno","apellido materno","fecha de nacimiento","telefono","email","Direccion","Contacto de emergencia","fecha de registro","activo"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun paciente")


def generar_recetita():
    
    st.title("Receta medica")
    fecha = datetime.today().strftime('%d/%m/%Y')#fecha actual
    paciente = st.text_input("Nombre del paciente")
    edad = st.text_input("Edad del paciente")
    peso = st.text_input("Peso del paciente")
    diagnostico = st.text_input("Diagnostico")
    tratamiento = st.text_area("Tratamiento/Instrucciones",height=300)
    doctor = st.text_input("Doctor a cargo")

    pdf = FPDF()

   
    pdf.add_page()


    pdf.set_font("Arial",'B', size=16)

    pdf.set_xy(60,15)
    pdf.cell(200, 3, txt="Clinica Privada Pit Ducan", ln=True, align='L')
    pdf.set_xy(75,30)
    pdf.cell(200, 3, txt="Receta Medica", ln=True, align='L')

    # la fecha hasta la izquierda  pero que quede debajo de la celda de receta medica
    #en el espacio en blanco: nombre del paciente(el nombre completo todo junto),edad , peso y diagnostico 


    if st.button("Generar receta"):
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
        # Usamos multi_cell por si el diagnóstico es largo y necesita bajar de renglón
        pdf.set_xy(35, 78) 
        pdf.multi_cell(0, 5, txt=diagnostico)

        pdf.rect(x=10, y=100, w=190, h=130,style="")

        pdf.set_xy(15, 105)
        pdf.set_font("Arial", 'I', size=10) 
        pdf.cell(0, 10, txt=f"Tratamiento / Instrucciones: \n {tratamiento}")



        pdf.line(70, 255, 150, 255)
        pdf.set_font("Arial", size=12)
        pdf.set_xy(90,260)
        pdf.cell(200, 3, txt=f"Dr. {doctor}", ln=True, align='L')

        try:
            pdf.image(r"C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas\Proyecto_final V3\Proyecto\Logo Clinica.png", x=160, y=10, w=40)
        except:
            pass
        
        pdfm = pdf.output(dest='S')
        pdf_bytes = pdfm.encode('latin-1')

        if pdf_bytes:
            st.success("Receta generada")
            
            st.download_button(
                label="Descargar PDF",
                data=pdf_bytes,
                file_name=f"Receta para {paciente}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Hubo un error al generar el PDF.")

def datos_paciente():
   st.header("Datos del paciente")

   # Usamos .strip() para limpiar espacios accidentales
   nombre = st.text_input("Nombre del paciente").strip()
   ap = st.text_input("Apellido paterno del paciente").strip()
   am = st.text_input("Apellido materno del paciente").strip()

   p = pacientes()

   if st.button("Buscar"):
      
        result = p.consultar_datos_medicos(nombre, ap, am)

        if len(result) >0:
            one = pd.DataFrame(result)
            one = one[["nombre","apellido paterno","apellido materno","tipo de sangre","alergias"]]
            st.dataframe(one, use_container_width=True,hide_index=True)

        else:
           st.error("No se encontro ningun paciente")
  
def generar_factura():
    st.title("Generar Factura")

    # --- 1. FORMULARIO DE DATOS ---
    with st.form("form_factura"):
        st.subheader("Datos de Facturación")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Datos del Cliente (Paciente)**")
            paciente = st.text_input("Nombre del Paciente")
            direccion_pac = st.text_input("Dirección Paciente")
            correo_pac = st.text_input("Correo Electrónico")
            
        with col2:
            st.markdown("**Datos del Servicio**")
            doctor = st.text_input("Médico Tratante")
            concepto = st.text_input("Descripción del Servicio")
            costo = st.number_input("Total a Pagar ($)", min_value=0.0, value=500.0, step=50.0)

        enviado = st.form_submit_button("Generar y Guardar Factura")

    # --- 2. LÓGICA DE GENERACIÓN ---
    if enviado:
        if not paciente or not doctor:
            st.warning("Por favor ingrese al menos el nombre del paciente y del doctor.")
        else:
            # Datos automáticos
            fecha_str = datetime.today().strftime('%d/%m/%Y')
            folio = datetime.now().strftime('%H%M%S') # Folio basado en la hora
            nombre_archivo_pdf = f"Factura_{folio}_{paciente}.pdf"

            # --- INICIO DEL DISEÑO PDF ---
            pdf = FPDF()
            pdf.add_page()

            # A. LOGO
            try:
                # Ajusta la ruta si es necesario
                pdf.image("Logo Clinica.png", x=160, y=10, w=35)
            except:
                pass # Si no hay logo, no pasa nada

            # B. ENCABEZADO CLÍNICA
            pdf.set_font("Arial", 'B', 16)
            pdf.set_text_color(44, 62, 80) # Un color azul oscuro profesional
            pdf.set_xy(10, 15)
            pdf.cell(0, 10, "CLÍNICA PRIVADA PIT DUCAN", ln=True)
            
            pdf.set_font("Arial", size=9)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 5, "Andador Vikingos 102 El Morro, Boca del Rio", ln=True)
            pdf.cell(0, 5, "Tel: 22291416534 | Email: contacto@clinicapit.com", ln=True)

            # C. TÍTULO FACTURA
            pdf.ln(10)
            pdf.set_font("Arial", 'B', 24)
            pdf.set_text_color(0, 90, 120) # Azul tipo "Factura"
            pdf.cell(0, 10, "FACTURA", ln=True, align='C')
            
            pdf.set_font("Arial", size=10)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 5, f"Folio: {folio}  |  Fecha: {fecha_str}", ln=True, align='R')

            pdf.line(10, 60, 200, 60) # Línea separadora

            # D. BLOQUES DE INFO (Cliente vs Médico)
            y_bloques = 70
            
            # Izquierda: Cliente
            pdf.set_xy(10, y_bloques)
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(90, 8, "FACTURAR A:", ln=True)
            pdf.set_font("Arial", size=10)
            pdf.cell(90, 5, f"Cliente: {paciente}", ln=True)
            pdf.cell(90, 5, f"Dirección: {direccion_pac}", ln=True)
            pdf.cell(90, 5, f"Email: {correo_pac}", ln=True)

            # Derecha: Médico (Usamos set_xy para movernos a la derecha)
            pdf.set_xy(110, y_bloques)
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(90, 8, "EMISOR / MÉDICO:", ln=True)
            pdf.set_x(110)
            pdf.set_font("Arial", size=10)
            pdf.cell(90, 5, f"Dr. {doctor}", ln=True)
            pdf.set_x(110)
            pdf.cell(90, 5, "Especialidad: Medicina General", ln=True)

            # E. TABLA DE SERVICIOS
            pdf.set_y(120)
            
            # Encabezado Tabla
            pdf.set_fill_color(0, 90, 120) # Fondo Azul
            pdf.set_text_color(255, 255, 255) # Texto Blanco
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(130, 8, "Descripción", border=1, fill=True)
            pdf.cell(60, 8, "Importe", border=1, ln=True, align='C', fill=True)

            # Fila de Datos
            pdf.set_text_color(0, 0, 0) # Texto Negro
            pdf.set_font("Arial", size=10)
            pdf.cell(130, 10, concepto, border=1)
            pdf.cell(60, 10, f"$ {costo:.2f}", border=1, ln=True, align='R')

            # Totales
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(130, 10, "SUBTOTAL", border=1, align='R')
            pdf.cell(60, 10, f"$ {costo:.2f}", border=1, ln=True, align='R')
            
            pdf.cell(130, 10, "IVA (16%)", border=1, align='R')
            iva = costo * 0.16
            pdf.cell(60, 10, f"$ {iva:.2f}", border=1, ln=True, align='R')

            pdf.set_fill_color(220, 220, 220) # Gris clarito para el total final
            pdf.cell(130, 10, "TOTAL NETO", border=1, align='R', fill=True)
            pdf.cell(60, 10, f"$ {costo + iva:.2f}", border=1, ln=True, align='R', fill=True)

            # F. PIE DE PÁGINA
            pdf.set_y(250)
            pdf.set_font("Arial", 'I', 8)
            pdf.cell(0, 5, "Gracias por su preferencia.", ln=True, align='C')
            pdf.cell(0, 5, "Este documento es una representación impresa de un servicio médico.", ln=True, align='C')

            # --- GUARDAR PDF ---
            pdfm = pdf.output(dest='S')
            pdf_bytes = pdfm.encode('latin-1')

            # --- 3. GUARDAR EN MONGODB ---
            f = facturas()
            guardado = f.guardar_factura(paciente, doctor, concepto, costo + iva, nombre_archivo_pdf)

            if guardado:
                st.success("Factura generada y guardada en la base de datos.")
                
                st.download_button(
                    label="Descargar PDF",
                    data=pdf_bytes,
                    file_name=f"Factura para {paciente}.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("El PDF se creó, pero hubo un error al guardar en MongoDB.")