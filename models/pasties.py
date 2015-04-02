import psycopg2

class User:
  def __init__(self, email = None):
    if email:
      connection = psycopg2.connect('dbname=ati_database user=ati password=ati host=127.0.0.1')
      query = connection.cursor()
      query.execute('select email, password from users where email=%s', (email,))
      result = query.fetchone()
      if result:
        self.email = result[0]
        self.password = result[1]
      else:
        self.email = None
        self.password = None
      query.close()
      connection.close()
    
