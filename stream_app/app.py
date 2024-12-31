import streamlit as st
import zipfile
import os
from unzip_tool import uzip

def main():
    st.title("SEF Solution")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a zip file", type="zip")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp.zip", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write("File uploaded successfully!")

        # Add a button to unzip the file
        if st.button("Unzip File"):
            # Unzip the file
            uzip("temp.zip")
            
            st.write("File unzipped successfully!")

            # List the contents of the unzipped directory
            unzipped_files = os.listdir("extracted_files")
            st.write("Unzipped files:")
            for file in unzipped_files:
                st.write(file)

if __name__ == "__main__":
    main()
