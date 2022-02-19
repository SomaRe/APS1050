from flask import Flask, render_template, url_for
import os
import pythoncom
from settings import install_packages, Engine, pdf2text
    
app = Flask(__name__)


@app.route("/")
def index():
    pythoncom.CoInitialize()
    install_packages()
    _,folders_names,ppts_path,ppts_names = Engine()
    return render_template('choose.html', folders_names=folders_names,ppts_path=ppts_path,ppts_names=ppts_names)

@app.route("/app/<session>/<pdf>")
def main(session,pdf):
    vids = [vid for vid in os.listdir(os.path.join(os.getcwd(),'static\\files',session)) if vid.endswith('.mp4')]
    array = pdf2text(session,pdf)
    if('[Error]' in array):
        return array
    array = "-x0x-".join(array)
    return render_template('main.html',pdf = pdf,session=session, vids = vids, array = array)

if __name__ == "__main__":
    app.run(debug=True)