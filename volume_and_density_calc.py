import os
import time

os.system("cls")
print ("Press ctrl + c to terminate")
print('''
          ____                         _____    ______                 
\      / /    \ |                     |     \  |       |\   |   
 \    /  |    | |                     |      \ |___    | \  |             __          __                 
  \  /   |    | |                     |      / |       |  \ |            |    /\ |   |                         
   \/    \____/ |_____ 0      AND     |_____/  |______ |   \| 0          |__ /  \|__ |__               By FilippoCcane''')


what_to = int(input("""WHAT do you want to do:
	1: Calculate density
	2: Calculate Volume
	3: Info
 	
   Ans: """))

if what_to == int(1):
   what_to_a = int(input("""What do you want to do?
   1: Inverse calculations
   2: Basic calculations
   
   Ans: """))
   
   if what_to_a == int(1):
      m_or_v = int(input("""What are you searching for?
      1: Mass
      2: Volume
      
      Ans: """))
      
      if m_or_v == int(1):
         
         density = float(input("Insert Density: "))
         volume = float(input("Insert Volume: "))
         print("Result: " , (density * volume))

      elif m_or_v == int(2):
         mass = float(input("Insert Mass: "))
         density = float(input("Insert Density"))
         print("Result: " , (mass / density))

   elif what_to_a == int(2):
      mass = float(input("Insert Mass: "))
      volume = float(input("Insert Volume: "))
      print("Result:" , (mass / volume))

elif what_to == int(2):
   what_to_b = int(input("""What do you want to do?
   1: Inverse calculations
   2: Basic calculations
   
   Ans: """))

   if what_to_b == int(1):
      b_or_h = int(input("""What are you searching for?
      1: Base
      2: Height
      
      Ans: """))
      if b_or_h == int(1):
         volume = float(input("Insert Volume: "))
         height = float(input("Insert height: "))
         print("Result: " , (volume / height))
         
      if b_or_h == int(2):
         volume = float(input("Insert Volume: "))
         base = float(input("Insert base: "))
         print("Result: " , (volume / base))

   elif what_to_b == int(2):
      base = float(input("Insert base: "))
      height = float(input("Insert height: "))
      print("Result: " , (base * height))

elif what_to == int(3):
   os.system("cls")
   print("""
-------------------------------------------------------------------------------------
Produttore: FilippoCcane
Script Language: English
Massage Language: Italian
GitHub: @FilippoCcane
Telegram: @FilippoCcane_

Descrizione: 
    Questa é una calcolatrice dotata di formule inverse.
    Essa per tutto l algoritmo non viene utilizzata la semplificazione 3.14 ma 
    viene importato il modulo conpreso in python chiamato math
    
    Se riscontrate problemi non esitate a farmelo sapere sul mio Telegram.
     
        
    Vi ringrazio di aver visualizzato tutto questo!      
          """)



   

         

	
 







