import streamlit as st
#from interfaz_generar_usuario import interfaz_gusuario,ddb_usuario
from interfaces_menu_admin import menu_user
from interfaces_menu_doc import generar_recetita,generar_factura,menu
from interfaces_menu_inv import menu_inv,comprar_medicina
from interfaz_citas import menu_citas
from interfaz_login import interfaz_login
# 1. Inicializamos el estado (memoria) si no existe
if 'vista_actual' not in st.session_state:
    st.session_state['vista_actual'] = 'menu_principal'

def main():
    try:
        pathlogo = r"C:\Users\jonyx\OneDrive\Documentos\Universidad\Semestre 9\BDA\ProyectosFinal\ProyectoFinal_Local\logo3.png"
        st.sidebar.image(pathlogo, width=200)
    except:
        pass
    
    with st.sidebar.container(border=True):
        st.markdown("**Informacion de la clinica**")
        st.write("**Dirección**: Andador Vikingos 102 El Morro, Boca del Rio")
        st.write("**Telefono**: 22291416534")
        st.write("**Soporte**: clinicaprivadapitduncan@gmail.com")
        
    # menú principal
    if st.session_state['vista_actual'] == 'menu_principal':
        st.title("Clinica privada Pit Duncan")

        if st.button("Login"):
            st.session_state['vista_actual'] = 'formulario_login'
            st.rerun()

        elif st.button("Generar Cita"):
            st.session_state['vista_actual'] = 'formulario_cita1'
            st.rerun() # Esto fuerza a recargar la página inmediatamente

        elif st.button("Comprar medicina"):
            st.session_state['vista_actual'] = 'formulario_compra_medicinas'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_cita1':#--------------------------------------------------------------------------------------------
        cita_aux1 = False
        menu_citas(cita_aux1)

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_cita2':#--------------------------------------------------------------------------------------------
        cita_aux2 = True
        menu_citas(cita_aux2)

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_compra_medicinas':
        comprar_medicina()
        #st.write("Seguimos en obra negra, favor de regresar mas tarde.")
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_login':#interfaz login
        interfaz_login()
        
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_gusuario':#generar ususario
        menu_user()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()
    
    elif st.session_state['vista_actual'] == 'formulario_receta':#generar una receta
        generar_recetita()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_ingresar_paciente':
        menu()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()

    elif st.session_state['vista_actual'] == 'crear_factura':
        generar_factura()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()

    elif st.session_state['vista_actual'] == 'ver_citas':
        ver_citas()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_inv1':#consultar el stock de la clinica
        aux1 = True
        menu_inv(aux1)

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_admin'
           st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_inv2':#certificaciones de la clinica
        aux2 = False
        menu_inv(aux2)

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()

    elif st.session_state['vista_actual'] == 'menu_admin':

        st.title("Menu de administrador")
        if st.button("Usuarios"):
            st.session_state['vista_actual'] = 'formulario_gusuario'
            st.rerun()

        elif st.button("Inventario"):
            st.session_state['vista_actual'] = 'formulario_inv1'
            st.rerun()

        elif st.button("Cerrar Sesion"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'menu_medicos':
        st.title("Menu de medicos")

        if st.button("Prescribir una receta"):
            st.session_state['vista_actual'] = 'formulario_receta'
            st.rerun()

        elif st.button("Pacientes"):
            st.session_state['vista_actual'] ='formulario_ingresar_paciente'
            st.rerun()

        elif st.button("Generar factura"):
            st.session_state['vista_actual'] = 'crear_factura'
            st.rerun()

        elif st.button("Inventario"):
            st.session_state['vista_actual'] = 'formulario_inv2'
            st.rerun()

        elif st.button("Citas"):
            st.session_state['vista_actual'] = 'formulario_cita2'
            st.rerun()

        elif st.button("Cerrar Sesion"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()
    
if __name__ == "__main__":
    main()