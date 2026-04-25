import streamlit as st
import pandas as pd
from user_streamlit import users
from inventario import inventario


def stock():
    st.header("Stock de la clinica")

    with st.form("formulario_stock"):

        medicamento = st.text_input("Ingrese el nombre del medicamento o inicial.")
        stk = st.number_input("Ingrese el numero de Stock.")

        bt_one = st.form_submit_button("Ver producto")
        bt_all = st.form_submit_button("Ver Stock Completo")
        mayq = st.form_submit_button("Stock mayor o igual que")
        menq = st.form_submit_button("Stock menor o igual que")
        
        if bt_one:
            if not medicamento:
                st.warning("Ingrese al menos una inicial.")
            else:
                up = inventario()
                result = up.consultar_producto(medicamento)
                
                if len(result) >0:
                    one = pd.DataFrame(result)
                    one = one[["nombre","stock_total","descripcion"]]
                    st.dataframe(one, use_container_width=True,hide_index=True)

                else:
                   st.error("No se encontro ningun producto con esa/s inicial/es.")

        if bt_all:
            i = inventario()

            resultado = i.consultar_stock()

            if len(resultado) >0:
                df = pd.DataFrame(resultado)
                df = df[["nombre","stock_total","descripcion"]]
                st.dataframe(df, use_container_width=True,hide_index=True)

            else:
               st.error("Stock vacio.")

        if mayq:
            mayq = inventario()
            resultado = mayq.stock_mayor(stk)

            if len(resultado) >0:
                df = pd.DataFrame(resultado)
                df = df[["nombre","stock_total","descripcion"]]
                st.dataframe(df, use_container_width=True,hide_index=True)

            else:
               st.error("Stock vacio.")

        if menq:
            menq = inventario()
            resultado = menq.stock_menor(stk)

            if len(resultado) >0:
                df = pd.DataFrame(resultado)
                df = df[["nombre","stock_total","descripcion"]]
                st.dataframe(df, use_container_width=True,hide_index=True)
            else:
               st.error("Stock vacio.")


def certificaciones():
   st.header("Certificaciones")

   i = inventario()

   resultado = i.consultar_certificaciones()

   if len(resultado) >0:
        st.dataframe(resultado, use_container_width=True)

   else:
       st.warning("No hay certificaciones que mostrar.")