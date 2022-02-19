# source = https://github.com/matthewrenze/powerpoint-to-pdf

import os
import shutil
from pathlib import Path
import comtypes.client
import win32com.client
from pdf2images import pdf_to_images


def ppt2pdf(folder_path,file):
    #powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
    powerpoint.Visible = 1
    slides = powerpoint.Presentations.Open(file)
    file_name = os.path.splitext(file)[0]
    slides.SaveAs(os.path.join(folder_path, file_name +".pdf"), 32)
    slides.Close()

def main_engine(main_path,folder_name):
    session_folders_path = []
    folders_names =[]
    presentations_path = []
    ppts_names = []
    for folder in os.listdir(main_path):
        if (os.path.isdir(main_path+"\\"+folder) and (folder_name in folder.lower())):
            if not (os.path.isdir(os.getcwd()+'\\static\\files\\'+folder)):
                os.mkdir(os.getcwd()+'\\static\\files\\'+folder)
            session_folders_path.append(main_path+"\\"+folder)
            folders_names.append(folder)
            for ppt_folder in os.listdir(main_path+"\\"+folder):
                if("guide" in ppt_folder.lower()):
                    if not (os.path.isdir(os.getcwd()+'\\static\\files\\'+folder+"\\guides")):
                        os.mkdir(os.getcwd()+'\\static\\files\\'+folder+"\\guides")
                        for pdf in os.listdir(main_path+"\\"+folder+'\\'+ppt_folder):
                            if(pdf.lower().endswith('.pdf')):
                                shutil.copy(main_path+"\\"+folder+"\\"+ppt_folder+"\\"+pdf,os.getcwd()+'\\static\\files\\'+folder+"\\guides")
                if("present" in ppt_folder.lower()):
                    ppt_names = []
                    pdf_names = []
                    temp_presentations_path = []
                    for ppt in os.listdir(main_path+"\\"+folder+'\\'+ppt_folder):
                        if(ppt.lower().endswith((".ppt", ".pptx"))):
                            ppt_names.append(ppt.split('.p')[0])
                        elif(ppt.lower().endswith((".pdf"))):
                            temp_presentations_path.append(main_path+"\\"+folder+'\\'+ppt_folder+ppt)
                            pdf_names.append(ppt.split(".p")[0])
                    for ppt in os.listdir(main_path+"\\"+folder+'\\'+ppt_folder):
                        if(ppt.lower().endswith((".ppt", ".pptx")) and (ppt.split('.p')[0] not in pdf_names)):
                            ppt2pdf(main_path+"\\"+folder+'\\'+ppt_folder,main_path+"\\"+folder+'\\'+ppt_folder+'\\'+ppt)
                    for pdf in os.listdir(main_path+"\\"+folder+'\\'+ppt_folder):
                        if(pdf.lower().endswith(".pdf") and (pdf.split('.p')[0] not in pdf_names)):
                            if not Path(os.getcwd()+'\\static\\files\\'+folder+'\\'+pdf).exists():
                                shutil.copy(main_path+"\\"+folder+'\\'+ppt_folder+'\\'+pdf,os.getcwd()+'\\static\\files\\'+folder)
                    for vid in os.listdir(main_path+"\\"+folder+'\\'+ppt_folder):
                        if(vid.lower().endswith(".mp4")):
                            if not Path(os.getcwd()+'\\static\\files\\'+folder+'\\'+vid).exists():
                                shutil.copy(main_path+"\\"+folder+'\\'+ppt_folder+'\\'+vid,os.getcwd()+'\\static\\files\\'+folder)
                    presentations_path.append(temp_presentations_path)
                    ppts_names.append(ppt_names)
                    pdf_to_images(main_path+"\\"+folder+'\\'+ppt_folder,folder)

    return session_folders_path, folders_names, presentations_path, ppts_names






