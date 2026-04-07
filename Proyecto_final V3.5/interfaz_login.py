import streamlit as st
from user_streamlit import users

def interfaz_login():

    st.title("LOGIN")
    user = st.text_input("Ingrese su nombre de usuario")
    password = st.text_input("Ingrese su contraseña", type="password")
    

    if st.button("Iniciar sesion"):
        u = users()
        resultado = u.login(user,password)
        if  resultado:
         st.success(f"Bienvenido {user} !")
         st.session_state['usuario'] = resultado
         st.session_state['logeado'] = True

         if "admin" in user.lower():
           st.session_state['vista_actual'] = 'menu_admin'
         else:
            st.session_state['vista_actual'] = 'menu_medicos'
         st.rerun()
        
        else:
          st.error("Contraseña o Usuario Incorrecto: ")        