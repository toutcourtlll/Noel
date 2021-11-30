min = 5
max = 21
number_pass = False
processing = -1
pl = '^'
a = 0      # a est un repert pour créer une boucle d'une durée controlé
 
 
 
 #number_pass est une boucle qui verifie si le nombre choisi correspond aux critères min et max
 
 #lenght est une variable choisie par l'utilisateur qui va correspondre a l'échelle du sapin
while number_pass == False:
    lenght =  input("Choisissez une taille comprise entre " + str(min) + " et " + str(max) + " ")
    if int(lenght) < min:
        print('le nombre choisis est trop petit !')
    elif int(lenght) > max:
        print('le nombre choisis est trop grand !')
    else:
        number_pass = True #passe numbre_true sur false se qui arrete la boucle
 
#pl est le sapin
 
while processing < int(lenght):
min = 5
max = 21
number_pass = False
processing = -1
pl = '^'               # pl est une variable qui va aider a construire les branches

 #number_pass est une boucle qui verifie si le nombre choisi correspond aux critères min et max
 
 #lenght est une variable choisie par l'utilisateur qui va correspondre a l'échelle du sapin
 
while number_pass == False:
    lenght =  input("Choisissez une taille comprise entre " + str(min) + " et " + str(max) + " ")
    if int(lenght) < min:
        print('le nombre choisis est trop petit !')
    elif int(lenght) > max:
        print('le nombre choisis est trop grand !')
    else:
        number_pass = True     #passe numbre_pass sur false se qui arrete la boucle
 
for i in range(int(lenght) + 1):
    pl = ' ' + pl                    #ceci permet au code de mettre les espaces
                                     #tout en haut pour que le sapin soit droit
print(pl)

for i in range(int(lenght) + 1):
 
    pl = pl[1:len(pl)]
    pl += '^^'
    print(pl)
  
 # # # # # # # # # # # # # # # #
 #on passe a la parti du tronc #
 
log = ' '                                #log = tronc
logl = round(int(lenght) / 2, 0)         #logl = largeur du tronc
plenM = len(pl) / 2 + 0.5                #plenM est le centre du sapin
 
 #on calcule ici si logl est pair ou unpair et si est sur pair ajoute 1
if (logl % 2) == 0:
   logl += 1
while len(log) < plenM:
    log = str(log) + ' '
    
boucle = (logl-1)/2

for i in range(int(boucle) + 1):
    log = log[1:len(log)]
    
# on créer ici la taille du tronc
for i in range(int(logl)):
    log = log + 'I'
    
 #la variable hight est la hauteur du tronc
hight = round(len(log.replace('  ','')))/2 + 0.5
#                 ^^^^^^^^^^^^^^^^^^^^
#                 retire tout les espaces necessaire au cadrage du tronc du  calcul

#met le tronc dans la console
for i in range(int(hight) + 1):
    print(log)
