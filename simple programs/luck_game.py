import random

random_secret_int = (random.randint(1, 5))

print(" ")

user_int = int(input("Inserisci il numero che pensi che il computer abbia pensato (da 1 a 5):      "))

if user_int == random_secret_int:
    
    print("Hai vinto!!!")
    print("Hai vinto!!!")
    print("Hai vinto!!!")
    print("Hai vinto!!!")
    print("Hai vinto!!!")
    print("Hai vinto!!!")
    
    print("il numero che ha pensato il computer era:  ")
    print("--------------------------------------------------------------------")
    print(random_secret_int)
    print("--------------------------------------------------------------------")
    print(" ")
    print("Tu hai scelto:     ")
    print(" ")
    print("--------------------------------------------------------------------")
    print(user_int)
    print("--------------------------------------------------------------------")   
    print(" ")
    
else:
    
    print("Hai perso! :(")
    print("Hai perso! :(")
    print("Hai perso! :(")
    print("Hai perso! :(")
    print("Hai perso! :(")
    print("Hai perso! :(")
    print(" ")
    
    print("il numero che ha pensato il computer era:  ")
    print("--------------------------------------------------------------------")
    print(random_secret_int)
    print("--------------------------------------------------------------------")
    print(" ")
    print("Tu hai scelto:     ")
    print(" ")
    print("--------------------------------------------------------------------")
    print(user_int)
    print("--------------------------------------------------------------------")   
    print(" ")
    print("Riprovaci!!!!") 
    print(" ")
