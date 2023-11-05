from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader 
import openai
#from dotenv import load_dotenv
import os
import sys
import subprocess
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__) #create a Flask instance
UPLOAD_FOLDER = '/uploads'
app.config[UPLOAD_FOLDER] = '/uploads' #linked to the variable above to store uploaded PDFs

def create_pset(input_pdf, num_mcq, num_long, model):
    
    # by default, num_mcq = 2
    # by default, num_long = 3
    # by default, model = "gpt-3.5-turbo"

    # remove .pdf filename, create output file paths
    input_name = input_pdf[:-4]
    md_out = f"{input_name}_pset.md"
    pdf_out = f"{input_name}_pset.pdf"

    # extract text
    reader = PdfReader(str(input_pdf))
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    # GPT CONFIG
    sys_content = f'''
        You are a problem set writer. Given a set of class notes, compile a problem set based on the relevant content. 
        The output must be in GFM format so it can be easily exported as a PDF file. 
        The conversion will happen through Pandoc, ensure no text overflows.
        Show the problem set at the top, and the solution set at the bottom.
        The problem set must contain {num_mcq} multiple choice questions and {num_long} long answer questions.
        '''
    sys_prompt = [{"role": "system", "content": sys_content}]
    usr_prompt = [{"role": "user", "content": text}]
    openai.api_key = OPEN_AI_API_KEY
    print("Generating problem set ...")
    response = openai.ChatCompletion.create(
        model = str(model),
        messages = sys_prompt + usr_prompt
    )
    print("Problem set generation complete!")

    # PDF conversion and output
    print("Starting PDF conversion ...")
    with open(md_out, "w") as mdfile:
        mdfile.write(response['choices'][0]['message']['content'])
    try:
        subprocess.run(["pandoc", "--from=gfm", "--to=pdf", "-o", pdf_out, md_out], check=True)
        print("PDF conversion complete!")
        print("Success!")
        return pdf_out
    except subprocess.CalledProcessError:
        print("Markdown to PDF conversion failed")
    
    input_pdf = sys.argv[1]

    try:
        num_mcq = int(sys.argv[2])
    except (IndexError, ValueError):
        num_mcq = 2

    try:
        num_long = int(sys.argv[3])
    except (IndexError, ValueError):
        num_long = 3

    try:
        model = sys.argv[4]
    except IndexError:
        model = "gpt-3.5-turbo"

    create_pset(input_pdf, num_mcq, num_long, model)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_reader(file_path):
    reader = PdfReader(file_path)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)


@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('/index.html')
    if request.method == 'POST': 
        if 'file' not in request.files:
            return render_template('index.html')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html')
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename) #generate a secure file name
            file_path = 'static/uploads/' + filename
            file.save('static/uploads/' + filename)
            pdf_reader(file_path)
            return send_file(file_path)
        return render_template('index.html')

#load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


