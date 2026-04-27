import streamlit as st
from src.services.users import users



def interfaz_login():
    st.markdown("""
    <style>
    /* Color del texto que escribe el usuario */
    input[type="text"], input[type="password"] {
        color: #e2e8f0 !important;
        background-color: #111720 !important;
        border: 0.5px solid #1e2a3a !important;
        border-radius: 8px !important;
    }

    /* Color del label encima del input */
    label[data-testid="stWidgetLabel"] p {
        color: #a0aec0 !important;
        font-size: 13px !important;
    }

    /* Borde cuando está seleccionado (focus) */
    input[type="text"]:focus, input[type="password"]:focus {
        border-color: #4a9eff !important;
        box-shadow: 0 0 0 1px #4a9eff !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("LOGIN")
    user = st.text_input("Ingrese su nombre de usuario").strip()
    password = st.text_input("Ingrese su contraseña", type="password").strip()
    

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