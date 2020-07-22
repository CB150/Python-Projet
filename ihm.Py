import tkinter as tk
from generation import Generation


class Application(tk.Frame):

    value_choix=0
    res="Résultat :"

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.Frame1 = tk.Frame()
        self.addLoginMdp(self.Frame1)
        self.Frame1.pack(side="left")

        self.Frame2 = tk.Frame()

        self.addChoix1(self.Frame2)
        self.addChoix3(self.Frame2)
        self.addChoix4(self.Frame2)
        self.addChoix5(self.Frame2)
        self.addChoix6(self.Frame2)
        self.addChoix7(self.Frame2)
        self.startSearch(self.Frame2)
         
        self.show_result= tk.Label(self.Frame2)
        self.show_result["text"]=self.res
        self.show_result.pack()

        self.Frame2.pack()

    # x : int
    # no return 
    # change la valeur de value_choix
    def modify_value_choix(self,x):
        self.value_choix=x

    # choix : int
    # log : string
    # passcrypt : string
    # no return 
    # teste la combinaison avec le choix stocké sur la variable "choix" et l'affiche sur l'interface à droite de résultat
    def appeldegen(self,choix,log,passcrypt):

      
      self.res="Résultat :"
      self.show_result.config(text=self.res)
      
      # Create object Generation with path for animals file
      gen = Generation(path_animaux='dico_animaux.txt.txt')
      if choix==1:
        self.res=self.res+gen.choix1(login=str(log),hashpass=str(passcrypt))
      if choix==3:
        self.res=self.res+gen.choix3(hashpass=str(passcrypt))
      if choix==4:
        self.res=self.res+gen.choix4(hashpass=str(passcrypt))
      if choix==5:
        self.res=self.res+gen.choix5(hashpass=str(passcrypt))
      if choix==6:
        self.res=self.res+gen.choix6(hashpass=str(passcrypt))
      if choix==7:
        self.res=self.res+gen.choix7(hashpass=str(passcrypt))
      self.show_result.config(text=self.res)

    # f : frame
    # no return 
    # ajoute les entrées pour le login et le mot de passe sur l'interface  
    def addLoginMdp(self,f):

        self.log= tk.Label(self)
        self.log["text"]="Login : "
        self.log["justify"]="left"
        self.log.pack(side="left") 
       
        self.log_ent = tk.Entry(self)
        self.log_ent.pack(side="left")

        self.passcryp = tk.Label(self)
        self.passcryp["text"]="Mot de passe crypté : "
        self.passcryp["justify"]="right"
        self.passcryp.pack(side="left")

        self.passcryp_ent = tk.Entry(self)
        self.passcryp_ent.pack(side="left")

    # f : frame
    # no return 
    # ajoute le bouton choix1
    def addChoix1(self,f):

        self.bouton1 = tk.Radiobutton(f)
        self.bouton1["text"]="Lettre + nom avec ou sans capitale + année"
        self.bouton1["variable"]=self.value_choix
        self.bouton1["value"]=1
        self.bouton1["command"]=lambda: self.modify_value_choix(1)
        self.bouton1.pack()

    # f : frame
    # no return 
    # ajoute le bouton choix3
    def addChoix3(self,f):
      
      self.bouton3 = tk.Radiobutton(f)
      self.bouton3["text"] = "choix classqiue"
      self.bouton3["variable"] = self.value_choix
      self.bouton3["value"] = 3
      self.bouton3["command"] = lambda: self.modify_value_choix(3)
      self.bouton3.pack()

    # f : frame
    # no return 
    # ajoute le bouton choix4
    def addChoix4(self,f):

      self.bouton4 = tk.Radiobutton(f)
      self.bouton4["text"] = "ajouté nombre devant ou derrière et mis la première letttre en majuscule ou pas"
      self.bouton4["variable"] = self.value_choix
      self.bouton4["value"] = 4
      self.bouton4["command"] = lambda: self.modify_value_choix(4)
      self.bouton4.pack()

    # f : frame
    # no return 
    # ajoute le bouton choix5
    def addChoix5(self,f):

      self.bouton5 = tk.Radiobutton(f)
      self.bouton5["text"] = "on change les voyelles par un nombre mit le reste en majuscule"
      self.bouton5["variable"] = self.value_choix
      self.bouton5["value"] = 5
      self.bouton5["command"] = lambda: self.modify_value_choix(5)
      self.bouton5.pack()

    # f : frame
    # no return 
    # ajoute le bouton choix6
    def addChoix6(self,f):

      self.bouton6 = tk.Radiobutton(f)
      self.bouton6["text"] = "prendre un nom d'animal le mettre a l'enver et le déboublé"
      self.bouton6["variable"] = self.value_choix
      self.bouton6["value"] = 6
      self.bouton6["command"] = lambda: self.modify_value_choix(6)
      self.bouton6.pack()

    # f : frame
    # no return 
    # ajoute le bouton choix7
    def addChoix7(self,f):

      self.bouton7 = tk.Radiobutton(f)
      self.bouton7["text"] = "concaténé deux nom d'animaux"
      self.bouton7["variable"] = self.value_choix
      self.bouton7["value"] = 7
      self.bouton7["command"] = lambda: self.modify_value_choix(7)
      self.bouton7.pack()

    # f : frame
    # no return 
    # ajoute le bouton Lancer la recherche
    def startSearch(self,f):

      self.search = tk.Button(f)
      self.search["text"] = "Lancer la recherche "
      self.search["command"] = lambda: self.appeldegen(self.value_choix,self.log_ent.get(),self.passcryp_ent.get())
      self.search.pack()