#Questo codice crea dei "dadi" virtuali e in base all input dell utente ci sono 1, 2, 3, 4 dadi"


import random

dado_1 = [1, 2, 3, 4, 5, 6]
dado_2 = [1, 2, 3, 4, 5, 6]
dado_3 = [1, 2, 3, 4, 5, 6]
dado_4 = [1, 2, 3, 4, 5, 6]

print(" ")

print("Inserisci solo un numero (no lettere / Simboli)")

print(" ")

input_primario = int(input("Quanti dadi vuoi usare?       "))

if input_primario > 4:
    
    print("Il massimo di dadi é 4!")
    
    
elif input_primario == (1):
    
    casual_1 = print(random.randint(1, 6))
    
    
elif input_primario == (2):
    
    casual_2_1 = (random.randint(1, 6))
    casual_2_2 = (random.randint(1, 6))
    
    print(casual_2_1, casual_2_2)
    
    print(casual_2_1 + casual_2_2)
    

elif input_primario == (3):
    
    casual_3_1 = (random.randint(1, 6))
    casual_3_2 = (random.randint(1, 6))
    casual_3_3 = (random.randint(1, 6))
    
    print(casual_3_1, casual_3_2, casual_3_3)
    
    print(casual_3_1 + casual_3_2 + casual_3_3)
    
    
elif input_primario == (4):
    
    casual_4_1 = (random.randint(1, 6))
    casual_4_2 = (random.randint(1, 6))
    casual_4_3 = (random.randint(1, 6))
    casual_4_4 = (random.randint(1, 6))
    
    print(casual_4_1, casual_4_2, casual_4_3, casual_4_4)    
    
    print(casual_4_1 + casual_4_2 + casual_4_3 + casual_4_4) 


else:
    
    print("""Controlla di averi inserito solo numeri!
          Riavvia il programma!""")
    

