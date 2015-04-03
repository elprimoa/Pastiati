import psycopg2

class User:
  def __init__(self, email = None, username = None):
    if email:
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('SELECT email, password, username, fullname from usuario where email = %s', (email,))
      result = query.fetchone()
      if result:
        self.email = result[0]
        self.password = result[1]
        self.username = result[2]
        self.fullname = result[3]
      else:
        self.email = None
        self.password = None
        self.username = None
        self.fullname = None
      query.close()
      connection.close()
    if username:
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('SELECT email, password, username, fullname from usuario where username = %s', (username,))
      result = query.fetchone()
      if result:
        self.email = result[0]
        self.password = result[1]
        self.username = result[2]
        self.fullname = result[3]
      else:
        self.email = None
        self.password = None
        self.username = None
        self.fullname = None
      query.close()
      connection.close()
  def save(self, create = None, update = None, password = None):
    if create: 
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('INSERT INTO usuario (username, fullname, password, email) VALUES (%s, %s, %s, %s)', (self.username, self.fullname, self.password, self.email,))
      connection.commit()
      query.close()
      connection.close()
    if(update):
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('UPDATE usuario SET fullname = %s, email = %s WHERE username = %s', (self.fullname, self.email, self.username,))
      connection.commit()
      query.close()
      connection.close()
    if(password):
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('UPDATE usuario SET password = %s WHERE username = %s', (self.password, self.username,))
      connection.commit()
      query.close()
      connection.close()


class Pastie:
  def __init__(self, pid = None):
    if pid:
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('SELECT title, content, owner, private, created_at, updated_at from pastie where id = %s', (pid,))
      result = query.fetchone()
      if result:
        self.id = pid
        self.title = result[0]
        self.content = result[1]
        self.owner = result[2]
        self.private = result[3]
        self.created_at = result[4]
        self.updated_at = result[5]
      else:
        self.id = None
        self.title = None
        self.content = None
        self.owner = None
        self.private = None
        self.created_at = None
        self.updated_at = None
      query.close()
      connection.close()
  def save(self, create = None):
    if create:
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('INSERT INTO pastie (title, content, owner, private, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)', (self.title, self.content, self.owner, self.private, self.created_at, self.updated_at,))
      connection.commit()
      query.close()
      connection.close()