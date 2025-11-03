
import streamlit as st
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config.settings import set_llm_api_key
from utils.llm_setup import get_llm
from utils.data_utils import preprocess_and_save

import tempfile
import pandas as pd
from PyPDF2 import PdfReader

# ----------------------------
# Streamlit page setup
# ----------------------------

st.set_page_config(
    page_title="InsightMate",
    page_icon=" 🌐 ",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# UI Layout
# ----------------------------
st.title("🌐 InsightMate")
st.caption("Your AI partner for exploring data, files, and ideas.")

user_input = st.text_input("Your message:", key="user_input_box")


if st.button("Send", key="send_btn") and user_input:
    pass
    st.rerun()

# -----------------------------------
# SIDEBAR - FILE UPLOAD
# -----------------------------------
st.sidebar.header("📂 Upload your files")

uploaded_files = st.sidebar.file_uploader(
    "Upload TXT, PDF, CSV, or Excel files",
    type=[ "csv", "xlsx"]
)

# Create directories if they don't exist
# DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
# files_dir = os.path.join(DATA_DIR, 'files')
# datasets_dir = os.path.join(DATA_DIR, 'datasets')

# os.makedirs(files_dir, exist_ok=True)
# os.makedirs(datasets_dir, exist_ok=True)

temp_dir = tempfile.mkdtemp()
saved_files = []

if uploaded_files:
    st.sidebar.success(f"{len(uploaded_files)} file(s) uploaded!")
    for file in uploaded_files:
        # Save the uploaded file temporarily for processing
        temp_file_path = os.path.join(temp_dir, file.name)
        with open(temp_file_path, "wb") as f:
            f.write(file.read())
        df,df_col,df_html,error= preprocess_and_save(temp_file_path)

        
        # # Determine the appropriate directory based on file type
        # file_ext = os.path.splitext(file.name)[1].lower()
        # if file_ext in ['.txt', '.pdf']:
        #     # Save to files directory
        #     final_file_path = os.path.join(files_dir, file.name)
        # elif file_ext in ['.csv', '.xlsx']:
        #     # Save to datasets directory
        #     final_file_path = os.path.join(datasets_dir, file.name)
        # else:
        #     # Default to files directory for other types
        #     final_file_path = os.path.join(files_dir, file.name)
        
        # # Copy from temp to final location
        # with open(temp_file_path, "rb") as temp_file:
        #     with open(final_file_path, "wb") as final_file:
        #         final_file.write(temp_file.read())
        
        # saved_files.append(temp_file_path)  # Keep temp path for processing

    st.sidebar.write("📁 **Saved locally at:**")
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[1].lower()
        if file_ext in ['.txt', '.pdf']:
            st.sidebar.text(f"files/{file.name}")
        elif file_ext in ['.csv', '.xlsx']:
            st.sidebar.text(f"datasets/{file.name}")
        else:
            st.sidebar.text(f"files/{file.name}")

# # -----------------------------------
# # FILE DELETION SECTION
# # -----------------------------------
# st.sidebar.header("🗑️ Delete Files")

# # List files in files directory
# files_in_files_dir = os.listdir(files_dir) if os.path.exists(files_dir) else []
# files_in_datasets_dir = os.listdir(datasets_dir) if os.path.exists(datasets_dir) else []

# # Combine all files for deletion interface
# all_files = []
# for file in files_in_files_dir:
#     all_files.append(("files", file))
# for file in files_in_datasets_dir:
#     all_files.append(("datasets", file))

# if all_files:
#     selected_files = st.sidebar.multiselect(
#         "Select files to delete:",
#         [f"{folder}/{filename}" for folder, filename in all_files]
#     )
    
#     if st.sidebar.button("Delete Selected Files"):
#         for file_path in selected_files:
#             folder, filename = file_path.split("/", 1)
#             full_path = os.path.join(DATA_DIR, folder, filename)
#             if os.path.exists(full_path):
#                 os.remove(full_path)
#                 st.sidebar.success(f"Deleted: {file_path}")
#         st.rerun()
# else:
#     st.sidebar.info("No files available for deletion.")

