from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os, io
from wtforms.validators import InputRequired
from google.cloud import vision
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

# init calendar
CLIENT_SECRET_FILE = 'new_client_secret_624935813097-m84odsjv6pc2n5dejcu445d99q8ccutr.apps.googleusercontent.com'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# # new calendar name
# request_body = {
#     'summary': 'UCSC Class Schedule - Quarter'
# }
#
# # create the new aforementioned calendar
# response = service.calendars().insert(body = request_body).execute()
# print(response)
#
# calendar_id_california = '7b5f6e43e367aba0f8bc43c6bcc25808ded09c53b8a1d2b85ae4ab4788d3353e@group.calendar.google.com'
#
# event_request_body_1 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 10, 40),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 11, 45),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
#
#
# event_request_body_2 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 13, 20),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 14, 25),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
#
#
# response2 = service.events().insert(
#     calendarId = calendar_id_california,
#     body = [event_request_body_1, event_request_body_2]
# ).execute()
# pprint(response2)

# event_request_body_3 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 14, 40, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 13, 15, 45, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
#
# event_request_body_4 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 14, 9, 50, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 14, 11, 25, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
#
# event_request_body_5 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 14, 19, 10, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 14, 21, 10, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
#
# event_request_body_6 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 10, 40, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 11, 45, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
# event_request_body_7 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 14, 40, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 15, 45, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
# event_request_body_8 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 16, 00, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 15, 17, 00, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
# event_request_body_9 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 16, 9, 50, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 16, 11, 25, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
# event_request_body_10 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 17, 10, 40, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 17, 11, 45, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }
# event_request_body_11 = {
#     'start': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 17, 14, 40, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'end': {
#         'dateTime': convert_to_RFC_datetime(2023, 11, 17, 15, 45, hour_adjustment - 8),
#         'timeZone': 'America/Los_Angeles'
#     },
#     'summary': 'class_1',
#     'colorId': 5,
#     'visibility': 'private'
# }





















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