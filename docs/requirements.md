# Requisitos y Ejecución del Sistema

Para poder desplegar **Clínica Privada Pit Duncan** de forma local, es indispensable contar con las siguientes dependencias de Python instaladas en tu entorno.

## 📦 Librerías Necesarias

A continuación se listan las librerías principales empleadas según su propósito dentro del código:

* **Frontend / UI Web:** 
  * `streamlit`
* **Conexión a Base de Datos (MongoDB):** 
  * `pymongo`
* **Análisis y Extracción de Datos:** 
  * `pandas`
* **Generación de Reportes / PDF:** 
  * `fpdf`
* **Gráficos e Indicadores:** 
  * `matplotlib`
* **Criptografía (Hasheo de credenciales):** 
  * `bcrypt`
* **Ingeniería de Consolas Internas:** 
  * `stdiomask`

> [!TIP]  
> Puedes instalar todas estas librerías de forma masiva en tu entorno gráfico ejecutando:
> ```bash
> pip install streamlit pymongo pandas fpdf matplotlib bcrypt stdiomask
> ```

---

## 🚀 Cómo ejecutar el programa

1. Asegúrate de estar posicionado en la carpeta raíz del proyecto desde tu consola / terminal.
2. Levanta el servidor local de **Streamlit** apuntando al archivo principal (antes llamado `test.py`).

Ejecuta el siguiente comando:
```bash
streamlit run main.py
```
