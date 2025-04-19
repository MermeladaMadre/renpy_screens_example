screen hud_box:
    
    timer 1.0 repeat True action [If(gtimer > 1, SetVariable("gtimer",gtimer - 1), Jump("gameover"))]

    # Botón Catálogo de Enemigos
    frame:
        align (1.0,0.03)
        padding (20,20)
        background None

        hbox:
            imagebutton:
                auto "images/btncatalog_%s.png"
                action Show("ventana_catalogo_enemigos", dissolve)

    # Temporizador
    frame:
        align (0.5,0.03)
        xsize 64
        ysize 64
        background None
        add "images/action_frame.png"
        text "[gtimer]" color "#FFFFFFAA" size 20 align (0.70,0.60) bold True 
      
screen ventana_catalogo_enemigos():    
    modal True
    
    # Marco principal
    frame:
        align (0.5,0.1)
        xsize 844
        ysize 453
        background None
        add "panelsettings.png"

        # Botones añadir y eliminar
        frame:
            padding(10,10)
            align (0.05,0.0)
            background None

            hbox spacing 5:
                imagebutton:
                    auto "images/add_%s.png"
                    action Jump("crear_nuevo_enemigo")
                imagebutton:
                    auto "images/delete_%s.png"
                    action [Function(delete_enemigo,lst_enemigo[indx_enemigo]),Show("ventana_catalogo_enemigos")] 

        # Marco foto y datos
        frame:
            padding (30,20)
            background None

            has vbox spacing 15
            align (0.1,0.1)

            label "CATÁLOGO DE ENEMIGOS" xalign 0.5 text_color "#FFFFFF"
            
            hbox:
                spacing 15

                # Foto enemigo
                frame:
                    background None
                    #padding (20,20)
                    xsize 263
                    ysize 346
                    add cat_enemigos[lst_enemigo[indx_enemigo]]['imagen'] align((0.5, 0.5))
                    add status_frame align((0.5, 0.5))
                    add "frame_enemy.png" align((0.5, 0.5))
                
                # Datos    
                frame:
                    background None
                    
                    label "[cat_enemigos[lst_enemigo[indx_enemigo]]['Nombre']]" xalign 0.5 text_color "#1eff00"

                    vbox spacing 5:
                        align (0.1,0.5)
                        xsize 500 
                        ysize 120 
                        
                        hbox spacing 20:
                            hbox spacing 5:
                                text "Tipo:" color "#1eff00" size 20
                                text "[cat_enemigos[lst_enemigo[indx_enemigo]]['Tipo']]" color "#ffffff" size 20
                            hbox spacing 5:
                                text "HP:" color "#fff700"
                                text "[cat_enemigos[lst_enemigo[indx_enemigo]]['HP']]" color "#ffffff"
                            hbox spacing 5:
                                text "Maná:" color "#0026ff"
                                text "[cat_enemigos[lst_enemigo[indx_enemigo]]['Mana']]" color "#ffffff"
                        
                        vbox spacing 5:
                            text "Detalles:" color "#fe0606"
                            text "[cat_enemigos[lst_enemigo[indx_enemigo]]['Detalles']]" color "#ffffff"

        # Botón Status
        frame:
            align (0.16,0.9)
            background None
            xsize 55
            ysize 34
            imagebutton:
                idle status_btn
                hover status_btn
                action Function(toggle_status)


        # Botónes de desplazamiento
        frame:
            background None
            align (0.99,0.99)
            padding (10,10)
            has hbox spacing 10

            imagebutton:
                idle "images/btnback_idle.png"
                hover "images/btnback_hover.png"
                action [If(indx_enemigo <= 0,SetVariable("indx_enemigo",num_enemigos - 1),SetVariable("indx_enemigo",indx_enemigo - 1))]
                

            imagebutton:
                idle "images/btnfoward_idle.png"
                hover "images/btnfoward_hover.png"                    
                action [If(indx_enemigo >= num_enemigos -1,SetVariable("indx_enemigo",0),SetVariable("indx_enemigo",indx_enemigo + 1))]

        
        # Botón de cerrar
        frame:
            background None
            align (1.0,0.0)
            padding (10,10)
            
            imagebutton:
                idle "images/exit_idle.png"
                hover "images/exit_hover.png"
                action Hide(None,dissolve)


