#!/usr/bin/python
# -*- coding: latin-1 -*-

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_pdf(file_name):
      # Path to the PDF file on your local filesystem
      pdf_path = f"/home/aymen/SEF/RC/rc_resume_file/rc_resume_{file_name}.pdf"
      
      
      with open(pdf_path, "rb") as pdf_file:
            binary_data = pdf_file.read()

    # Display the PDF using the pdf_viewer component
      st.title("PDF Viewer")
      pdf_viewer(input=binary_data, width=700)
      
      
