#!/usr/bin/python
# -*- coding: latin-1 -*-

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def show_rc(file_name):
      # Path to the PDF file on your local filesystem
      pdf_path = f"/home/aymen/SEF/output_file/rc_resume_{file_name}.pdf"
      
      
      with open(pdf_path, "rb") as pdf_file:
            binary_data = pdf_file.read()

    # Display the PDF using the pdf_viewer component
      st.title("RC_RESUME")
      pdf_viewer(input=binary_data, width=700)
      
def show_dc1():
      # Path to the PDF file on your local filesystem
      pdf_path = "/home/aymen/SEF/output_file/DC1_2019.pdf"
      
      
      with open(pdf_path, "rb") as pdf_file:
            binary_data = pdf_file.read()

    # Display the PDF using the pdf_viewer component
      st.title("word Viewer")
      pdf_viewer(input=binary_data, width=700)    


if __name__ == "__main__":
    show_word()