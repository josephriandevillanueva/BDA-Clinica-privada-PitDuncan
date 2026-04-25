import streamlit as st
from user_streamlit import users

def ddb_usuario():
    st.title("Dar de baja usuario")
    user = st.text_input("Nombre del usuario que quiere dar de baja")

    if st.button("Dar de baja"):
        u = users()

        resultado = u.dar_de_baja(user)

        if not resultado:
            st.success(f"{user} ha sido dado de baja")
        else:
            st.error("No se pudo dar de baja al ususario")

def interfaz_gusuario():

 st.title("Generar Usuario")

 # 1. Los inputs son widgets visuales
 nuevo_user = st.text_input("Nombre de usuario")
 nuevo_pass = st.text_input("Contraseña", type="password")

 # 2. El botón dispara la acción
 if st.button("Crear Usuario"):
     u = users()
     # Llamamos a la función limpia pasando los datos
     resultado = u.generar_usuario(nuevo_user, nuevo_pass)
    
     if not resultado:
         st.success("Usuario creado correctamente")
     else:
         st.error("No se pudo crear: ")


def mostrar_usuario():
 

  st.header("usuarios activos")

 
 

  u = users()
 # Llamamos a la función limpia pasando los datos
  resultado = u.mostrar_usuarios()

  if len(resultado) >0:
     st.dataframe(resultado, use_container_width=True)

  else:
     st.warning("No se encontraron usuarios activos.")