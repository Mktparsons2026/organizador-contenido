import streamlit as st
import os
from PIL import Image
# Librerías preparadas para cuando configures tu API de Google Drive
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

st.set_page_config(page_title="Organizador de Contenido", page_icon="⚙️")

# Título de tu página web
st.title("⚙️ Portal de Organización de Contenido CNC")
st.write("Sube el material de las entregas y convencionales. El sistema los enviará directamente a las carpetas de Drive.")

# Zona para arrastrar y soltar archivos
archivos_subidos = st.file_uploader("Arrastra tus imágenes aquí", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if archivos_subidos:
    st.success(f"Se han cargado {len(archivos_subidos)} imágenes listas para clasificar.")
    
    if 'indice' not in st.session_state:
        st.session_state.indice = 0

    if st.session_state.indice < len(archivos_subidos):
        archivo_actual = archivos_subidos[st.session_state.indice]
        
        st.subheader(f"Clasificando imagen {st.session_state.indice + 1} de {len(archivos_subidos)}")
        
        # Mostramos la imagen
        imagen = Image.open(archivo_actual)
        st.image(imagen, width=500)
        
        st.write("¿A qué categoría pertenece este contenido?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🚜 Maquinaria / Entregas", use_container_width=True):
                # Aquí el sistema conectará con Drive para subir a la carpeta Entregas
                st.info("Conectando con Google Drive... (Requiere configuración de API)")
                st.session_state.indice += 1
                st.rerun()
                
        with col2:
            if st.button("🧑‍🏫 Cursos / Capacitación", use_container_width=True):
                # Aquí el sistema conectará con Drive para subir a la carpeta Cursos
                st.info("Conectando con Google Drive... (Requiere configuración de API)")
                st.session_state.indice += 1
                st.rerun()
                
        with col3:
            if st.button("🗑️ Descartar", type="primary", use_container_width=True):
                st.session_state.indice += 1
                st.rerun()
    else:
        st.balloons()
        st.success("¡Todo listo! Las imágenes han sido procesadas.")
        if st.button("Subir más material"):
            st.session_state.indice = 0
            st.rerun()