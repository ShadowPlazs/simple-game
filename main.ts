input.onButtonPressed(Button.A, function () {
    game.startCountdown(10000)
    game.addScore(100)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showString("[Speaker] Game resumed.")
    game.resume()
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString("[Speaker] Game paused.")
    game.pause()
})
let Players = 0
game.addLife(1)
Players += 1
