input.onButtonPressed(Button.A, function () {
    if (Math.randomBoolean()) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Duck)
    }
})
