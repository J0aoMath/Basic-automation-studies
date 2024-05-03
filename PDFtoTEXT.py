import PyPDF2
import os

reader = PyPDF2.PdfReader('MinhaPasta/COMPUTAÇÃO EM NUVEM.pdf')
page = reader.pages[23]
open(os.path.join('MinhaPasta','textocompemnuvem.txt'),mode='w').write(page.extract_text())