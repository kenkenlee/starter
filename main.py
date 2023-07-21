def on_button_pressed_a():
    global dhksjjgkfjgrajgh
    dhksjjgkfjgrajgh += 4000
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global dhksjjgkfjgrajgh
    dhksjjgkfjgrajgh += 4000
input.on_button_pressed(Button.B, on_button_pressed_b)

dhksjjgkfjgrajgh = 0
idk_oidfjdfj = 60

def on_forever():
    while dhksjjgkfjgrajgh == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            . # . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            # . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . # . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . # # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . # # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . # .
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . #
            . . . . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . # .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # .
            """)
        basic.pause(dhksjjgkfjgrajgh)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # . .
            """)
        basic.pause(dhksjjgkfjgrajgh)
    for index in range(10):
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
basic.forever(on_forever)

def on_forever2():
    global idk_oidfjdfj
    idk_oidfjdfj += 2
    basic.pause(100)
basic.forever(on_forever2)

def on_forever3():
    while dhksjjgkfjgrajgh == 0:
        music.play(music.create_sound_expression(WaveShape.NOISE,
                3328,
                931,
                255,
                255,
                5000,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever3)

def on_forever4():
    while dhksjjgkfjgrajgh == 0:
        music.play(music.string_playable("F B D A C5 E G C ", idk_oidfjdfj),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever4)

def on_forever5():
    if dhksjjgkfjgrajgh >= 4000:
        music.play(music.string_playable("C C5 C C5 C C5 C C5 ", 500),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever5)
