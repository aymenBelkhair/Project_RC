#!/usr/bin/python
# -*- coding: latin-1 -*-

from find_rc import RC
from unzip_tool import uzip
from pdf_trait import pdf
from prompt import inpute
from llm import GenAi
from create_rc_resume import create_pdf
import sys

path_to_zip = sys.argv[1]
print(1)
dir_rc = uzip(path_to_zip)
print(2)
rc_path,nom_fichier=RC(dir_rc)
print(3)
chunks,text,pages = pdf(rc_path)
print(4)
messages,questions_extract,question_pdf,questions_gpt = inpute()
print(5)
answers = GenAi(text,pages,messages,chunks,questions_extract,question_pdf,questions_gpt)

create_pdf(answers,nom_fichier)
