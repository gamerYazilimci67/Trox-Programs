import string
from random import *
#Some parts of this code are in Turkish because it is my language. However, the introductory sentences are in English and will not cause you any trouble.
while(True):
 print("*-*-*-*-*-*-*-*-*-*-*-*-* Arthion *-*-*-*-*-*-*-*-*-*-*-*-*")
 sifre_türü = int(input("""What type of password do you want?: 
  1: Numbers
  2: Letters
  3: Punctuation
  4: Mixed(Numbers, Letters, Punctutaion)
  5: Numbers and Letters
  6: Numbers and Punctuation
  7: Letter Punctuation
  Password Type's Number: """))
  
 sifre_sayisi = int(input("How many passwords do you want?: "))
 sifre_uzunluk = int(input("How many characters long do you want your password to be?: "))


 for _ in range(sifre_sayisi):
  if(sifre_türü == 1):
    karakterler = string.digits
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
  
  elif(sifre_türü == 2):
    karakterler = string.ascii_letters
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
  
  elif(sifre_türü == 3):
    karakterler = string.punctuation
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
  
  elif(sifre_türü == 4):
    karakterler = string.ascii_letters + string.punctuation + string.digits
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
  
  elif(sifre_türü == 5):
    karakterler = string.ascii_letters + string.digits
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
   
  elif(sifre_türü == 6): 
    karakterler = string.digits + string.punctuation
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")
  
  elif(sifre_türü == 7):
    karakterler = string.ascii_letters + string.punctuation
    sifre = "".join(choice(karakterler) for x in range(sifre_uzunluk))
    print(sifre)
    print("-----------------")

   
  else:
    print("Hatalı giriş")
    print("-----------------")
    
    
