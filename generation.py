import string
import hashlib
from methode import isVowel,dec_to_bin

class Generation:

    def __init__(self, path_animaux):
        #lecture ligne par ligne du fichier dont le path est path_animaux et stockage des données dans self.animaux_list
        self.animaux_list = []
        animaux_file = open(path_animaux, 'r')
        for line in animaux_file:
          self.animaux_list.append(line)
            #self.animaux_list.append(line.encode("iso-8859-1").decode("utf-8"))
            #cette manip permet d'enlever les erreurs d'encodage du fichier mais elle ne fonctionne pas pour moi, mais elle fonctionne pour d'autres
        for i in range(len(self.animaux_list)-1):
          self.animaux_list[i]=self.animaux_list[i][:-1]



        

    # login : string
    # hashpass : string 
    # return : string
    # permet de trouver le mot de passe en fonction du login et du hashpass de quatre manières différentes
    def choix1(self, login, hashpass):
        years = range(1950, 2020, 1)
        alphabet = string.ascii_letters
        print(hashpass)

        # lettre + login + année
        for letter in alphabet:
            for year in years:
                passToTest = letter + login + str(year)
                if str(hashpass).strip() == str(hashlib.md5(passToTest.encode('utf-8')).hexdigest()).strip():
                    print('ok')
                    return passToTest

        # login + 4 chiffres ou 4 chiffres + login 
        for i in range(10):
          for j in range(10):
            for k in range(10):
              for l in range(10):
                temp1=login+str(i)+str(j)+str(k)+str(l)
                temp2=str(i)+str(j)+str(k)+str(l)+login
                if (str(hashpass).strip() == str(hashlib.md5(temp1.encode('utf-8')).hexdigest()).strip()):
                  print('ok')
                  return(temp1)
                if (str(hashpass).strip() == str(hashlib.md5(temp2.encode('utf-8')).hexdigest()).strip()):
                  print('ok')
                  return(temp2)

        # login avec des maj
        for i in range(2**len(login)):
          test=dec_to_bin(i)
          log=login
          indice=0
          while test > 0:
            reste=test%10
            if reste==1:
              timp=log[indice].upper()
              log=log[:indice]+timp+log[indice+1:]
            if (str(hashpass).strip() == str(hashlib.md5(log.encode('utf-8')).hexdigest()).strip()):
              print('ok')
              return(log)
            test=test//10
            indice=indice+1
           
        # login avec majuscule + 4 chiffre
        for i in range(10000):
          log=login.capitalize()
          temp=log+str(i)
          if (str(hashpass).strip() == str(hashlib.md5(temp.encode('utf-8')).hexdigest()).strip()):
             print('ok')
             return(temp)

             
        return 'Non trouvé'


    # hashpass : string
    # return : bool
    # test tous les mots contenus dans self.animaux_list 
    def choix3(self,hashpass):
      for ani in self.animaux_list :      
        if (str(hashpass).strip() == str(hashlib.md5(ani.encode('utf-8')).hexdigest()).strip()):
          print("ok")
          return(ani)
      return("Non trouvé")

    # hashpass : string
    # return : string
    # on teste tous les mots contenus dans self.animaux_list en mettant ou non la première lettre en majuscule et en mettant devant ou derrière un nombre
    # un chiffre allant 0 a 999 
    def choix4(self,hashpass):
      for ani in self.animaux_list:
        for i in range (1000):
          tab=[]
          tab.append(str(i)+ani)
          tab.append(str(i)+ani.capitalize())
          tab.append(ani+str(i))
          tab.append(ani.capitalize()+str(i))
          for tr in tab:
            if (str(hashpass).strip() == str(hashlib.md5(tr.encode('utf-8')).hexdigest()).strip()):
              print('ok')
              return(tr)
      return'Non trouvé'

    # hashpass : string
    # return : string 
    # on remplace toutes les voyelles par un chiffre puis on passe les consones en majuscules pour tout le contenu de self.animaux_list
    def choix5(self,hashpass):

      for ani in self.animaux_list:
        for i in range(10):
          temp=ani.upper()
          for y in range (len(temp)):
            if (isVowel(temp[y])):
              temp=temp[:y]+str(i)+temp[y+1:]
          if (str(hashpass).strip() == str(hashlib.md5(temp.encode('utf-8')).hexdigest()).strip()):
            print("ok")
            return(temp)
      return 'Non trouvé'
    
    # hashpass : string
    # return : string 
    # on met un mot a l'envers et on le dédouble, on fait ça sur tous les mots de self.animaux_list
    def choix6(self,hashpass):
      for ani in self.animaux_list:
        temp=""
        for i in range (len(ani)):
          temp=temp+ani[len(ani)-1-i]
        temp=temp+temp
        if (str(hashpass).strip() == str(hashlib.md5(temp.encode('utf-8')).hexdigest()).strip()):
          print("ok")
          return(temp)
      return' Non trouvé'

    # hashpass : string
    # return : string 
    # on essaie toutes les combinaisons de deux mots contenus dans self.animaux_list
    def choix7(self,hashpass):
      for ani1 in self.animaux_list:
        for ani2 in self.animaux_list:
          temp=ani1+ani2
          if (str(hashpass).strip() == str(hashlib.md5(temp.encode('utf-8')).hexdigest()).strip()):
            print('ok')
            return(temp)
          
      return'Non trouvé'





    