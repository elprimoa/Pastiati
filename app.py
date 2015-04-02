from flask import *
from models.pasties import *

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')

# Routes goes here
@app.route('/')
def index():
  return 'Hello Flask'

@app.route('/sayhello')
def sayhello():
  name = request.args.get('name')
  return render_template('say.html', name = name)

@app.route('/form')
def form():
  return render_template('form.html')

@app.route('/login', methods = ['POST'])
def pedro():
  email = request.form['Email']
  password = request.form['Password']
  user = User(email = email)
  if user and user.password == password:
    return render_template('say.html')
  return render_template('form.html')

if __name__ == '__main__':
  app.debug = True
  app.run( host = '127.0.0.1', port = 8000 )


