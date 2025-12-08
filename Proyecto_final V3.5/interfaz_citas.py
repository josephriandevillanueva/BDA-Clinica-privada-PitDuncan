import streamlit as st
from datetime import datetime
from citas import agendar_citas

def form_cita():
    st.title("Agende una cita")

    with st.form("formulario_citas"):
        
        nombre = st.text_input("Ingrese su nombre:")
        especialista = st.text_input("Ingrese el especialista que necesita (ej: Dermatologo):")

        col1, col2 = st.columns(2)
        
        with col1:
            fecha = st.date_input("Fecha de la cita")
        
        with col2:
            hora = st.time_input("Hora", step=1800) 

        enviado = st.form_submit_button("Agendar")

    if enviado:
        if not nombre or not especialista:
            st.error("Por favor complete todos los campos")
        else:
            fecha_hora_mongo = datetime.combine(fecha, hora)
            ag = agendar_citas()
            resultado = ag.generar_cita(nombre,especialista,fecha_hora_mongo)

            if resultado:
            	st.success("Cita agendada.")

def ver_citas():
    st.header("Citas")

    with st.form("mostrar_cita"):
        nombre_comp = st.text_input("Nombre completo: ").strip()

        env = st.form_submit_button("Ver citas")

    if env:
        if not nombre_comp:
            st.error("Por favor complete el campo.")
        else:
            ag = agendar_citas()
            c = ag.mostrar_cita(nombre_comp)

            if len(c) >0:
                st.dataframe(c, use_container_width=True)

            else:
               st.warning("No se encontro la cita para este paciente.")

