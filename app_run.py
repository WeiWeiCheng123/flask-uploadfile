from flask import *
from flask_sqlalchemy import SQLAlchemy
from dbModel import *
import os

#UPLOAD_FOLDER = 'C:/Users/user/Desktop/weiiii331/uploads'
#ALLOWED_IMAGE_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv'}

app = Flask(__name__)
#app.config["IMAGE_UPLOADS"] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', **locals())

@app.route('/upload', methods=['GET', 'POST'])
def upload():
     if request.method == 'POST':
             file = request.files['inputfile']
             newfile= FileContents(name=file.filename, data=file.read())
             db.session.add(newfile)
             db.session.commit()

             return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
    
    
    class FileContents():
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    data=db.Column(db.LargeBinary)
    def __init__(self
                 , name
                 , data
                ):
        self.name = name
        self.data = data