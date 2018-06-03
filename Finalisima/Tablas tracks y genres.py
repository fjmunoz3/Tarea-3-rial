
# coding: utf-8

# In[15]:


import sqlite3, csv

####CREACIÓN DE BASE

a = open('genres.csv','r',encoding = 'utf8')
b = open('tracks.csv','r',encoding = 'utf8')
generos = a.read()
pistas = b.read()


# In[16]:


generos2 = generos.split('\n')
pistas2 = pistas.split('\n')


# In[17]:


#Ahora extraeremos la información de los archivos csv

generos3 = {}
pistas3 = []
for artist in generos2:
    aux = artist.split(',')
    #print(len(aux), aux)
    if len(aux) == 1 or aux[0] == 'Artist':
        pass
    elif aux[0] in generos3.keys():
        generos3[aux[0]].append(aux[1])
    else:
        generos3[aux[0]] = [aux[1]]

for track in pistas2:
    #'Artist,Album,Track,Duration'
    aux = track.split(',')
    if len(aux) == 1 or aux[0] == 'Artist':
        pass
    else:
        pistas3.append(aux)


# In[18]:


#Creamos la base de datos

archivo = sqlite3.connect('Base.db')
cursor = archivo.cursor()


# In[19]:


#Creamos las siguientes tablas Artistas y Canciones

cursor.execute("CREATE TABLE IF NOT EXISTS Artistas(id INTEGER, nombre STRING , genero string)")
cursor.execute("""CREATE TABLE IF NOT EXISTS Canciones(id INTEGER, artista STRING ,album  STRING, cancion STRING , 
                duracion INT, UNIQUE(artista,cancion), PRIMARY KEY(id))""")  #FOREIGN KEY(artista) REFERENCES Artistas(nombre))")
A= 5 #SDVOSD


# In[20]:


#Poblamos "Artistas" en base a genres.csv

j = 1
for key in generos3.keys():
    for value in generos3[key]:
        aux = (j, key, value)
        cursor.execute("INSERT INTO Artistas VALUES(?,?,?)", aux)
        j = j + 1

#Poblamos "Canciones" en base a tracks.csv       
j = 1
for i in pistas3:
    duracion = i[3].split(":")
    duracion = int(duracion[0])*60 + int(duracion[1])
    aux = (j, i[0], i[1], i[2], duracion)
    cursor.execute("INSERT INTO Canciones VALUES(?,?,?,?,?)", aux)
    j = j + 1


# In[21]:


#Creamos la tabla Usuarios en la base


cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios(id INTEGER, nombre TEXT, contrasena TEXT, 
                PRIMARY KEY(id), UNIQUE(nombre))""")  #????O NOMBRE???


c = open('usuarios.csv','r',encoding="utf-8")

usuarios = c.read()
usuarios2 = usuarios.split('\n')
usuarios3 = []

for usuario in usuarios2:
    aux = usuario.split(',')
    if len(aux) == 1 or aux[0] == 'id':
        pass
    else:
        usuarios3.append(aux)


for i in usuarios3:
    aux = (i[0], i[1], i[2])
    cursor.execute("INSERT INTO Usuarios VALUES(?,?,?)", aux)


#Creamos la tabla Escuchadas en la base


cursor.execute("""CREATE TABLE IF NOT EXISTS Escuchadas(id INTEGER, id_usuario TEXT, id_cancion TEXT, fecha TEXT,
                    PRIMARY KEY(id), FOREIGN KEY(id_usuario) REFERENCES Usuarios, 
                    FOREIGN KEY(id_cancion) REFERENCES Canciones)""")


d = open('escuchadas.csv','r',encoding="utf-8")

escuchadas = d.read()
escuchadas2 = escuchadas.split('\n')
escuchadas3 = []

for escuchada in escuchadas2:
    aux = escuchada.split(',')
    if len(aux) == 1 or aux[0] == 'id':
        pass
    else:
        escuchadas3.append(aux)


for i in escuchadas3:
    aux = (i[0], i[1], i[2], i[3])
    cursor.execute("INSERT INTO Escuchadas VALUES(?,?,?,?)", aux)


# In[22]:


archivo.commit()
archivo.close()


# In[14]:


cursor.execute("DROP TABLE Usuarios")
cursor.execute("DROP TABLE Escuchadas")
cursor.execute("DROP TABLE Artistas")
cursor.execute("DROP TABLE Canciones")


# In[41]:


hola="3:4"
hola= hola.split(":")
hola=int(hola[0])*60 + int(hola[1])
hola

