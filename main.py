import streamlit as st
import os

# Imports from views (UI)
from src.views.admin_view import menu_user
from src.views.doctor_view import generar_recetita, generar_factura, menu
from src.views.inventory_view import menu_inv, comprar_medicina
from src.views.appointments_view import menu_citas
from src.views.login_view import interfaz_login

# ─── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Clínica Privada Pit Duncan",
    page_icon="🏥",
    layout="wide"
)

# ─── CSS Global ────────────────────────────────────────────────────────────────
try:
    with open("src/static/css/styles.css", "r", encoding="utf-8") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

if 'vista_actual' not in st.session_state:
    st.session_state['vista_actual'] = 'menu_principal'

params = st.query_params
if "vista" in params:
    st.session_state['vista_actual'] = params["vista"]
    st.query_params.clear()
    st.rerun()


# Estos botones están ocultos con CSS 
_BTN_LOGIN   = "nav_login"
_BTN_CITA    = "nav_cita"
_BTN_COMPRA  = "nav_compra"

def main():
    # ── Sidebar ────────────────────────────────────────────────────────────────
    try:
        pathlogo = "src/static/img/logo3.png"
        st.sidebar.image(pathlogo, width=180)
    except:
        pass

    st.sidebar.markdown("""
    <div class="sidebar-info">
        <div class="sidebar-info-title">Información</div>
        <div class="sidebar-info-row">
            <div class="sidebar-info-label">Dirección</div>
            <div class="sidebar-info-val">Andador Vikingos 102 El Morro, Boca del Río</div>
        </div>
        <div class="sidebar-info-row">
            <div class="sidebar-info-label">Teléfono</div>
            <div class="sidebar-info-val">222 914 1653</div>
        </div>
        <div class="sidebar-info-row">
            <div class="sidebar-info-label">Soporte</div>
            <a class="sidebar-info-link" href="mailto:clinicaprivadapitduncan@gmail.com">
                clinicaprivadapitduncan@gmail.com
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


    if st.session_state['vista_actual'] == 'menu_principal':

        st.markdown("""
        <div class="main-title">
            Clínica Privada<br><span>Pit Duncan</span>
        </div>
        <div class="main-subtitle">Selecciona una opción para continuar</div>

        <div class="card-grid">
            <a href="?vista=formulario_login" class="action-card" target="_self">
                <div class="card-icon icon-blue">🔐</div>
                <div>
                    <p class="card-title">Login</p>
                    <p class="card-desc">Acceso para médicos y administradores del sistema</p>
                </div>
                <div class="card-arrow">→</div>
            </a>
            <a href="?vista=formulario_cita1" class="action-card" target="_self">
                <div class="card-icon icon-green">📅</div>
                <div>
                    <p class="card-title">Generar Cita</p>
                    <p class="card-desc">Agenda tu consulta con un especialista disponible</p>
                </div>
                <div class="card-arrow">→</div>
            </a>
            <a href="?vista=formulario_compra_medicinas" class="action-card" target="_self">
                <div class="card-icon icon-amber">💊</div>
                <div>
                    <p class="card-title">Comprar Medicina</p>
                    <p class="card-desc">Farmacia en línea con catálogo completo</p>
                </div>
                <div class="card-arrow">→</div>
            </a>
        </div>

        <div class="footer-bar">
            <span class="status-dot"></span>
            Sistema activo — Clínica Privada Pit Duncan © 2025
        </div>
        """, unsafe_allow_html=True)

  
    elif st.session_state['vista_actual'] == 'formulario_cita1':
        cita_aux1 = False
        menu_citas(cita_aux1)
        if st.button("Volver al Menú", key="volver_cita1"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_cita2':
        cita_aux2 = True
        menu_citas(cita_aux2)
        if st.button("Volver al Menú", key="volver_cita2"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_compra_medicinas':
        comprar_medicina()
        if st.button("Volver al Menú", key="volver_compra"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_login':
        interfaz_login()
        if st.button("Volver al Menú", key="volver_login"):
            st.session_state['vista_actual'] = 'menu_principal'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_gusuario':
        menu_user()
        if st.button("Volver al Menú", key="volver_gusuario"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_receta':
        generar_recetita()
        if st.button("Volver al Menú", key="volver_receta"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_ingresar_paciente':
        menu()
        if st.button("Volver al Menú", key="volver_paciente"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'crear_factura':
        generar_factura()
        if st.button("Volver al Menú", key="volver_factura"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_inv1':
        aux1 = True
        menu_inv(aux1)
        if st.button("Volver al Menú", key="volver_inv1"):
            st.session_state['vista_actual'] = 'menu_admin'
            st.rerun()

    elif st.session_state['vista_actual'] == 'formulario_inv2':
        aux2 = False
        menu_inv(aux2)
        if st.button("Volver al Menú", key="volver_inv2"):
            st.session_state['vista_actual'] = 'menu_medicos'
            st.rerun()

    # ── Menú Admin ─────────────────────────────────────────────────────────────
    elif st.session_state['vista_actual'] == 'menu_admin':

        st.markdown("""
        <div class="admin-title">Menú de <span style="color:#4a9eff">Administrador</span></div>
        <div class="admin-subtitle">Selecciona una opción para continuar</div>

        <div class="admin-card-grid">
            <a href="?vista=formulario_gusuario" class="admin-card" target="_self">
                <p class="admin-card-title">Usuarios</p>
                <p class="admin-card-desc">Gestión de cuentas de médicos y administradores</p>
                <div class="admin-card-arrow">→</div>
            </a>
            <a href="?vista=formulario_inv1" class="admin-card" target="_self">
                <p class="admin-card-title">Inventario</p>
                <p class="admin-card-desc">Consulta y administración del stock de la clínica</p>
                <div class="admin-card-arrow">→</div>
            </a>
        </div>

        <div class="volver-wrapper">
            <a href="?vista=menu_principal" class="volver-btn" target="_self">← Cerrar sesión</a>
        </div>
        """, unsafe_allow_html=True)

    # ── Menú Médicos ───────────────────────────────────────────────────────────
    elif st.session_state['vista_actual'] == 'menu_medicos':
       st.markdown("""
        <div class="medicos-title">Menú de <span style="color:#4a9eff">Médicos</span></div>
        <div class="medicos-subtitle">Selecciona una opción para continuar</div>

        <div class="medicos-card-grid">
            <a href="?vista=formulario_receta" class="medico-card" target="_self">
                <p class="medico-card-title">Prescribir Receta</p>
                <p class="medico-card-desc">Genera y registra recetas médicas para pacientes</p>
                <div class="medico-card-arrow">→</div>
            </a>
            <a href="?vista=formulario_ingresar_paciente" class="medico-card" target="_self">
                <p class="medico-card-title">Pacientes</p>
                <p class="medico-card-desc">Consulta y gestión del registro de pacientes</p>
                <div class="medico-card-arrow">→</div>
            </a>
            <a href="?vista=crear_factura" class="medico-card" target="_self">
                <p class="medico-card-title">Generar Factura</p>
                <p class="medico-card-desc">Emite facturas para consultas y servicios médicos</p>
                <div class="medico-card-arrow">→</div>
            </a>
            <a href="?vista=formulario_inv2" class="medico-card" target="_self">
                <p class="medico-card-title">Inventario</p>
                <p class="medico-card-desc">Consulta el stock y certificaciones de la clínica</p>
                <div class="medico-card-arrow">→</div>
            </a>
            <a href="?vista=formulario_cita2" class="medico-card" target="_self">
                <p class="medico-card-title">Citas</p>
                <p class="medico-card-desc">Visualiza y administra las citas programadas</p>
                <div class="medico-card-arrow">→</div>
            </a>
        </div>

        <div class="volver-wrapper">
            <a href="?vista=menu_principal" class="volver-btn" target="_self">← Cerrar sesión</a>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()