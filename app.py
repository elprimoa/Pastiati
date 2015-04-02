from flask import *
from flast_mail import Mail
from models.pasties import *

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
mail = Mail(app)

# Routes goes here
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/login', methods = ['POST'])
def pedro():
  email = request.form['Email']
  password = request.form['Password']
  user = User(email = email)
  if user and user.password == password:
    return render_template('say.html')
  return render_template('form.html')

@app.route('/forgot')
def forgot():
  return render_template('forgot.html')

if __name__ == '__main__':
  app.debug = True
  app.run( host = '127.0.0.1', port = 8000 )


