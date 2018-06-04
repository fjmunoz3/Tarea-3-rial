
# coding: utf-8

# In[ ]:


import sqlite3, csv, datetime, sys

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



#Creamos las siguientes tablas Artistas y Canciones

cursor.execute("CREATE TABLE IF NOT EXISTS Artistas(id INTEGER, nombre STRING , genero string)")
cursor.execute("""CREATE TABLE IF NOT EXISTS Canciones(id INTEGER, artista STRING ,album  STRING, cancion STRING , 
                duracion INT, UNIQUE(artista,cancion), PRIMARY KEY(id))""")  #FOREIGN KEY(artista) REFERENCES Artistas(nombre))")
A= 5 #SDVOSD

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


archivo.commit()
archivo.close()




#CONSULTAS BÁSICAS

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
    
def eliminar_persona(ide):
    archivo = sqlite3.connect('Base.db')
    cursor = archivo.cursor()    
    aux=(ide,)
    
    cursor.execute('DELETE FROM Usuarios WHERE id=?', ide)

    
#CONSOLA


while True:
    
    print('Hola, bienvenido a Splotify. Qué desea hacer?')
    retorna = False
    while not retorna:
        print('1) Registrarse\n2) Ingresar\n3)Salir')
        inp = input()
        while not inp.isnumeric() or int(inp) not in [1,2,3]:
            print('Accion no valida. Elija otra opcion')
            print('1) Registrarse\n2) Ingresar\n')
            inp = input()
        if inp == '1':
            user = input('Elija un nombre de usuario: ')
            password = input('Elija una contraseña: ')
            retorna = nuevo_usuario(user,password)

        if inp == '2':
            user = input('Ingrese su usuario: ')
            password = input('Ingrese su contraseña: ')
            retorna = ingresar_al_sistema(user,password)
            ide = id_usuario(user)
        if inp == '3':
            sys.exit()
    while retorna:
        print('Que desea hacer? 1) Agregar Musica\n2) Escuchar Musica\n3) Modificar Cancion\n4) Eliminar Usuario\n5) Consultas\n6)Salir')
        inp = input()
        while not inp.isnumeric() or int(inp) not in [1,2,3,4,5,6]:
            print('Accion no valida. Elija otra opcion')
            print('Que desea hacer? 1) Agregar Musica\n2) Escuchar Musica\n3) Modificar Cancion\n4) Eliminar Usuario\n5) Consultas')
            inp = input()
        if inp =='1':
            cancion = input('Ingresa la cancion: ')
            artista = input('Ingresa el artista: ')
            genero = input('Ingresa el genero musical: ')
            album = input('Ingresa el album: ')
            duracion = input('Ingresa la duracion en segundos: ')
            while not duracion.isnumeric():
                print('Ingresa una duracion valida')
                duracion = input('Ingresa la duracion en segundos: ')
            agregar_nueva_cancion(artista,album,cancion,duracion)
        if inp == '2':
            cancion = input('Ingresa la cancion: ')
            artista = input('Ingresa el artista: ')
            escuchar(cancion,artista,ide)

        if inp == '3':
            cancion = input('Que cancion deseas modificar? ')
        if inp == '4':
            nombre = input('ESTAS SEGURO? El cambio será irreversible. Ingresa el nombre a eliminar: ')
        if inp == '6':
            sys.exit()
        if inp == '5':
            print('Que deseas saber? ')
            print('1)Generos mas escuchados\n2)Tiempo invertido\n3)Buscar amiguitos')
            inpu = input()
            while not inpu.isnumeric() or int(inpu) not in [1,2,3]:
                print('Accion no valida. Elija otra opcion')
                print('1)Generos mas escuchados\n2)Tiempo invertido\n3)Buscar amiguitos')
                inpu = input()
            if inpu == '1':
                print('Sitio en construccion. Vuelva pronto.')
            if inpu == '2':
                print('404 : Site not Found')
            if inpu == '3':
                print('No encontramos nada. Estás seguro que tienes amiguitos?')


