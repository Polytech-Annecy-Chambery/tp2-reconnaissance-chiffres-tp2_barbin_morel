from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        
        # creation d'une image vide
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        
        for long in range (0,len(self.pixels)):
            for larg in range (0,len(self.pixels[long])):
                if (self.pixels[long][larg]>=S):
                    im_bin.pixels[long][larg]=255
                            
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        ok1=0
        # la variable haut renvoie la ligne à laquelle commence le chiffre
        haut=0
        h1=0
        while ok1==0:
            for i in range (0, self.W):
                if self.pixels[h1][i]==0:
                    haut=h1
                    ok1=1
            h1=h1+1
        
        ok2=0
        # la variable bas renvoie la ligne à laquelle se termine le chiffre
        bas=0
        h2=self.H-1
        while ok2==0:
            for j in range (0, self.W):
                if self.pixels[h2][j]==0:
                    bas=h2
                    ok2=1
            h2=h2-1

        ok3=0
        # la variable gauche renvoie la colone à laquelle commence le chiffre
        gauche=0
        w3=0
        while ok3==0:
            for k in range (0, self.H):
                if self.pixels[k][w3]==0:
                    gauche=w3
                    ok3=1
            w3=w3+1
        
        ok4=0
        # la variable droite renvoie la colone à laquelle se termine le chiffre
        droite=0
        w4=self.W-1
        while ok4==0:
            for l in range (0, self.H):
                if self.pixels[l][w4]==0:
                    droite=w4
                    ok4=1
            w4=w4-1
        
        im_bin2 = Image()
        im_bin2.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        im_bin2.pixels=self.pixels
        im_bin2.pixels=im_bin2.pixels[haut:bas,gauche:droite]
        
        # img_localisee=im_bin2[a:b,c:d]
        return im_bin2
    
        
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        
        img_resize_float = Image()
        img_resize_float.H=new_H
        img_resize_float.W=new_W
        img_resize_float.pixels = resize(self.pixels, (new_H,new_W), 0)
        
        img_resize_int = Image()
        img_resize_int.H=new_H
        img_resize_int.W=new_W
        img_resize_int.pixels = np.uint8(img_resize_float.pixels*255)
        return img_resize_int

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        
        nb_pixels = self.W*self.H
        nb_pixels_pareils=0
        for i in range (0,self.H):
            for j in range (0,self.W):
                if self.pixels[i][j]==im.pixels[i][j]:
                    nb_pixels_pareils = nb_pixels_pareils + 1
        correspondance = nb_pixels_pareils / nb_pixels
        return correspondance
    