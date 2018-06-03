import csv
import random

#para la tabla de usuarios en el sistema

with open('usuarios.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
    quotechar='|',quoting=csv.QUOTE_NONE)
    spamwriter.writerow(["id","Nombre", "Contrasena"])
    spamwriter.writerow([1,"pancho_bacan", "hongkong"])
    spamwriter.writerow([2,"andy96", "toddy"])
    spamwriter.writerow([3,"jack_sparrow", "tortuga"])
    spamwriter.writerow([4,"michael_bolton", "lonelisland"])
    spamwriter.writerow([5,"el_cufifa", "unmanjar"])
    
csvfile.close()

#para la tabla de canciones escuchadas por cada usuario

with open('escuchadas.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
    quotechar='|',quoting=csv.QUOTE_NONE)
    spamwriter.writerow(["id","id_usuario", "id_Cancion","Fecha"])
    
    k=1
    for i in range(5):            #i = id del usuario
        for j in range(4):        #necesitamos 4 canciones
            id_cancion = random.randint(1,1700)
            año = random.randint(2016,2018)
            mes = random.randint(11,12)   #no nos interesa cubrir todos los casos
            dia = random.randint(10,28)
            hora = random.randint(10,23)
            minuto= random.randint(10,59)
            spamwriter.writerow([k, i+1, id_cancion, "{0}-{1}-{2} {3}:{4}".format(año, mes, dia, hora, minuto)])
            k = k +1
            #spamwriter.writerow([k, i, id_cancion, "hola"])

csvfile.close()


hola= datetime.datetime(2018,6,4,8)
hola= str(hola)
hola[0:6]
hola


import datetime
hola= datetime.datetime.now()
hola=str(hola)
print(hola[:16])

