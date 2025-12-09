from fpdf import FPDF
from datetime import datetime
def crear_pdf():
    
  

   
    pdf = FPDF()

   
    pdf.add_page()

    fecha = datetime.today().strftime('%d/%m/%Y')#fecha actual
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    edad = input("edad: ")
    peso = input("peso: ")
    diagnostico = input("diagnostico:")
    doctor = input("doctor: ")

    pdf.set_font("Arial",'B', size=16)

    pdf.set_xy(60,15)
    pdf.cell(200, 3, txt="Clinica Privada Pit Ducan", ln=True, align='L')
    pdf.set_xy(75,30)
    pdf.cell(200, 3, txt="Receta Medica", ln=True, align='L')

    # la fecha hasta la izquierda  pero que quede debajo de la celda de receta medica
    #en el espacio en blanco: nombre del paciente(el nombre completo todo junto),edad , peso y diagnostico 


    pdf.set_font("Arial", size=11)
    pdf.set_xy(10, 45)
    pdf.cell(0, 10, txt=f"Fecha:{fecha}", ln=True, align='L')


    pdf.set_xy(10, 55) 
    pdf.set_font("Arial", 'B', size=11) 
    pdf.cell(40, 10, txt="Paciente:", align='L')
    pdf.set_font("Arial", size=11) 
    pdf.cell(0, 10, txt=nombre_paciente, ln=True, align='L')


    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(15, 10, txt="Edad:", align='L')
    pdf.set_font("Arial", size=11)
    pdf.cell(30, 10, txt=edad, align='L') 

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(15, 10, txt="Peso:", align='L')
    pdf.set_font("Arial", size=11)
    pdf.cell(30, 10, txt=peso, ln=True, align='L')

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
    




    pdf_filename = "ejemplo_receta.pdf"
    pdf.output(pdf_filename)
    print(f"PDF '{pdf_filename}' Receta generada")


