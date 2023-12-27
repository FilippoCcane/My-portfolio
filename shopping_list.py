Lista_spesa = []
print("-------------------------------------------------------------------------------------------------------------------------------")
print("Per fermare il programma fai: CTRL + C")
def run():
    
    domanda_primaria =str(input("""Che tipo di modifiche vuoi apportare alla tua lista?
                                
    A: vedere la lista          B:aggiungere elemento alla lista        C:rimuovere elemento dalla lista
    
                                                     """))

    

    if domanda_primaria == str("a"):
    
        print(Lista_spesa)

    elif domanda_primaria == str("b"):
        
        new = str(input("Elemento da aggiungere:  "))
        
        def add():
            
            Lista_spesa.insert(1, new)  
            
        confirm = input("""Vuoi davvero aggiungerlo?

            a: si                              b: no  
                              """)
        
        if confirm == str("a") or str("si"):
            
            add()
                
            while True:

                run()

        elif confirm == str("b") or str("no"):   
                    
            while True:
                    
                run()
        
        else:
            
            while True:
                
                run()
                
    elif domanda_primaria == str("c"):
        
        el_rim = str(input("Inserire elemento da rimuovere:    "))

        confirm_rem = str(input("Vuoi cancellare " + el_rim + """ ?
                                
            a: si                               b: no
            
                                """))
                
        if confirm_rem == str("a") or str("si"):
            
            Lista_spesa.remove(el_rim)
            
        elif confirm_rem == str("b") or str("no"):
            
            while True:
                
                run()
            
            
            
            
            
run()
