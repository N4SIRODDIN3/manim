from manim import *


class Updater4(Scene):

    def construct(self):
        NP = NumberPlane(x_range=(-4.01, 4.01, 1), y_range=(-4.01,
                         4.01, 1), axis_config={'stroke_width': 5},
                         background_line_style={'stroke_color': TEAL,
                         'stroke_width': 3, 'stroke_opacity': 0.6})

        (RedGear, BlueGear) = SVGMobject('Gears.svg')
        BlueGear.scale(2).center()

        num = DecimalNumber(number=0, num_decimal_places=2)
        
        unit = Tex('rad/s').next_to(num, RIGHT * 0.5)
        velocity = VGroup(num, unit)
        velocity.next_to(BlueGear, DOWN * 3)
        
        bg = Rectangle(fill_opacity=1, fill_color=BLACK,
                       stroke_color='#ff073a')
        bg.round_corners().surround(velocity)

        def update_function(mobj, dt):
            mobj.rotate(dt * num.get_value())
            num.set_value(num.get_value() + dt)

        self.add(NP, BlueGear, bg, velocity)
        self.wait()
        BlueGear.add_updater(update_function)
        self.wait(6)
