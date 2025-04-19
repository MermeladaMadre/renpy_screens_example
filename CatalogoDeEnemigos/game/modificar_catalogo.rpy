label modificar_catalogo:
    # if renpy.get_screen("ventana_catalogo_enemigos"):
    #     hide screen ventana_catalogo_enemigos
    #     with dissolve

    pause 1.0

    "(La lluvia cae copiosamente)"

    menu acciones_catalogo:

        "Mostrar catálogo":
            if not renpy.get_screen("ventana_catalogo_enemigos"):
                call screen ventana_catalogo_enemigos
                with dissolve
            
            "(El ambiente es denso)"
            
        "Crear nuevo enemigo":
            jump crear_nuevo_enemigo
        "Salir":
            jump gameover

    jump modificar_catalogo

label crear_nuevo_enemigo:
    if renpy.get_screen("ventana_catalogo_enemigos"):
        hide screen ventana_catalogo_enemigos
        with dissolve
        pause 0.5


    menu mnutipo:
        "Seleccióne el tipo de enemigo."

        "Bruja":
            $ i_tipo = "Bruja"
        "Esqueleto":
            $ i_tipo = "Esqueleto"
        "Espectro":
            $ i_tipo = "Espectro"
        "Sucubo":
            $ i_tipo = "Sucubo"
        "Demonio":
            $ i_tipo = "Demonio"
        "Cancelar":
            jump modificar_catalogo

    $ i_nombre = renpy.input("Escriba el nombre del enemigo: ", default = "")
    if(i_nombre == ""):
        "El nombre no puede estar vacío."
        jump crear_nuevo_enemigo
    elif(i_nombre in lst_enemigo):
        "El enemigo ya existe, intente nuevamente."
        jump crear_nuevo_enemigo

    $ i_hp = int(renpy.input("Escriba la cantidad de vida (0-100): ", allow="0123456789", default = 0))
    $ i_mana = int(renpy.input("Escriba la cantidad de magia (0-100): ", allow="0123456789", default = 0))
    $ i_detalles = renpy.input("Escriba los detalles importantes (255 caracteres): ", default = "")

    menu mnucontinuarnuevo:
        "Tipo: [i_tipo], Nombre: [i_nombre], HP: [i_hp], Maná: [i_mana], Detalles: [i_detalles]"
        
        "Continuar":
            $ insert_enemigo(i_tipo,i_nombre,i_hp,i_mana,i_detalles)
            if not renpy.get_screen("ventana_catalogo_enemigos"):
                call screen ventana_catalogo_enemigos
                with dissolve
            jump modificar_catalogo
        "Cancelar":
            jump modificar_catalogo





