import streamlit as st
from user_streamlit import users
from datetime import datetime
from fpdf import FPDF
from user_streamlit import users
from pacientes import pacientes
def generar_recetita():
    
    st.title("Receta medica")
    fecha = datetime.today().strftime('%d/%m/%Y')#fecha actual
    paciente = st.text_input("Nombre del paciente")
    edad = st.text_input("Edad del paciente")
    peso = st.text_input("Peso del paciente")
    diagnostico = st.text_input("Diagnostico")
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
     pdf.cell(0, 10, txt="Tratamiento / Instrucciones:")

    
     pdf.line(70, 255, 150, 255)
     pdf.set_font("Arial", size=12)
     pdf.set_xy(90,260)
     pdf.cell(200, 3, txt=f"Dr. {doctor}", ln=True, align='L')

     pdf.image(r"C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas\Proyecto_final\Logo Clinica.png", x=160, y=10, w=40)
    




     pdf_filename = f"receta{paciente}.pdf"
     pdf.output(pdf_filename)
     print(f"PDF '{pdf_filename}' Receta generada")

def datos_paciente():
   
   st.header("Datos del paciente")

   nombre = st.text_input("Nombre del paciente")
   ap = st.text_input("Apellido paterno del paciente")
   am = st.text_input("Apellido materno del paciente")

   p = pacientes()


   if st.button("Buscar"):
      
      resultado = p.consultar_datos_medicos(nombre,ap,am)

      if len(resultado) >0:
        st.dataframe(resultado, use_container_width=True)

      else:
        st.warning("No se encontraron usuarios activos.")

def alta_paciente():
   st.header("Alta de paciente")

   nombre = st.text_input("Nombre del paciente")
   ap = st.text_input("Apellido paterno del paciente")
   am = st.text_input("Apellido materno del paciente")
   DOB = st.date_input("Fecha de nacimiento")
   tel = st.text_input("telefono")
   email = st.text_input("correo electronico")
   st.write("**Direccion del paciente**")
   calle = st.text_input("calle")
   nint = st.text_input("N.O interior")
   next = st.text_input("N.O exterior")
   col = st.text_input("colonia")
   cp = st.text_input("codigo postal")
   cd = st.text_input("ciudad")
   st.write("**Contacto de emergencia  del paciente**")
   nc = st.text_input("nombre del contacto")
   pa = st.text_input("parentesto")
   telc = st.text_input("telefono contacto")
   st.write("**datos medicos del paciente**")
   ts = st.text_input("tipo de sangre")
   alergias = st.text_input("alergias")

   p = pacientes()

   if st.button("Ingresar"):
      resultado = p.dar_de_alta_paciente(nombre,ap,am,DOB,tel,email,calle,nint,next,col,cp,cd,nc,pa,telc,ts,alergias)

      if not resultado:
         st.success("Paciente ingresado")
      else:
         st.error("No se pudo ingresar al paciente: ")


def baja_paciente():
   st.header("Baja de paciente")

   nombre = st.text_input("Nombre del paciente")
   ap = st.text_input("Apellido paterno del paciente")
   am = st.text_input("Apellido materno del paciente")

   p = pacientes()

   if st.button("Dar de baja"):
      resultado = p.dar_de_baja_paciente(nombre,ap,am)

      if not resultado:
            st.success(f"{nombre} {ap} {am} ha sido dado de baja del sistema")
      else:
          st.error("No se pudo dar de baja al Paciente")

      
  


