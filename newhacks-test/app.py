import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename #for secure user input
from PyPDF2 import PdfReader 
ALLOWED_EXTENSIONS = {'pdf'} #limit the input of the extensions to PDF only

app = Flask(__name__) #create a Flask instance
UPLOAD_FOLDER = '/uploads'
app.config[UPLOAD_FOLDER] = '/uploads' #linked to the variable above to store uploaded PDFs
#file_path2 = ""

#simple function to check if the filename is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_reader(file_path):
    print(4)
    reader = PdfReader(file_path)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)


@app.route('/input.html', methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('/input.html')
    if request.method == 'POST': #if the user decides to upload a file
        # check if the post request has the file part, or redirect to an error
        if 'file' not in request.files:
            return render_template('/error.html')
        print('1')
        #here, the user has inputted some file, set the file variable as the file input
        file = request.files['file']
        # If the user's file is an empty string, redirect to an error
        if file.filename == '':
            return render_template('/error.html')
        print('2')
        if file and allowed_file(file.filename): 
        #check if user input is a valid file type
            filename = secure_filename(file.filename) #generate a secure file name
            print(filename)
            print(app.config['/uploads'])
            #save the file to uploads
            #print('the file name is ' + file)
            file_path = 'static/uploads/' + filename
            file.save('static/uploads/' + filename)
            print('3')
            #file_path2 = file_path
            #pdf_reader(file_path)
            return redirect(url_for('output', file__path=file_path))
        return render_template('/error.html')

@app.route('/output/<path:file__path>', methods=['GET', 'POST']) 
def output(file__path):
    if request.method == 'GET':
        print(6)
        pdf_reader(file__path)
        print(5)
        return render_template('output.html')

@app.route('/', methods=['GET', 'POST']) #get method is for getting onto the page, post is for uploading the file
def index():    
    if request.method == 'GET':
        return render_template('/index.html')

