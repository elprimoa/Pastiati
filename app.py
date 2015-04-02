from flask import *
from flask_mail import *
from models.pasties import *
from random import *

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'ppastiati@gmail.com'
MAIL_PASSWORD = 'ati*pastiati'
SECRET_KEY = 'development key'

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
app.config.from_object(__name__)
mail = Mail(app)

@app.route('/')
def index():
  return redirect(url_for('home'))

@app.route('/home')
def home():
  if 'username' in session:
    username = session['username']
    return render_template('home.html', username = username)
  return render_template('home.html')

@app.route('/about')
def about():
  if 'username' in session:
    username = session['username']
    return render_template('about.html', username = username)
  return render_template('about.html')

@app.route('/contact')
def contact():
  if 'username' in session:
    username = session['username']
    return render_template('contact.html', username = username)
  return render_template('contact.html')

@app.route('/register')
def register():
  if 'username' in session:
    username = session['username']
    return render_template('register.html', username = username)
  return render_template('register.html')

@app.route('/doregister', methods = ['POST'])
def doregister():
  username = request.form['username']
  fullname = request.form['fullname']
  email = request.form['email']
  password = request.form['password']
  session['username'] = username
  return redirect(url_for('home'))

@app.route('/create')
def create():
  if 'username' in session:
    username = session['username']
    return render_template('create.html', username = username)
  return render_template('create.html')

@app.route('/login', methods = ['POST'])
def login():
  email = request.form['email']
  password = request.form['pass']
  session['username'] = "ElPrimoA"
  return "ElPrimoA"

@app.route('/logout', methods = ['POST'])
def logout():
  session.pop('username', None)
  return ""

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


