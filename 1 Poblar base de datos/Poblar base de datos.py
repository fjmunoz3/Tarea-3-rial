import csv
import random

#para la tabla de usuarios en el sistema

with open('Usuarios.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
    quotechar='|',quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["id","nombre", "contrasena"])
    spamwriter.writerow([1,"pancho_bacan", "hongkong"])
    spamwriter.writerow([2,"andy96", "toddy"])
    spamwriter.writerow([3,"jack_sparrow", "tortuga"])
    spamwriter.writerow([4,"michael_bolton", "lonelisland"])
    spamwriter.writerow([5,"el_cufifa", "unmanjar"])
    
csvfile.close()

#para la tabla de canciones escuchadas por cada usuario

with open('Escuchadas.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
    quotechar='|',quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["id","id_usuario", "id_cancion","fecha"])
    
    for k in range(4*5):
        for i in range(5):            #i = id del usuario
            for j in range(4):        #necesitamos 4 canciones
                id_cancion = random.randint(1,1700)
                año = random.randint(2016,2018)
                mes = random.randint(11,12)   #no nos interesa cubrir todos los casos
                dia = random.randint(10,28)
                hora = random.randint(10,23)
                minuto= random.randint(10,59)
                spamwriter.writerow([k+1, i+1, id_cancion, "{0}-{1}-{2} {3}:{4}".format(año, mes, dia, hora, minuto)])
                #spamwriter.writerow([k, i, id_cancion, "hola"])

csvfile.close()