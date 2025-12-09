import streamlit as st
from user_streamlit import users


def menu_user():
    st.title("Usuarios")

    pes1, pes2, pes3 = st.tabs(["Ingresar usuario", "Dar de baja usuario", "Ver usuarios activos"])

    with pes1:
        st.header("Generar Usuario")
        nuevo_user = st.text_input("Nombre de usuario",key="alta_nuse")
        nuevo_pass = st.text_input("Contraseña", type="password",key="alta_npass")

        if st.button("Crear Usuario",key="alta_btn"):
            u = users()
            resultado = u.generar_usuario(nuevo_user, nuevo_pass)

            if not resultado:
                st.success("Usuario creado correctamente")
            else:
                st.error("No se pudo crear: ",key="alta_error")

    with pes2:
        st.header("Dar de baja usuario")
        user = st.text_input("Nombre del usuario que quiere dar de baja",key="baja_user")

        if st.button("Dar de baja",key="baja_btn"):
            u = users()

            resultado = u.dar_de_baja(user)

            if not resultado:
                st.success(f"{user} ha sido dado de baja",key="baja_scs")
            else:
                st.error("No se pudo dar de baja al usuario",key="baja_error")

    with pes3:
        st.header("Usuarios activos")

        u = users()

        resultado = u.mostrar_usuarios()

        if len(resultado) >0:
            st.dataframe(resultado, use_container_width=True)

        else:
            st.warning("No se encontraron usuarios activos.",key="masbaja_error")
   