from flask import *
from flask_mail import *
from models.pasties import *
from random import *

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'ppastiati@gmail.com'
MAIL_PASSWORD = 'ati*pastiati'

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
app.config.from_object(__name__)
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

@app.route('/forgotmail', methods = ['POST'])
def forgotmail():
  email = request.form['email']
  msg = Message('Pastiati mail system', sender=("Pastiati", "ppastiati@gmail.com"), recipients = [email])
  genkey = ""
  for i in range(5):
    genkey = genkey + chr(randint(97, 122))
  for i in range(3):
    genkey = genkey + chr(randint(48, 57))
  for i in range(2):
    genkey = genkey + chr(randint(35, 47))
  genkey = ''.join(sample(genkey, len(genkey)))
  msg.body = "Your new password is: %s" % genkey 
  with app.app_context():
    mail.send(msg)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.debug = True
  app.run( host = '127.0.0.1', port = 8000 )


