import sqlite3

DATABASE_NAME = "procesed_video.db"

def create_table():
    try:
        conexion=sqlite3.connect(DATABASE_NAME)
        conexion.execute("""create table if not exists videos (
                                codigo integer primary key AUTOINCREMENT,
                                id text,
                                process bool DEFAULT true,
                                create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )""")
        conexion.close()
    except sqlite3.OperationalError:
        print("La tabla articulos ya existe")  

def insert_data(data):
    print(f"Insertando: {data}")
    conexion=sqlite3.connect(DATABASE_NAME)
    conexion.execute("insert into videos(id) values (?)", (data, ))
    conexion.commit()
    conexion.close()

def exist_video(id):
    conexion=sqlite3.connect(DATABASE_NAME)
    cursor=conexion.execute("select * from videos where id=?", (id, ))
    fila=cursor.fetchone()
    conexion.close()
    if fila!=None:
        return True
    else:
        return False