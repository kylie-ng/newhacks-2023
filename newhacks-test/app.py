import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename #for secure user input
#from PyPDF2 import PdfReader 
ALLOWED_EXTENSIONS = {'pdf'} #limit the input of the extensions to PDF only

app = Flask(__name__) #create a Flask instance
UPLOAD_FOLDER = '/uploads'
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER #linked to the variable above to store uploaded PDFs

#simple function to check if the filename is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#def pdf_reader():
 #   reader = PdfReader(file)
  #  for page in reader.pages:
   #     text = page.extract_text()
    #    print(text)

@app.route('/input.html', methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('/input.html')

@app.route('/output.html', methods=['GET', 'POST']) 
def output():    
    if request.method == 'GET':
        return render_template('/output.html')

@app.route('/', methods=['GET', 'POST']) #get method is for getting onto the page, post is for uploading the file
def index():    
    if request.method == 'GET':
        return render_template('/index.html')
    if request.method == 'POST': #if the user decides to upload a file
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect('some.url')
        file = request.files['file']
        # If the user does not select a file, the browser submits an error
        if file.filename == '':
            return redirect('some.url')
        #If user input is valid
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename) #generate a secure file name
            file.save(os.path.join(app.config['/uploads'], filename)) #save the file to uploads
            #pdf_reader()
            #process_file(os.path.join(app.config['/uploads'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))

