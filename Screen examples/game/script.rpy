# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alice", color="#ff0000")
define e = Character("Eve", color="#eaff00") 
define n = Character("---", color="#757575")

default mana = 10
default sangre = 100

define mirespuesta = 0
define is_alice_visible = False
define my_dictionary = {}

# The game starts here.

label start:
    scene bg pond1_day
    pause 1.0

    n "Un día normal (presiona haz click para continuar)"

    scene bg pond1_day
    pause 1.0

    show screen screens_manager


    show alice blush at left
    a "Hola Eve"
    
    show eve smile at right
    e "Hola Alice"

    show alice doubt
    
    menu tema:
        a "¿Sabes usar..."

        "Diccionarios?":                
            call fn_dictionary()
        "Funciones?":
            show eve surprise
            e "Sí claro. ¿Acaso tú no?"

    menu claro_que_se:
        a "Claro que sé"

        "(Es mentira)":
            $ mirespuesta = "Sí claro"

        "(Sí, pero no me acuerdo bien.)":
            $ mirespuesta = "Sí, peeeero, hay cosas que no entiendo."

    call func_responder(e,mirespuesta)

    e "Pues si hay algo que no te acuerdes, pregúntame."

    a "[_return]"

    jump menus_frame



label func_responder(_character,_respuesta):

    _character "Debo responder que [_respuesta]"

    return "Todo lo que diga, la mitad no lo creas y la otra mitad ponla en duda."

label calculadora(operador,operando,operacion):
    e "El cálculo será de [operador] [operacion] [operando]"
    $ nOperador = float(operador)
    $ nOperando = float(operando)
    $ nResultado = 0

    if(operacion == "*"):
        $ nResultado = nOperador * nOperando

    return nResultado



label menus_frame:

    #hide screen sc_frame_hp
    hide screen screens_manager

    hide alice
    hide eve

    show bg pond1_evening
    with fade

    pause 1.0

    show alice default

    show screen sc_reducir_valores
    show screen sc_menu_reiniciar_valores
    show screen sc_buttons

    "Puedes jugar con los valores de los menus."

    "Yo mientras seguiré aquí"

    "Pero si sigues presionando el juego se termina."

    call fn_asigna_valores(3,70)

    "Puntos de mana: [mana], puntos de sangre: [sangre]"

    menu dmenus:
        "¿Seguro que quieres terminar?"

        "No, quiero seguir picando botones.":
            jump menus_frame
        "Sí, sácame de aquí":
            "Escucho y obedezco."
            return

