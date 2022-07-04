from manim import *


class Updater3(Scene):
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

        (RedGear, BlueGear) = SVGMobject("Gears.svg")
        BlueGear.scale(2).center()

        Point = Dot(color=YELLOW)
        Path = Square(4)

        def update_function(mobj):
            mobj.move_to(Point.get_center())

        self.add(NP, BlueGear, Point)

        BlueGear.add_updater(update_function)

        self.play(Point.animate.move_to(Path.get_start()))
        self.play(MoveAlongPath(Point, Path, run_time=4, rate_func=linear))

        self.wait(2)

        def update_function_dt(mobj, dt):
            mobj.rotate(dt * PI)

        BlueGear.add_updater(update_function_dt)  # Now, the updater animation starts

        self.wait(2)  # Holder: animate it 2s before the next one starts.

        self.play(MoveAlongPath(Point, Path, run_time=4, rate_func=linear))
