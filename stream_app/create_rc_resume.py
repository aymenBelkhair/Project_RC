#!/usr/bin/python
# -*- coding: latin-1 -*-

#!/usr/bin/env python
# -*- coding: utf8 -*- 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import streamlit as st
# Register a TTF font to handle Unicode characters
#pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'STORES AND FERMETURES', 0, 1, 'L')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Add the page number in the center
        self.set_x(0)
        self.cell(0, 10, f' {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color( 0 , 179 , 255)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)

    def chapter_body(self, body):
        self.add_font('DejaVu', '', r"/home/aymen/SEF/stream_app/DejaVuSans.ttf", uni=True)
        self.set_font('DejaVu', '', 12)#DejaVu
        self.set_text_color( 0 , 0 , 0)
        self.multi_cell(0, 10, body)
        self.ln()
        

        
        
def create_pdf(joined_answer,file_name):
      # Create instance of FPDF class
      pdf = PDF()
      joined_answer = joined_answer.replace("’"," ")
      joined_answer = joined_answer.replace("‘"," ")
      joined_answer = joined_answer.replace("–","-")
      joined_answer = joined_answer.replace("€"," euro")
      joined_answer = joined_answer.replace("œ"," oe")
      joined_answer = joined_answer.replace("ti","ti")
      
      # Add a page
      pdf.add_page()
      
      # Add long text
      pdf.chapter_title(f"RC_RESUME")
      
      long_text = f"{joined_answer}"
      
      pdf.chapter_body(long_text)
      
      # Save the pdf with name .pdf
      pdf.output(f"/home/aymen/SEF/RC/rc_resume_file/rc_resume_{file_name}.pdf")
      
      print("PDF created successfully.")
      

