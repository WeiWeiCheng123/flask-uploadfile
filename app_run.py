from flask import *
from flask_sqlalchemy import SQLAlchemy
from dbModel import *
import os


app = Flask(__name__)

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
    
    
