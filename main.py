def on_button_pressed_a():
    game.start_countdown(10000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.show_string("[Speaker] Game resumed.")
    game.resume()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    basic.show_string("[Speaker] Game paused.")
    game.pause()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

Players = 0
game.add_life(1)
Players += 1