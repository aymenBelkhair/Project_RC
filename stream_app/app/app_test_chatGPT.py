#!/usr/bin/python
# -*- coding: latin-1 -*-

import streamlit as st
import zipfile
import os
import re
import shutil
from pdf_trait import pdf
from prompt import inpute
from llm_openAi import GenAi
from create_rc_resume import create_pdf
from view_pdf import show_rc,show_dc1
from dc import DC1_file,DC2_file

def find_files_with_exact_rc(directory):
    matches = []
    pattern = re.compile(r'(?<![a-zA-Z])RC(?![a-zA-Z])|(Reglement|r�glement).*consultation([a-zA-z _]*)')  # Regular expression pattern

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if pattern.search(filename) and (filename.lower().endswith('.pdf') or filename.lower().endswith('.doc') or filename.lower().endswith('.docx')):
                matches.append(os.path.join(root, filename))

    return matches

def clear_directory(directory_path):
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # remove the file or link
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # remove the directory and its contents
    except Exception as e:
        print(f"Failed to delete contents of '{directory_path}'. Reason: {e}")

def main():
    st.title("SEF Solution - ChatGpt")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a zip file", type="zip")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        file_name = uploaded_file.name
        with open("temp.zip", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write("File uploaded successfully!")
        extracted_files = "/home/aymen/SEF/extracted_files"
        output_file = "/home/aymen/SEF/output_file"
        # Add a button to unzip the file
        if st.button("Unzip File"):
            status_dir = os.listdir(extracted_files)
            if len(status_dir) != 0:
                clear_directory(extracted_files)
                clear_directory(output_file)
            else :
                print("dir to extrat empty")
            # Unzip the file
            with zipfile.ZipFile("temp.zip", 'r') as zip_ref:
                zip_ref.extractall("extracted_files")
            
            st.write("File unzipped successfully!")

            # Add a button to search for specific files
            
            directory = "/home/aymen/SEF/extracted_files"
            matches = find_files_with_exact_rc(directory)
            
            

            if matches:
                #file_name = matches[0].split("/")[-1].split(".")[0]
                rc_path = matches[0]
                st.write("RC File found:")
                for match in matches:
                    st.write(match)
            else:
                st.write("No RC file founded.")
                
            if (matches[0].endswith('.docx') or matches[0].endswith('.doc') ):
                 os.system(f'abiword --to pdf "{matches[0]}"')
                 #os.system(f'libreoffice --headless --convert-to pdf "{matches[0]}"')
                 rc_path = f"{matches[0].split('.docx')[0]}.pdf"
                 
            print(f"rc path {rc_path}")
            chunks,text,pages = pdf(rc_path)
            print("chunks created")
            messages,questions_extract,question_pdf,questions_gpt = inpute()
            st.write("Start generating answers ...")
            
            joined_answer,dc = GenAi(text,pages,messages,chunks,questions_extract,question_pdf,questions_gpt)
            
            joined_answer = joined_answer.strip()
            
            create_pdf(joined_answer,file_name)
            print("PDF created successfully.")
            st.write("RC_RESUME-PDF-created successfully.")
            show_rc(file_name)
            

            #DC1    
            st.write("DC1 creation ...")
            DC1_file(dc)
            st.write("DC1 a ete bien cree")
            #DC2
            st.write("DC2 creation ...")
            DC2_file(dc)
            st.write("DC2 a ete bien cree")
            os.system(f"cp /home/aymen/SEF/examples_files/constant_file/* {output_file}")
            os.system("cd /home/aymen/SEF/output_file && zip SEF_dossier.zip ./*")
            #download le dossier complet resume
            with open(f"/home/aymen/SEF/output_file/SEF_dossier.zip", "rb") as file:
                  btn = st.download_button(
                      label="SEF_dossier",
                      data=file,
                      file_name=f"SEF_dossier.zip"
                      
                  )
            

if __name__ == "__main__":
    main()
