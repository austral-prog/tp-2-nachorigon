def change():
    expense = 23.75
    money = 100
    vuelto = money - expense 
    print ("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print ("\nVuelto\n")
    print ("Pesos:")
    print (int(vuelto))
    print ("Centavos:")
    print (int((vuelto - int (vuelto))*100))
change()

