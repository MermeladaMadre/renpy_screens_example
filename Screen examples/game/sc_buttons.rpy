screen sc_buttons():
    modal True
    imagebutton:
        xanchor 0.5
        yanchor 0.1
        xpos 0.5
        ypos 0.1
        # idle "switch_idle.png"
        # hover "switch_hover.png"
        auto "switch_%s.png"
        action [Call("play_alice")]

    # imagebutton auto "switch_%s.png" action [Call("play_alice")]


label play_alice():

    if not is_alice_visible:
        show alice blush at right
        $ is_alice_visible = True
    else:
        hide alice
        $ is_alice_visible = False

    return is_alice_visible
