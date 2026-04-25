import streamlit as st
from interfaces_menu_admin import menu_user
from interfaces_menu_doc import generar_recetita, generar_factura, menu
from interfaces_menu_inv import menu_inv, comprar_medicina
from interfaz_citas import menu_citas
from interfaz_login import interfaz_login

# ─── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Clínica Privada Pit Duncan",
    page_icon="🏥",
    layout="wide"
)

# ─── CSS Global ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

/* Fondo general de la app */
.stApp {
    background-color: #0a0e14;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0d1117 !important;
    border-right: 1px solid #1e2530;
}
section[data-testid="stSidebar"] * {
    color: #a0aec0 !important;
}

/* Ocultar botones Streamlit fantasma (usados solo para navegación) */
div[data-testid="stButton"].nav-hidden > button {
    display: none !important;
}

/* Tarjetas de acción del menú principal */
.card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 32px;
}
.action-card {
    background: #111720;
    border: 0.5px solid #1e2a3a;
    border-radius: 16px;
    padding: 28px 22px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s, transform 0.15s;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
}
.action-card:hover {
    background: #141c28;
    border-color: #2a3f5f;
    transform: translateY(-3px);
}
.card-icon {
    width: 52px;
    height: 52px;
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
}
.icon-blue  { background: rgba(74,158,255,0.12); }
.icon-green { background: rgba(32,201,151,0.12); }
.icon-amber { background: rgba(251,191,36,0.12); }

.card-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 17px;
    font-weight: 500;
    color: #e2e8f0;
    margin: 0;
}
.card-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: #4a5568;
    margin: 0;
    line-height: 1.5;
}
.card-arrow {
    font-size: 20px;
    color: #2a3f5f;
    margin-top: 6px;
    transition: color 0.2s;
}
.action-card:hover .card-arrow { color: #4a9eff; }

/* Título principal */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 700;
    color: #f0f4ff;
    line-height: 1.15;
    margin: 0;
}
.main-title span { color: #4a9eff; }
.main-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #4a5568;
    margin-top: 8px;
}

/* Footer */
.footer-bar {
    margin-top: 40px;
    padding-top: 16px;
    border-top: 0.5px solid #1e2530;
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: #2a3f5f;
    display: flex;
    align-items: center;
    gap: 8px;
}
.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #20c997;
    display: inline-block;
}

/* Sidebar info card */
.sidebar-info {
    background: #111720;
    border: 0.5px solid #1e2a3a;
    border-radius: 10px;
    padding: 16px;
    font-family: 'DM Sans', sans-serif;
}
.sidebar-info-title {
    font-size: 11px;
    font-weight: 500;
    color: #4a9eff !important;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.sidebar-info-row { margin-bottom: 10px; }
.sidebar-info-label {
    font-size: 10px;
    color: #4a5568 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.sidebar-info-val {
    font-size: 12px;
    color: #a0aec0 !important;
    line-height: 1.4;
}
.sidebar-info-link {
    font-size: 12px;
    color: #4a9eff !important;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


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
        pathlogo = r"C:\Users\Laura\OneDrive\Documentos\Base de datos avanzadas\ProyectoFinal_Local\logo3.png"
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
    <style>
    .admin-title {
        font-family: 'Playfair Display', serif;
        font-size: 38px;
        font-weight: 700;
        color: #f0f4ff;
        line-height: 1.15;
        margin: 0 0 8px 0;
    }
    .admin-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 14px;
        color: #4a5568;
        margin-bottom: 36px;
    }
    .admin-card-grid {
        display: grid;
        grid-template-columns: repeat(2, 340px);
        gap: 20px;
        justify-content: center;
        margin-top: 40px;
    }
    .admin-card {
        background: #111720;
        border: 0.5px solid #1e2a3a;
        border-radius: 16px;
        padding: 32px 28px;
        cursor: pointer;
        transition: border-color 0.2s, background 0.2s, transform 0.15s;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .admin-card:hover {
        background: #141c28;
        border-color: #2a3f5f;
        transform: translateY(-3px);
    }
    .admin-card-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 20px;
        font-weight: 500;
        color: #e2e8f0;
        margin: 0;
    }
    .admin-card-desc {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        color: #4a5568;
        margin: 0;
        line-height: 1.5;
    }
    .admin-card-arrow {
        font-size: 20px;
        color: #2a3f5f;
        margin-top: 10px;
        transition: color 0.2s;
    }
    .admin-card:hover .admin-card-arrow { color: #4a9eff; }

    /* Botón volver esquina inferior derecha */
    .volver-wrapper {
        position: fixed;
        bottom: 32px;
        right: 40px;
        z-index: 999;
    }
    .volver-btn {
        font-family: 'DM Sans', sans-serif;
        font-size: 13px;
        color: #4a5568;
        background: #111720;
        border: 0.5px solid #1e2a3a;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
        text-decoration: none;
        transition: color 0.2s, border-color 0.2s;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .volver-btn:hover {
        color: #a0aec0;
        border-color: #2a3f5f;
    }
    </style>

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
    <style>
    .medicos-title {
        font-family: 'Playfair Display', serif;
        font-size: 38px;
        font-weight: 700;
        color: #f0f4ff;
        line-height: 1.15;
        margin: 0 0 8px 0;
    }
    .medicos-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 14px;
        color: #4a5568;
        margin-bottom: 36px;
    }
    .medicos-card-grid {
        display: grid;
        grid-template-columns: repeat(3, 300px);
        gap: 20px;
        justify-content: center;
        margin-top: 40px;
    }
    .medico-card {
        background: #111720;
        border: 0.5px solid #1e2a3a;
        border-radius: 16px;
        padding: 28px 24px;
        cursor: pointer;
        transition: border-color 0.2s, background 0.2s, transform 0.15s;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .medico-card:hover {
        background: #141c28;
        border-color: #2a3f5f;
        transform: translateY(-3px);
    }
    .medico-card-title {
        font-family: 'DM Sans', sans-serif;
        font-size: 17px;
        font-weight: 500;
        color: #e2e8f0;
        margin: 0;
    }
    .medico-card-desc {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        color: #4a5568;
        margin: 0;
        line-height: 1.5;
    }
    .medico-card-arrow {
        font-size: 20px;
        color: #2a3f5f;
        margin-top: 8px;
        transition: color 0.2s;
    }
    .medico-card:hover .medico-card-arrow { color: #4a9eff; }
    </style>

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