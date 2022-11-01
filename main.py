def on_button_pressed_a():
    if Math.random_boolean():
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.DUCK)
input.on_button_pressed(Button.A, on_button_pressed_a)
