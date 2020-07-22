# ch : char 
# return : bool
# permet de savori si un char est un voyelle
def isVowel(ch):
  if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u' or ch=='Y' or ch=='y'):
    return(True)
  else:
    return(False)

# x : int
#return : int
#transforme un decimal en binaire
def dec_to_bin(x):
    return int(bin(x)[2:])