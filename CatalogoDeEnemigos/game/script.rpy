#region definición de variables
define witch = {'Tipo': "Bruja"
    ,'imagen':"witch_idle.png"
    ,'Nombre':"Zahia"
    ,'HP':70
    ,'Mana':200
    ,'Detalles':"Descendiente de Llohorul"
    }

define skeleton = {'Tipo': "Esqueleto",'imagen':"skeleton_idle.png",'Nombre':"Iho",'HP':70,'Mana':0,'Detalles':"Su punto debil es la cuenca de los ojos."}

define wraith = {'Tipo': "Espectro",'imagen':"wraith_idle.png",'Nombre':"Yerah",'HP':30,'Mana':200,'Detalles':"Sólo los objetos sagrados pueden causarle daño."}

define succubus = {'Tipo': "Sucubo",'imagen':"succubus_idle.png",'Nombre':"Aihaz",'HP':100,'Mana':200,'Detalles':"Demonio femenino que aparece en sueños para seducir a hombres."}

define daemon = {'Tipo': "Demonio",'imagen':"daemon_idle.png",'Nombre':"Llohorul",'HP':200,'Mana':200,'Detalles':"No hay detalles"}

default cat_enemigos = {'Bruja':witch,'Esqueleto':skeleton,'Espectro':wraith,'Sucubo':succubus,'Demonio':daemon}

default indx_enemigo = 0
default lst_enemigo = list(cat_enemigos.keys())
default num_enemigos = len(lst_enemigo)
default enemigo_actual = cat_enemigos[lst_enemigo[indx_enemigo]]
default msgn = ""

default i_enemigo = enemigo_actual
default i_tipo = i_enemigo['Tipo']
default i_imagen = i_enemigo['imagen']
default i_nombre = i_enemigo['Nombre']
default i_hp = i_enemigo['HP']
default i_mana = i_enemigo['Mana']
default i_detalles = i_enemigo['Detalles']

default gtimer = 60 

define transparent_frame = "images/transparent_frame.png"
define mano_frame = "images/mano_frame.png"
default status_frame = transparent_frame

define statusbtn_live = "images/statusbtn_live.png"
define statusbtn_obliterated = "images/statusbtn_obliterated.png"
default status_btn = statusbtn_live

#endregion definición de variables

#region definiciones de python

init python:

    def update_enemigo(n_enemigo):
        global cat_enemigos

        cat_enemigos.update(n_enemigo)

        return cat_enemigos


    def delete_enemigo(s_keyenemigo):
        global cat_enemigos
        global lst_enemigo
        global num_enemigos
        global indx_enemigo

        if s_keyenemigo in cat_enemigos:
            del cat_enemigos[s_keyenemigo]
            lst_enemigo = list(cat_enemigos.keys())
            num_enemigos = len(lst_enemigo)
            if(indx_enemigo >= num_enemigos):
                indx_enemigo = num_enemigos - 1
            
            msgn = "El registro del enemigo {} se ha eliminado.".format(s_keyenemigo)
            renpy.notify(msgn)

        else:
            msgn = "El registro del enemigo {} no se ha eliminado.".format(s_keyenemigo)
            renpy.notify(msgn)

        return cat_enemigos


    def insert_enemigo(tipo,nombre,hp,mana,detalles): 
        global cat_enemigos
        global lst_enemigo
        global num_enemigos
        imagen = "witch_idle.png"

        if tipo == 'Bruja':
            imagen = "witch_idle.png"
        elif tipo == 'Esqueleto':
            imagen = "skeleton_idle.png"
        elif tipo == 'Espectro':
            imagen = "wraith_idle.png"
        elif tipo == 'Sucubo':
            imagen = "succubus_idle.png"
        elif tipo == 'Demonio':
            imagen = "daemon_idle.png"


        enemigo = {'Tipo': tipo
            ,'imagen':imagen
            ,'Nombre':nombre
            ,'HP':hp
            ,'Mana':mana
            ,'Detalles':detalles
            }

        cat_enemigos.update({nombre:enemigo})
        lst_enemigo = list(cat_enemigos.keys())
        num_enemigos = len(lst_enemigo)

        return enemigo
        
    def toggle_status():
        global statusbtn_live
        global statusbtn_obliterated
        global status_btn
        global transparent_frame
        global mano_frame
        global status_frame

        if status_btn == statusbtn_live:
            status_btn = statusbtn_obliterated
            status_frame = mano_frame
        else:
            status_btn = statusbtn_live
            status_frame = transparent_frame

            


            



#endregion definiciones de python

label start:
    scene bg abandoned_house

    pause 2.0

    show screen hud_box

    "(La lluvia es intensa afuera)"

    "(El tiempo es limitado)"
    
    "(Los enemigos te acechan)"

    menu mnu_acciones:        
        "Modificar catálogo":
            jump modificar_catalogo
        "Abandonar":
            return
    jump start

label gameover:
    hide screen hud_box
    with dissolve

    if renpy.get_screen("ventana_catalogo_enemigos"):
        hide screen ventana_catalogo_enemigos
        with dissolve
        pause 1.0



    "Tu tiempo se ha acabado."

    menu reiniciar:

        "Reiniciar":
            $ gtimer = 10
            jump start
        "Modificar catálogo":
            jump modificar_catalogo
        "Abandonar":
            return



