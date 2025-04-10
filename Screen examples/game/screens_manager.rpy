screen screens_manager():
    window id "Pensamientos":
        vbox:
            spacing 10

            text "Hola mundo"
            text "Otro texto"

screen sc_frame_hp():
    frame:
        modal True

        align (0.9,0.1)
        padding (20,20)

        vbox:
            text "Mana: [mana]"
            text "Sangre: [sangre]"

screen sc_reducir_valores():
    frame:
        align (0.8,0.7)
        padding (20,20)

        hbox:
            textbutton "- Maná":
                #if mana > 0:
                action [SetVariable("mana", mana - 1)]
            textbutton "- Sangre":
                #if sangre > 0:
                action [SetVariable("sangre", sangre - 1)]


screen sc_menu_reiniciar_valores():

    frame:

        align (0.1,0.1)
        padding (20,20)

        vbox:
            textbutton "Reiniciar":
                action [SetVariable("mana", 10), SetVariable("sangre", 100), Return()]


label fn_asigna_valores(_mana,_sangre):
    $ mana = _mana
    $ sangre = _sangre