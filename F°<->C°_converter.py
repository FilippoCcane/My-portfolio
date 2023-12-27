domanda_n_1 = str(input("""Cosa vuoi fare?
                        
         Fahrenight-->Celsious     Celsious-->Fahrenight
                 --A--                     --B--
                 
                 
                                """))

if domanda_n_1 == str("A"):
    
    A_Far = int(input("Gradi F°:       "))
    
    print("Gradi C°:      ", (A_Far - 32) * 5/9 )
    
    

else:
    B_Cel = int(input("Gradi C°:       "))

    print("Gradi F°:      ", (B_Cel * 9/5) + 32)
