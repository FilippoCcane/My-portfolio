import random 
print("Ciao! Qui potrai creare la tua password casuale!(max18 / min 7")

num_lettere = int(input("Quanti caratteri deve essere la password?     "))

if num_lettere ==  7:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista))

    print(lista_est)

elif num_lettere ==  8:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista))

    print(lista_est)
      
elif num_lettere ==  9:

    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista))

    print(lista_est)      

elif num_lettere ==  10:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista))

    print(lista_est)      

elif num_lettere ==  11:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista))

    print(lista_est)      

elif num_lettere ==  12:
    
    #---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista))

    print(lista_est)      

elif num_lettere ==  13:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista))

    print(lista_est)      
    
elif num_lettere ==  14:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista))

    print(lista_est)      
    
elif num_lettere ==  15:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista))

    print(lista_est)  
    
elif num_lettere ==  16:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista))
    
    print(lista_est)
      
elif num_lettere ==  17:
    
#---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista))
      
    print(lista_est)
    
elif num_lettere ==  18:
    
    #---------------------------------------------------------------------------------------------------------------------------------------
    numeri = [1,2,3,4,5,6,7,8,9,0]
    num_est_1 = random.choice(numeri)
    num_est_2 = random.choice(numeri)
    num_est_3 = random.choice(numeri)
    num_est_4 = random.choice(numeri)
    num_est_5 = random.choice(numeri)
    num_est_6 = random.choice(numeri)
#---------------------------------------------------------------------------------------------------------------------------------------    

    lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    lett_est_1 = random.choice(lettere)
    lett_est_2 = random.choice(lettere)
    lett_est_3 = random.choice(lettere)
    lett_est_4 = random.choice(lettere)
    lett_est_5 = random.choice(lettere)
    lett_est_6 = random.choice(lettere)
    lett_est_7 = random.choice(lettere)
    lett_est_8 = random.choice(lettere)
    
#---------------------------------------------------------------------------------------------------------------------------------------

    simboli = ["!", "(", ")", "[", "]", "{", "}", "@", "-", "_", "#", "?", "$"]
    sim_est_1 = random.choice(simboli)
    sim_est_2 = random.choice(simboli)
    sim_est_3 = random.choice(simboli)
    sim_est_4 = random.choice(simboli)
#---------------------------------------------------------------------------------------------------------------------------------------


    lista = (lett_est_1, lett_est_2, lett_est_3, lett_est_4, lett_est_5, lett_est_6, lett_est_7, lett_est_8,
             num_est_1, num_est_2, num_est_3, num_est_4, num_est_5, num_est_6,
             sim_est_1, sim_est_2, sim_est_3, sim_est_4)
    
    lista_est = (random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista),random.choice(lista),random.choice(lista),
                 random.choice(lista),random.choice(lista))
    
    print(lista_est)
