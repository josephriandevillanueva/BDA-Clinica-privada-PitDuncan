import streamlit as st
from datetime import datetime
from citas import agendar_citas

def menu_citas(aux):
    st.title("Menu de Citas")

    pes1,pes2 = st.tabs(["Agendar una cita","Ver citas"])

    with pes1:
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

    with pes2:
        if aux == True:
            st.header("Citas")

            with st.form("mostrar_cita"):
                nombre_comp = st.text_input("Nombre completo: ").strip()

                colu1,colu2 = st.columns(2)

                with colu1:
                    vuc = st.form_submit_button("Ver cita")

                with colu2:
                    vtc = st.form_submit_button("Ver todas la citas.")

            if vuc:
                if not nombre_comp:
                    st.error("Por favor complete el campo.")
                else:
                    ag = agendar_citas()
                    c = ag.mostrar_cita(nombre_comp)

                    if len(c) >0:
                        st.dataframe(c, use_container_width=True)

                    else:
                       st.warning("No se encontro la cita para este paciente.")

            if vtc:
                ag = agendar_citas()
                c = ag.mostrar_todas_citas()

                if len(c) >0:
                    st.dataframe(c, use_container_width=True)

                else:
                   st.warning("No hay citas registradas")
        else:
            st.write("Para ver este apartado necesita iniciar sesion.")