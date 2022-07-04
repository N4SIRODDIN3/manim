from manim import *


class Updater2(Scene):
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

        (RedGear, BlueGear) = SVGMobject(
            "C:/Manim_3_feb/manim_ce/updaters_gear_train/Gears.svg"
        )
        BlueGear.scale(2).center()

        def update_function(mobj, dt):
            mobj.rotate(dt * PI)

        self.add(NP, BlueGear)

        BlueGear.add_updater(update_function)

        self.wait(2)
        self.play(
            BlueGear.animate(run_time=3, rate_func=there_and_back).shift(UP * 2)
        )  # Goes up there and then back to the start point

        self.wait(2)
        BlueGear.suspend_updating()
        self.wait(3)
        BlueGear.resume_updating()
        self.wait(3)
        BlueGear.remove_updater(update_function)
        self.wait(2)
        # Updater as lambda function
        # Mobject.add_updater(lambda arguments: expression)

        BlueGear.add_updater(lambda m, dt: m.rotate(dt * PI))

        self.wait(3)

        BlueGear.clear_updaters()

    # Since lambda function is anonymous,
    # clear_updaters() is applied to remove all the updaters.
