
# coding: utf-8

# In[84]:


def no_puedo_usar_sql(csv):
    a = open(csv,'r',encoding = 'utf8')
    pistas = a.read()
    pistas2 = pistas.split('\n')
    pistas3 = []
    for track in pistas2:
        #'Artist,Album,Track,Duration'
        aux = track.split(',')
        if len(aux) == 1 or aux[0] == 'Artist'or aux[0] == 'id':
            pass
        else:
            pistas3.append(aux)
    return pistas3
def generos_populares(limite):
    dict = {}
    genres = no_puedo_usar_sql('genres.csv')
    tracks = no_puedo_usar_sql('tracks.csv')
    escuchadas = no_puedo_usar_sql('escuchadas.csv')
    usuarios = no_puedo_usar_sql('usuarios.csv')
    lista_generos_all = []                      #LISTA 4
    for artista in genres:
        if artista[1] not in lista_generos_all:
            lista_generos_all.append(artista[1])
    
    for usuario in usuarios:
        lista_0 = []
        lista_ids_canciones_escuchadas = []     ##LISTA 1
        for cancion in escuchadas:
            if cancion[1] == usuario[0]:               #si id usuario que escucha cancion es igual a id usuario
               # print((cancion[1],usuario[0]))
                lista_ids_canciones_escuchadas.append(cancion[2])  #agrego id cancion
        lista_2 = []
        print(lista_ids_canciones_escuchadas)
        for cancion in lista_ids_canciones_escuchadas:  #para cada id
            #print(cancion)
            lista_2.append(tracks[int(cancion)])         ###LISTA 2222 @@@@@@
            
            '''for artista in genres:                         #para cada (artista,genero)
               # print(artista[0])
                if artista[0] == tracks[int(cancion[0])]:    #si nombre artista es igual a
                    print(artista[0],cancion[0])
                    lista_2.append(artista[1])      ###lista 2 y 3'''
        lista_3 = []
        for cancion in lista_2:
            for genero in genres:
                if cancion[0] == genero[0]:
                    lista_3.append(genero[1])
        
            
        #print(lista_2)
        for genero in lista_generos_all:
            a = lista_3.count(genero)
            if a > limite:
                lista_0.append((genero,a))
        
        if lista_0:
            dict[usuario[1]] = lista_0
            
    
    return dict
def tiempo_gastado(minutos):
    lista_3 = []
    genres = no_puedo_usar_sql('genres.csv')
    tracks = no_puedo_usar_sql('tracks.csv')
    escuchadas = no_puedo_usar_sql('escuchadas.csv')
    usuarios = no_puedo_usar_sql('usuarios.csv')
    
    for usuario in usuarios:
        lista_0 = []
        lista_1 = [x for x in escuchadas if x[1] == usuario[0]] #canciones escuchadas([id,usuario,cancion,fecha])
        #print(lista_1)
        lista_2 = []    ### duraciones en segundos
        for cancion in lista_1:
            lista_2.append(tracks[int(cancion[2])])
        #print(lista_2)
        for cancion in lista_2:
            aux = cancion[3].split(':')
            lista_0.append(60*int(aux[0])+int(aux[1]))
        if sum(lista_0) > int(minutos)*60:
            lista_3.append(usuario[1])
        #  for cancion in lista_1:
 #       for cancion2 in tracks:
#            if cancion[]
    
    
    return lista_3


# In[91]:


tiempo_gastado(15)
#generos_populares(2)


# In[54]:


generos_populares(0)


# In[39]:


escuchadas

