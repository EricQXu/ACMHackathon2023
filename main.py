from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

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
        return "File has been uploaded."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)
