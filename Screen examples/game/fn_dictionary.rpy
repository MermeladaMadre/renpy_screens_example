label fn_dictionary:

    # Arreglo con los datos de un orco
    $ a_orco = ["Orco",
                "Soy feo",
                50, 
                100]

    $ vida_orco = a_orco[2] #Ejemplo de uso

    # Diccionario con los datos de un orco
    $ orco ={
        'Nombre':"Orco",
        'Descripcion':"Soy feo",
        'HP':50,
        'Mana': 100}

    $ vida_orco = orco['HP'] #Ejemplo de uso
    
    $ orco['HP'] = 10 # Modificación de un valor

    $ orco['Status'] = "Vivo" # Agregando campos

    "Datos del orco: Nombre: [orco['Nombre']], HP: [orco['HP']], Estatus: [orco['Status']]"


    $ esqueleto = {
        'Nombre':"Esqueleto",
        'Descripcion':"Soy flaco",
        'HP':50,
        'Mana': 0}
    
    $ esbirro = {
        'Nombre':"Esbirro",
        'Descripcion':"Soy chiquito",
        'HP':10,
        'Mana': 0}
    
    $ dict_enemigos = {
                        'esqueleto':esqueleto,
                        'orco':orco,
                        'esbirro':esbirro}

    menu muestradict:
        "Elige un enemigo:"

        "Enemigo 1":
            "El enemigo 1 es: [dict_enemigos['esqueleto']['Nombre']]"

        "Enemigo 2":
            "El enemigo 2 es: [dict_enemigos['orco']['Nombre']]"

        "Enemigo 3":
            "El enemigo 3 es: [dict_enemigos['nada']]"

