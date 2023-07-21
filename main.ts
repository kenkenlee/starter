input.onButtonPressed(Button.A, function () {
    dhksjjgkfjgrajgh += 4000
})
input.onButtonPressed(Button.B, function () {
    dhksjjgkfjgrajgh += 4000
})
let dhksjjgkfjgrajgh = 0
let idk_oidfjdfj = 60
basic.forever(function () {
    while (dhksjjgkfjgrajgh == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            . # . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . # . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . # .
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . # .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # .
            `)
        basic.pause(dhksjjgkfjgrajgh)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # . .
            `)
        basic.pause(dhksjjgkfjgrajgh)
    }
    for (let index = 0; index < 10; index++) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
})
basic.forever(function () {
    idk_oidfjdfj += 2
    basic.pause(100)
})
basic.forever(function () {
    while (dhksjjgkfjgrajgh == 0) {
        music.play(music.createSoundExpression(WaveShape.Noise, 3328, 931, 255, 255, 5000, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    while (dhksjjgkfjgrajgh == 0) {
        music.play(music.stringPlayable("F B D A C5 E G C ", idk_oidfjdfj), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function () {
    if (dhksjjgkfjgrajgh >= 4000) {
        music.play(music.stringPlayable("C C5 C C5 C C5 C C5 ", 500), music.PlaybackMode.UntilDone)
    }
})
