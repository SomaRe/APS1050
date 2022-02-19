# source = https://pymupdf.readthedocs.io/en/latest/tutorial.html#working-with-pages

import glob, fitz, os
import shutil
 

def pdf_to_images(path,folder): 

    # To get better resolution
    # zoom_x = 2.0  # horizontal zoom
    # zoom_y = 2.0  # vertical zoom
    # mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    all_files = glob.glob(path + "\\*.pdf")
    for filename in all_files:
        new_folder = filename.split('.pdf')[0] + "_images"
        if not (os.path.isdir(new_folder)):
            os.mkdir(new_folder)
            doc = fitz.open(filename) 
            for page in doc: 
                #pix = page.get_pixmap(matrix=mat)  # render page to an higher resolution image
                pix = page.get_pixmap()  
                pix.save(new_folder + "\\page-"+ str(page.number) +".png") 
            shutil.copytree(new_folder,os.getcwd()+'\\static\\files\\'+folder+'\\'+new_folder.split('\\')[-1])

