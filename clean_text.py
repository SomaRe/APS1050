import fitz  # pymupdf
import re
import os


def clean_text(text):
    ls = text.splitlines()
    ls = [i for i in ls if i]
    new_text = ' '.join(ls)
    new_text = new_text.strip()
    return new_text

def pdf_to_text(session,pdf):
    regex = "[s|S]lide[\s][\d]+"
    text = ""
    error = "[Error]Check File Names in static folder in web_app usually occures when name of guide file is slighly different from ppt name"
    for pd in os.listdir(os.getcwd()+"\\static\\files\\"+session+"\\guides"):
        if (pdf.lower() in pd.lower()):
            file = "static\\files\\"+session+"\\guides\\"+pd
            with fitz.open(file) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

            
            slides_text_list = re.split(regex,text)
            for slides in range(len(slides_text_list)):
                slides_text_list[slides] = clean_text(slides_text_list[slides])


            split_lastslide = slides_text_list[-1].split()
            for i in range(len(split_lastslide)):
                if(re.search("…+",split_lastslide[i])):
                    slides_text_list[-1] = ' '.join(split_lastslide[:i])
                    slides_text_list.append(' '.join(split_lastslide[i:]))

            return list(filter(None,slides_text_list))
        
    return error


