from flask import *
from flask_mail import *
from models.pasties import *
from random import *
from datetime import datetime
import hashlib
import simplejson


MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'ppastiati@gmail.com'
MAIL_PASSWORD = 'ati*pastiati'
SECRET_KEY = 'development key'
ALLOWED_EXTENSIONS = set(['txt'])

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

@app.route('/create')
def create():
  if 'username' in session:
    username = session['username']
    return render_template('create.html', username = username)
  return redirect(url_for('home'))

@app.route('/pastie/<int:pid>')
def pastie(pid):
  p = Pastie(pid = pid)
  if 'username' in session:
    username = session['username']
    if (p.private == 1) and (p.owner != username):
      return render_template('pastie.html', error="No tiene permisos de ver ese pastie")
    return render_template('pastie.html', username = username, p = p)
  if p.private == 1:
    return render_template('pastie.html', error="No tiene permisos de ver ese pastie")
  return render_template('pastie.html', p = p)

@app.route('/modpastie/<int:pid>', methods = ['PUT', 'DELETE'])
def modpastie(pid):
  if request.method == 'PUT':
    p = Pastie(pid = pid)
    p.title = request.form['title']
    p.content = request.form['content']
    private = request.form['private']
    if(private == 'false'):
      p.private = 0
    else:
      p.private = 1
    p.updated_at = datetime.now()
    p.save()
  if request.method == 'DELETE':
    p = Pastie(pid = pid)
    p.delete()
  return ""

@app.route('/pastiemod/<int:pid>')
def pastiemod(pid):
  if 'username' in session:
    username = session['username']
    update = Pastie(pid = pid)
    return render_template('create.html', username = username, update = update)
  return redirect(url_for('home'))

@app.route('/loadown', methods = ['GET'])
def loadown():
  page = request.args['page']
  p = Pasties(username = session['username'], condition = 2, offset = page)
  if len(p.id) == 0:
    abort(404)
  to_json = []
  desired_format = '%Y-%m-%dT%H-%M'
  for i in range(len(p.id)):
    p_dict = {}
    p_dict['id'] = p.id[i]
    p_dict['title'] = p.title[i]
    p_dict['content'] = p.content[i]
    p_dict['owner'] = p.owner[i]
    p_dict['private'] = p.private[i]
    p_dict['created_at'] = p.created_at[i].strftime(desired_format)
    p_dict['updated_at'] = p.updated_at[i].strftime(desired_format)
    to_json.append(p_dict)
  response_data = simplejson.dumps(to_json)
  return response_data

@app.route('/load', methods = ['GET'])
def load():
  page = request.args['page']
  if session.get('username'):
    p = Pasties(username = session['username'], condition = 1, offset = page)
  else:
    p = Pasties(offset = page)
  if len(p.id) == 0:
    abort(404)
  to_json = []
  desired_format = '%Y-%m-%dT%H-%M'
  for i in range(len(p.id)):
    p_dict = {}
    p_dict['id'] = p.id[i]
    p_dict['title'] = p.title[i]
    p_dict['content'] = p.content[i]
    p_dict['owner'] = p.owner[i]
    p_dict['private'] = p.private[i]
    p_dict['created_at'] = p.created_at[i].strftime(desired_format)
    p_dict['updated_at'] = p.updated_at[i].strftime(desired_format)
    to_json.append(p_dict)
  response_data = simplejson.dumps(to_json)
  return response_data

@app.route('/search', methods = ['GET'])
def search():
  page = request.args['page']
  params = request.args['search'].split(" ")
  if session.get('username'):
    query = "SELECT id, title, content, owner, private, created_at, updated_at from pastie where (owner = '" + session['username'] + "' OR private = 0) and ("
    first = True
    for p in params:
      if not first:
        query = query + " OR "
      else:
        first = False
      query = query + "content SIMILAR TO '%" + p + "%'"
    query = query + ") ORDER BY updated_at DESC LIMIT 5 OFFSET " + page
    p = Pasties(username = session['username'], condition = 1, offset = page, search = query)
  else:
    query = "SELECT id, title, content, owner, private, created_at, updated_at from pastie where private = 0 and ("
    first = True
    for p in params:
      if not first:
        query = query + " OR "
      else:
        first = False
      query = query + "content SIMILAR TO '%" + p + "%'"
    query = query + ") ORDER BY updated_at DESC LIMIT 5 OFFSET " + page
    p = Pasties(offset = page, search = query)
  if len(p.id) == 0:
    abort(404)
  to_json = []
  desired_format = '%Y-%m-%dT%H-%M'
  for i in range(len(p.id)):
    p_dict = {}
    p_dict['id'] = p.id[i]
    p_dict['title'] = p.title[i]
    p_dict['content'] = p.content[i]
    p_dict['owner'] = p.owner[i]
    p_dict['private'] = p.private[i]
    p_dict['created_at'] = p.created_at[i].strftime(desired_format)
    p_dict['updated_at'] = p.updated_at[i].strftime(desired_format)
    to_json.append(p_dict)
  response_data = simplejson.dumps(to_json)
  return response_data

@app.route('/domodify', methods = ['POST'])
def domodify():
  u = User(username = session['username'])
  email = request.form['email']
  fullname = request.form['fullname']
  if(email != ""):
    u.email = email
  if(fullname != ""):
    u.fullname = fullname
  ve = User(email = email)
  vu = User(username = username)
  if ve.email:
      print("Email usado")
      return redirect(url_for('modify'))
  else:
    if vu.username:
      print("Usuario usado")
      return redirect(url_for('modify'))
    else:
      u.save(update = True)
      return redirect(url_for('profile'))
  

@app.route('/doregister', methods = ['POST'])
def doregister():
  username = request.form['username']
  fullname = request.form['fullname']
  email = request.form['email']
  password = hashlib.sha224(request.form['password']).hexdigest()
  u = User()
  u.username = username
  u.fullname = fullname
  u.email = email
  u.password = password
  ve = User(email = email)
  vu = User(username = username)
  if ve.email:
      return render_template('register.html', error = "Email existente")
  else:
    if vu.username:
      return render_template('register.html', error = "Username existente")
    else:
      u.save(create = True)
      session['username'] = username
      return redirect(url_for('home'))

@app.route('/dochange', methods = ['POST'])
def dochange():
  password = hashlib.sha224(request.form['password']).hexdigest()
  u = User(username = session['username'])
  u.password = password
  u.save(password = True)
  print password
  return redirect(url_for('profile'))

@app.route('/docreate', methods = ['POST'])
def docreate():
  title = request.form['title']
  content = request.form['content']
  private = 0
  value = request.form.getlist('private')
  if(len(value) > 0):
    private = 1
  owner = session['username']
  created_at = datetime.now()
  updated_at = created_at
  cfile = request.files['file']
  if cfile and allowed_file(cfile.filename):
    content = cfile.read()
  p = Pastie()
  p.title = title
  p.content = content
  p.private = private
  p.owner = owner
  p.created_at = created_at
  p.updated_at = updated_at
  p.save(create = True)
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

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
  app.debug = True
  app.run( host = '127.0.0.1', port = 8000 )


