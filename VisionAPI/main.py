from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os, io
from wtforms.validators import InputRequired
from google.cloud import vision

app = Flask(__name__)
# Secret Key for File Uploads
app.config['SECRET_KEY'] = 'thispasswordisverystrong'
# Folder for files uploaded to the website
app.config['UPLOAD_FOLDER'] = 'static/files'

class uploadFileForm(FlaskForm):
    file = FileField("File", validators = ([InputRequired()]))
    submit = SubmitField("Upload File")

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])

def home():
    form = uploadFileForm()
    if form.validate_on_submit():
        # grab the submitted file
        file = form.file.data
        # save the submitted file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        # extract text from the image using Google Vision OCR API
        image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],'schedule.jpg')
        with open(image_path, 'rb') as image_file:
            content = image_file.read()
        # credentials for google vision AI api
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
        # create a Google Vision Image object from the image content
        image = vision.Image(content=content)
        # create a Google Vision ImageAnnotatorClient object to access the OCR API
        client = vision.ImageAnnotatorClient()
        # send the image to the OCR API and get the response
        response = client.text_detection(image=image)
        # extract the text annotations from the response
        texts = response.text_annotations
        # get the first text annotation, which contains the extracted text
        extracted_text = texts[0].description
        # return the extracted text
        return extracted_text
    # if the form is not submitted or invalid, render the upload form
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)