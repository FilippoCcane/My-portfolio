float_2 = float(1.1)

domanda_n_1 = str(input("""Cosa vuoi fare?
                        
               EUR-->USD                 USD-->EUR
                 --A--                     --B--
                 
                 
                                """))

if domanda_n_1 == str("a"):
    
    A_eur = float(input("EUR:       "))
    
    print("USD:      ", (A_eur * float_2 ))
    
elif domanda_n_1 == ("b"):
    
    B_usd = float(input("USD:       "))

    print("EUR:      ", B_usd / float_2 )