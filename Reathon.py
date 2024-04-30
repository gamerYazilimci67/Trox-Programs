#Some parts of this code are in Turkish because it is my language. However, the introductory sentences are in English and will not cause you any trouble.
while True:
    girdi = input("Enter the text. : ")
    print("                  *-*-*-*-*-*-*-*-*-*-*-*-* Reathon *-*-*-*-*-*-*-*-*-*-*-*-*")
    karvesayilari = {}
    toplam_karakter = 0
    
    for karakter in girdi:
        if karakter not in karvesayilari:
            karvesayilari[karakter] = 1
            toplam_karakter += 1
            
        else:
            karvesayilari[karakter] += 1
            toplam_karakter += 1
    
    print("                                   Karakterler | Sayıları: ")
    for karakter, sayi in karvesayilari.items():
        print(f"                                         {karakter}     |    {sayi}")
    
    print(f"                                  Toplam karakter sayısı: {toplam_karakter}")

    print("                  *-*-*-*-*-*-*-*-*-*-*-*-* Reathon *-*-*-*-*-*-*-*-*-*-*-*-*")
