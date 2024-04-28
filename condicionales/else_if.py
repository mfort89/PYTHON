ingreso_mensual = 7000
gasto_mensual = 1000

#elif anidados

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando demasiado")    

elif ingreso_mensual > 1000:
        print("estas bien economicamente en latinoamerica")
    
elif ingreso_mensual > 10000:
        print("estas bien en argentna")    

    
else:
        print("estas en la pobreza")    
    
    #elif es el elfe if en python