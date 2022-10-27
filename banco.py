import sqlite3 as bd

from numpy import number


conn = bd.connect('BancoUsers.db')


def insert(id, nome, usuario, email):
      with conn:
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS 
        usuarios(itemId TEXT , nome TEXT, usuario TEXT, email TEXT)""")
        
        
        cursor.execute("INSERT INTO usuarios VALUES ('" + str(id) + "','" + str(nome) + "','" + str(usuario) + "','" + str(email) + "')")
        conn.commit()


def read():
    with conn:
      cursor = conn.cursor()

      cursor.execute("""CREATE TABLE IF NOT EXISTS 
        usuarios(itemId TEXT , nome TEXT, usuario TEXT, email TEXT)""")

      cursor.execute("SELECT * FROM usuarios")
      results = cursor.fetchall()
      conn.commit()
      return results


def delete(data):
    with conn:
      cursor = conn.cursor()

      cursor.execute("""CREATE TABLE IF NOT EXISTS 
          usuarios(itemId TEXT , nome TEXT, usuario TEXT, email TEXT)""")

      cursor.execute("DELETE FROM usuarios WHERE itemId = '" + str(data) + "'")
      conn.commit()


def update(id, nome, usuario, email, idUser):
  with conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        usuarios(itemId TEXT , nome TEXT, usuario TEXT, email TEXT)""")

    cursor.execute("UPDATE usuarios SET itemId = '" + str(id) + "', nome = '" + str(nome) + "', usuario = '" + str(usuario) + "', email = '" + str(email) + "' WHERE itemId='"+str(idUser)+"'")
    conn.commit()