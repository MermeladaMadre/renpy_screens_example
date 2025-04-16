label fn_dictionary:
    $ orco ={
        'Nombre':"Orco",
        'Descripcion':"Soy feo",
        'HP':50,
        'Mana': 100}

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
    # key : value

    # $ v1 = dict_enemigos['esqueleto']['Nombre']
    # $ v2 = dict_enemigos['esqueleto']['Descripcion']
    # "Mensaje: [v1] y [v2]"

    $ lst_enemigos = ["esqueleto","orco","esbirro"]
    # $ r = renpy.random.randint(0,2)
    # $ v1 = dict_enemigos[lst_enemigos[r]]['Nombre']
    # $ v2 = dict_enemigos[lst_enemigos[r]]['Descripcion']

    $ r = renpy.random.choice(lst_enemigos)
    $ v1 = dict_enemigos[r]['Nombre']
    $ v2 = dict_enemigos[r]['Descripcion']

    
    "Mensaje: [r] - [v1] y [v2]"

    jump fn_dictionary

    menu muestradict:
        "Elige un enemigo:"

        "Enemigo 1":
            "El enemigo 1 es: [dict_enemigos['esqueleto']['Nombre']]"

        "Enemigo 2":
            "El enemigo 2 es: [dict_enemigos['orco']['Nombre']]"

        "Enemigo 3":
            "El enemigo 3 es: [dict_enemigos['nada']]"

