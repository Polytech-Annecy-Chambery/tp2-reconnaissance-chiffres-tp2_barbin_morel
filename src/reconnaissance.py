from image import Image


def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    chiffre = 0
    similitude = 0
    for i in range (0,len(liste_modeles)):
        hauteur_model = liste_modeles[i].H
        hauteur_image = image_localisee.H
        largeur_model = liste_modeles[i].W
        largeur_image = image_localisee.W
        if (hauteur_model!=hauteur_image) and (largeur_model!=largeur_image):
            image_redimensionnee = image_localisee.resize(hauteur_model,largeur_model)
        else :
            image_redimensionnee = image_localisee
        simil = image_redimensionnee.similitude(liste_modeles[i])
        
        if simil > similitude:
            similitude = simil
            chiffre = i
          
    return chiffre
               

