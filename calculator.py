lista_report = []

input_primario = input("Scegli un segno: +, -, x, : ")

if input_primario == ("+"):
    
    piu_n_uno = int(input("Inserisci il primo numero: "))
    
    piu_n_due = int(input("Inserisci il secondo numero: "))
    
    print(piu_n_uno + piu_n_due)
    
    
elif input_primario == ("-"):
    
    meno_n_uno = int(input("Inserisci il primo numero: "))
    
    meno_n_due = int(input("Inserisci il secondo numero: "))
    
    print(meno_n_uno - meno_n_due)


elif input_primario == ("x"):
    
    per_n_uno = int(input("Inserisci il primo numero: "))
    
    per_n_due = int(input("Inserisci il secondo numero: "))

    print(per_n_uno * per_n_due)
    
    
elif input_primario == (":"):
    
    diviso_n_uno = int(input("Inserisci il primo numero: "))
    
    diviso_n_due = int(input("Inserisci il secondo numero: "))
    
    print(diviso_n_uno / diviso_n_due)
    
    
else:
    
    print("Controlla di aver inserito una delle possibili operazioni!")

    report = input("Inserisci eventuale bug (\"Enter\" se non c'é nessun bug):       ")

    if report != (""):
        
        print(report)
        
        confirm = input("Vuoi inviare il feedback?  - si -          - no -         ")
        
        if confirm == ("no"):
            
            print("Riavvia il programma")
                       
        elif confirm == ("si") :
             
            print("Grazie per il feedback!")
            
            lista_report.insert(1, report)
                     
    else:
        
        print("Riavvia il programma!")
