#Aqui llamamos a otros archivos y sus funciones y otras librerias
import streamlit as st
from user_streamlit import users

#funcion para poder ingresar nuevos usuarios que se puedan logear, dar de baja y ver usuario que aun estan activos
def menu_user():
    #Titulo del menu
    st.title("Usuarios")
    #Creamos pestañas para tener todo en una ventana y tener un orden
    pes1, pes2, pes3 = st.tabs(["Ingresar usuario", "Dar de baja usuario", "Ver usuarios activos"])
    #La primera pestaña es para poder ingresar un nuevo usuario
    with pes1:
        st.header("Generar Usuario") #Titulo de la pestaña
        with st.form("formulario_users"): #Para poder crear un frame y todo lo que se cree se quede dentro es mas por estetica
            nuevo_user = st.text_input("Nombre de usuario",key="alta_nuse").strip() #Campo de texto para usuario
            nuevo_pass = st.text_input("Contraseña", type="password",key="alta_npass").strip() #type="password sirve para poder convertir el text_input en un campo modificado para passwors"
            btn_user = st.form_submit_button("Crear Usuario",key="alta_btn") #Boton que da la instruccion de ingresar el usuario
            if btn_user: #Esto solo se va a activar si el boton se pulsa
                if nuevo_user and nuevo_pass: #Aqui verifica si los campos estan llenos
                    u = users() #llamamos la clase del archivo user_streamlit y lo metemos a una variable
                    resultado = u.generar_usuario(nuevo_user, nuevo_pass) #llamamos esta funcion de la clase del archivo user_streamlit y le colocamos sus respectivos parametos

                    if resultado: #Si resultado es True...
                        st.success("Usuario creado correctamente")#Va a mandar este mensaje al usuario
                    else:
                        st.error("No se pudo crear: ")#En caso de que no pues va a mandar este otro mensaje
                else:
                    st.warning("Favor de llenar los campos de forma correcta.") #En caso de que no esten llenos los campos manda una advertencia

    with pes2: #Pestaña para dar de baja-
        st.header("Dar de baja usuario")
        with st.form("formulario_baja_users"):
            user = st.text_input("Nombre del usuario que quiere dar de baja",key="baja_user").strip() #Mas campos de texto
            btn_baja = st.form_submit_button("Dar de baja",key="baja_btn")
            if btn_baja: #Esto solo se va a activar si el boton se pulsa
                if user:#Verifica si el campo de user esta completo
                    u = users() #Llama la clase del archivo antes mencionado

                    resultado = u.dar_de_baja(user) #Llama una de las funciones de la clase con su respectivos parametros

                    if resultado==True: #Si es verdadero
                        st.success(f"{user} ha sido dado de baja") #avisa que el usuario a sido dado de baja
                    else:
                        st.error("No se pudo dar de baja al usuario") #en caso de que no tambien avisa
                else:
                    st.warning("Porfavor ingresar un nombre de un usuario.") #en caso de que no haya nada en el campo de user avisa

    with pes3: #Pestaña para mostrar todos los usuarios que se pueden logear en la BD
        st.header("Usuarios activos")
        
        u = users()#Llama la clase del archivo antes mencionado

        resultado = u.mostrar_usuarios()#Llama una de las funciones de la clase con su respectivos parametros

        if len(resultado) >0: #Aqui revisa el tamaño de la lista que regresa la funcion anterior y que sea mayor a 0
            st.dataframe(resultado, use_container_width=True) #dataframe sirve para colocar los datos en una tabla, streamlit se escarga de acomodarlo, use_container_widht=True sirve para hacer la tabla mas grande.

        else:
            st.warning("No se encontraron usuarios activos.",key="masbaja_error")#En caso de que no haya nada pues va a ser igual a 0 por lo tanto no hay usuarios en la BD
   