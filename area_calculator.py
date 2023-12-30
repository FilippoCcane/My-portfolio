import math
import time
import os

print(""" CIRCLE
                  _ _ _ _    _ _ _ _                                            
         /\      |       \  |             /\                                      
        /  \     |       |  |            /  \         __  __       __        
       /    \    |-------/  |---        /    \       |   |__| |   |                
      /------\   |     \    |          /------\      |__ |  | |__ |__ .          
     /        \  |      \   |         /        \             
    /          \ |       \  |_ _ _ _ /          \                          MADE BY FilippoCcane     
    """)
domanda_di_cosa = str(input("""Che cosa vuoi fare?
                            
A: Calcolare circonferenza
B: Calcolare area 
C: Formule inverse
D: INFO e Report
:"""))


if domanda_di_cosa == str("A"):
    domanda_dia_or_r = str(input("""Vuoi inserire:
A: raggio
B: diametro

:"""))
    
    if domanda_dia_or_r == str("A"):
        os.system('cls')
        raggio = float(input("Raggio:   "))
        os.system('cls')
        print("Sto calconlando")
        time.sleep(1)
        os.system('cls')
        print("Sto calconlando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calconlando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calconlando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (raggio * float(2) * math.pi))
        

    elif domanda_dia_or_r == str("B"):
        os.system('cls')
        diametro = float(input("Diametro:   "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (diametro * math.pi))
        
elif domanda_di_cosa == str("B"):
    domanda_dia_or_r = str(input("""Vuoi inserire:
A: raggio
B: diametro

:"""))
    
    if domanda_dia_or_r == str("A"):
        os.system('cls')
        raggio = float(input("Raggio:   "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", ((raggio * raggio) * math.pi))
        

    elif domanda_dia_or_r == str("B"):
        os.system('cls')
        diametro = float(input("Diametro:   "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", ((diametro * diametro) * math.pi))
        
elif domanda_di_cosa == str("C"):
    cosa_form_inv = str(input("""Che formula inversa vuoi usare?
                              
---------------------------------------                             
A:Trovare diametro da Area            |
B:Trovare diametro da Circonferenza   |
--------------------------------------|
C:Trovare raggio da Area              |
D:Trovare raggio da Circonferenza     |
---------------------------------------
"""))
    
    if cosa_form_inv == str("A"):

        os.system('cls')
        dom_area = float(input("Inseisci Area:  "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (math.sqrt (dom_area / math.pi) * 2))
        
    elif cosa_form_inv == str("B"):
    
        os.system('cls')
        dom_circ = float(input("Inseisci Circonferenza:  "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (dom_circ / math.pi))
               
    elif cosa_form_inv == str("C"):
        os.system('cls')
        dom_area = float(input("Inseisci Area:  "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (math.sqrt (dom_area / math.pi)))
   
    elif cosa_form_inv == str("D"):
        
        os.system('cls')
        dom_circ = float(input("Inseisci Circonferenza:  "))
        os.system('cls')
        print("Sto calcolando")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando.")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando..")
        time.sleep(1)
        os.system('cls')
        print("Sto calcolando...")
        time.sleep(1)
        os.system('cls')
        
        print("Il risultato è: ", (dom_circ / math.pi / 2))
        
elif domanda_di_cosa == str("D"):
    
    print("""
Produttore: FilippoCcane
Language: Italian
GitHub: @FilippoCcane
Telegram: @FilippoCcane_

Descrizione: 
    Questa é una calcolatrice dotata di formule inverse.
    Essa per tutto l algoritmo non viene utilizzata la semplificazione 3.14 ma 
    viene importato il modulo conpreso in python chiamato math
    
    Se riscontrate problemi non esitate a farmelo sapere sul mio Telegram.
     
        
    Vi ringrazio di aver visualizzato tutto questo!      
          """)

#Lo so che avrei potuto vettere "time.sleep" etc... in un "def" e utilizzarlo ma mi sembrava giusto che voi vedeste tutto quello che c'é dietro.