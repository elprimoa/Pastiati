from flask import *
from flask_mail import *
from models.pasties import *
from random import *
import hashlib

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

@app.route('/profile')
def profile():
  if 'username' in session:
    u = User(username = session['username'])
    return render_template('profile.html', u = u)
  return redirect(url_for('home'))

@app.route('/change')
def change():
  if 'username' in session:
    username = session['username']
    return render_template('change.html', username = username)
  return redirect(url_for('home'))

@app.route('/modify')
def modify():
  if 'username' in session:
    username = session['username']
    return render_template('modify.html', username = username)
  return redirect(url_for('home'))

@app.route('/domodify', methods = ['POST'])
def domodify():
  u = User(username = session['username'])
  email = request.form['email']
  fullname = request.form['fullname']
  if(email != ""):
    u.email = email
  if(fullname != ""):
    u.fullname = fullname
  u.save(update = True)
  return redirect(url_for('profile'))

@app.route('/doregister', methods = ['POST'])
def doregister():
  username = request.form['username']
  fullname = request.form['fullname']
  email = request.form['email']
  password = hashlib.sha224(request.form['password']).hexdigest()
  session['username'] = username
  u = User()
  u.username = username
  u.fullname = fullname
  u.email = email
  u.password = password
  u.save(create = True)
  return redirect(url_for('home'))

@app.route('/dochange', methods = ['POST'])
def dochange():
  password = hashlib.sha224(request.form['password']).hexdigest()
  u = User(username = session['username'])
  u.password = password
  u.save(password = True)
  print password
  return redirect(url_for('profile'))

@app.route('/create')
def create():
  if 'username' in session:
    username = session['username']
    return render_template('create.html', username = username)
  return redirect(url_for('home'))

@app.route('/login', methods = ['POST'])
def login():
  email = request.form['email']
  password = hashlib.sha224(request.form['pass']).hexdigest()
  u = User(email = email)
  if u.email and u.password == password:
    session['username'] = u.username
    return u.username
  abort(404)

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
  genkey = hashlib.sha224(genkey).hexdigest()
  u = User(email = email)
  u.password(genkey)
  u.save(password = True)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.debug = True
  app.run( host = '127.0.0.1', port = 8000 )


