from clean_text import pdf_to_text
from package_installer import package_installer
from engine import main_engine

main_path = r"C:\Users\shiva\Desktop\UofT\Term1-Winter22\APS1050"
folders_name = "session"


# Installs necessary packages
def install_packages():
    requirements = {'flask','PyMuPDF'}
    package_installer(requirements)

# lot of stuuf, Converts all ppt's to pdf's, imports necessary files to static folder, etc
def Engine():
    return main_engine(main_path,folders_name)

def pdf2text(session,pdf):
    return pdf_to_text(session,pdf) 

