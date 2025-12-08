import streamlit as st
from user_streamlit import users
from inventario import inventario


def stock():
    st.header("Stock de la clinica")

    i = inventario()

    resultado = i.consultar_stock()

    if len(resultado) >0:
     st.dataframe(resultado, use_container_width=True)

    else:
       st.warning("Stock vacio.")

       

def certificaciones():
   st.header("Certificaciones")

   i = inventario()

   resultado = i.consultar_certificaciones()

   if len(resultado) >0:
     st.dataframe(resultado, use_container_width=True)

   else:
       st.warning("No hay certificaciones que mostrar.")

