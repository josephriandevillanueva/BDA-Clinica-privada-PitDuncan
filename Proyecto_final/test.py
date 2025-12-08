import streamlit as st
#from interfaz_generar_usuario import interfaz_gusuario,ddb_usuario
from interfaces_menu_admin import ddb_usuario,interfaz_gusuario, mostrar_usuario
from interfaces_menu_doc import generar_recetita,datos_paciente,alta_paciente,baja_paciente
from interfaces_menu_inv import stock,certificaciones

from interfaz_login import interfaz_login
# 1. Inicializamos el estado (memoria) si no existe
if 'vista_actual' not in st.session_state:
    st.session_state['vista_actual'] = 'menu_principal'

def main():
    
    st.sidebar.image("Logo Clinica.png", width=200)
    with st.sidebar.container(border=True):
        st.markdown("**Informacion de la clinica**")
        st.write("**Dirección**: Andador Vikingos 102 El Morro, Boca del Rio")
        st.write("**Telefono**: 22291416534")
        st.write("**Soporte**: clinicaprivadapitduncan@gmail.com")
        

    # menú principal
    if st.session_state['vista_actual'] == 'menu_principal':
        st.title("Clinica privada Pit Duncan")

        
       
        if st.button("Generar Cita"):
            st.session_state['vista_actual'] = 'formulario_cita'
            st.rerun() # Esto fuerza a recargar la página inmediatamente
        
        elif st.button("Comprar medicinas"):
            st.session_state['vista_actual'] = 'formulario_compra_medicinas'
            st.rerun()

        elif st.button("Login"):
            st.session_state['vista_actual'] = 'formulario_login'
            st.rerun()



    elif st.session_state['vista_actual'] == 'formulario_cita':
        # Aquí ya no existe el botón de arriba, solo tu función
        st.write("No disponible")

    

         # Un botón extra para poder regresar
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_compra_medicinas':
        # Aquí ya no existe el botón de arriba, solo tu función
        st.write("No disponible")

    

         # Un botón extra para poder regresar
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_login':#interfaz login
        interfaz_login()
        
        
        
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_gusuario':#generar ususario
        interfaz_gusuario()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_eusuario':#dar de baja a un ususario
        ddb_usuario()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()
    
    elif st.session_state['vista_actual'] == 'formulario_musuarios':#mostrar a los ususario activos
        mostrar_usuario()
         
        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_admin'#menu de administrador
            st.rerun()

    
    elif st.session_state['vista_actual'] == 'formulario_receta':#generar una receta
        generar_recetita()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_datos_paciente':#consultar los datos de un paciente
        
        datos_paciente()

        if st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_ingresar_paciente':#dar de alta a un paciente

        alta_paciente()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_baja_paciente':
        
        baja_paciente()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_medicos'
           st.rerun()


    elif st.session_state['vista_actual'] == 'formulario_stock':#consultar el stock de la clinica
        stock()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_inventario'
           st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_certificaciones':#certificaciones de la clinica
        certificaciones()

        if st.button("Volver al Menú"):
           st.session_state['vista_actual'] = 'menu_inventario'
           st.rerun()



    


    

    elif st.session_state['vista_actual'] == 'menu_admin':

        st.title("Menu de administrador")
        if st.button("Crear Usuario"):
            st.session_state['vista_actual'] = 'formulario_gusuario'
            st.rerun()
        elif st.button("Dar de baja usuario"):
            st.session_state['vista_actual'] = 'formulario_eusuario'
            st.rerun()
        elif st.button("Mostrar Usuarios activos"):
            st.session_state['vista_actual'] = 'formulario_musuarios'
            st.rerun()

        elif st.button("Desplegar menu de inventario"):
            st.session_state['vista_actual'] = 'menu_inventario'#desplego del menu del inventario
            st.rerun()


        elif st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()


    elif st.session_state['vista_actual'] == 'menu_inventario':
        st.title("Menu de inventario")

        if st.button("Consultar el Stock de la clinica"):
            st.session_state['vista_actual'] = 'formulario_stock'
            st.rerun()

        elif st.button("Verificar Certificaciones"):
            st.session_state['vista_actual'] ='formulario_certificaciones'
            st.rerun()

        elif st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()




    elif st.session_state['vista_actual'] == 'menu_medicos':
        st.title("Menu de medicos")

        if st.button("Prescribir una receta"):
            st.session_state['vista_actual'] = 'formulario_receta'
            st.rerun()

        elif st.button("Ingresar un paciente"):
            st.session_state['vista_actual'] ='formulario_ingresar_paciente'
            st.rerun()


        elif st.button("Buscar datos medicos de un paciente"):
            st.session_state['vista_actual'] = 'formulario_datos_paciente'
            st.rerun()

        elif st.button("Dar de baja un paciente"):
            st.session_state['vista_actual'] = 'formulario_baja_paciente'
            st.rerun()


        elif st.button("Volver al Menú"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()
    




    


        






if __name__ == "__main__":
    main()