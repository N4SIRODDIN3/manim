from manim import *


class Updater1(Scene):
    def construct(self):

        NP = NumberPlane(
            x_range=(-4.01, 4.01, 1),
            y_range=(-4.01, 4.01, 1),
            axis_config={"stroke_width": 5},
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 3,
                "stroke_opacity": 0.6,
            },
        )

        # (RedGear, BlueGear) = SVGMobject("Gears.svg")
        BlueGear = RegularPolygon(n=6).set_color(BLUE)
        BlueGear.scale(2).center()

        def update_function(mobj):
            mobj.rotate(2 * PI)

        self.add(NP, BlueGear)

        BlueGear.add_updater(
            update_function
        )  # Nothing will happen because the BlueGear isn't dependent on another mobj that is animated.

        self.play(BlueGear.animate(run_time=2, rate_func=there_and_back).shift(UP * 2))
