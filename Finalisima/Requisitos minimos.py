
# coding: utf-8

# In[19]:


import sqlite3
import datetime

def nuevo_usuario(nombre,contrasena):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()
    
    cursor.execute("""SELECT MAX (U.id) FROM Usuarios U""")
    maximo_id = cursor.fetchone()[0]
    maximo_id = maximo_id + 1
    aux = (maximo_id, nombre, contrasena)
    try:
        cursor.execute("""INSERT INTO Usuarios(id, nombre, contrasena) VALUES(?,?,?)""",aux)
    except:
        archivo.commit()
        archivo.close()   
        return "Nombre de usuario '{}' ya existente. Intente con otro nombre, su señoría".format(nombre)
    
    archivo.commit()
    archivo.close()
    
    return "Fue creado existosamente el usuario {}".format(nombre)


# In[35]:


nuevo_usuario("negropinera","elpapurri")


# In[56]:


def ingresar_al_sistema(nombre,contrasena):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()
    aux=(nombre,)
    cursor.execute("""SELECT U.contrasena FROM Usuarios U WHERE U.nombre=?""",aux)
    
    pseudoclave = cursor.fetchone()
    
    if pseudoclave:
        if pseudoclave[0] == contrasena:
            print("Ingreso exitoso, disfruta tu muzic")
            archivo.commit()
            archivo.close()
            
            return True
        
        else:
            print("Clave incorrecta, avíspate")
            archivo.commit()
            archivo.close()
            
            return False
        
    else:
        print("No existe este usuario, sorry loquill@")
        archivo.commit()
        archivo.close()
        
        return False


# In[59]:


ingresar_al_sistema("negropinera","lala")


# In[1]:


def agregar_nueva_cancion(artista, album, cancion, duracion):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()
    cursor.execute("""SELECT MAX (C.id) FROM Canciones C""")
    
    maximo_id = cursor.fetchone()[0]
    maximo_id = maximo_id + 1    
    aux = (maximo_id, artista, album, cancion, duracion)
    
    try:
        cursor.execute("""INSERT INTO Canciones(id, artista, album, cancion, duracion) VALUES(?,?,?,?,?)""",aux)
        
        return "Canción creada exitosamente baby"
        
    except:
        archivo.commit()
        archivo.close()   
        return None


# In[18]:


def id_usuario(nombre):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()
    aux=(nombre,)
    
    cursor.execute("SELECT U.id FROM Usuarios U WHERE U.nombre =?",aux)
    
    ret = cursor.fetchone()[0]   
    archivo.commit()
    archivo.close()
    
    return ret


# In[34]:


def escuchar(cancion, artista, ide):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()    
    
    cursor.execute("""SELECT MAX (E.id) FROM Escuchadas E""")
    maximo_id = cursor.fetchone()[0]
    maximo_id = maximo_id + 1
    aux=(cancion,artista)
    
    cursor.execute("SELECT C.id FROM Canciones C WHERE C.cancion = ? AND C.artista = ?",aux)
    id_cancion=cursor.fetchone()[0]
    fecha=datetime.datetime.now()
    fecha=str(fecha)
    fecha=fecha[:16]
    
    aux = (maximo_id, ide, id_cancion, fecha)
    
    try:
        cursor.execute("""INSERT INTO Escuchadas(id, id_usuario, id_cancion, fecha) VALUES(?,?,?,?)""",aux)
        archivo.commit()
        archivo.close()
        
        return "Canción añadida exitosamente"
        
    except:
        
        archivo.commit()
        archivo.close() 
        
        return "No se ha podido agragar la cancion, intenta otra"


# In[35]:


escuchar("Havana","Camila Cabello",5)

