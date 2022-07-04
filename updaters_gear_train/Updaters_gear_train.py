from manim import *

# HOME = "D:\Manim_Tutorial\updaters_gear_train"


class Updater1(Scene):
    def construct(self):
        NP = NumberPlane(
            x_range=(-4.01, 4.01),
            y_range=(-4.01, 4.01),
            axis_config={"stroke_width": 5},
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 3,
                "stroke_opacity": 0.6,
            },
        )
        (RedGear, BlueGear) = SVGMobject("Gears.svg")
        BlueGear.scale(2).center()

        def update_function(mobj):
            mobj.rotate(2 * PI)

        self.add(BlueGear, NP)

        BlueGear.add_updater(update_function)
        self.play(BlueGear.animate(rate_func=there_and_back, run_time=2).shift(UP * 2))


class Updater_Demo(Scene):
    def construct(self):

        config.max_files_cached = -1

        NP = NumberPlane(
            x_range=(-4.01, 4.01),
            y_range=(-4.01, 4.01),
            axis_config={"stroke_width": 5},
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 3,
                "stroke_opacity": 0.6,
            },
        )
        BlueGear = RegularPolygon(n=6)
        BlueGear.scale(2).center()

        fps = 60
        dt = 1 / fps
        run_time = 2
        """def update_function(mobj):
            mobj.rotate(2 * PI)"""

        self.add(BlueGear, NP)
        for _ in range(run_time * fps):
            BlueGear.rotate(dt * 180 * DEGREES)
            self.wait()

        """BlueGear.add_updater(update_function)
        self.play(BlueGear.animate(rate_func=there_and_back, run_time=2).shift(UP * 2))"""


class mult_updaters(Scene):
    def construct(self):
        NP = NumberPlane(
            x_range=(-4.01, 4.01),
            y_range=(-4.01, 4.01),
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

        point = Dot(color=YELLOW)
        path = RoundedRectangle(height=4, width=8, corner_radius=0.5)

        def dependent(mobj):
            mobj.move_to(point.get_center())

        def updater_func(mobj, dt):
            mobj.rotate(
                dt * PI
            )  # same as: for i in range(run_time * fps): rotate(dt * PI), while dt is 1/30,15,60

        self.add(NP, point, BlueGear)
        BlueGear.add_updater(dependent)  # Looks just like always redraw.
        BlueGear.add_updater(updater_func)
        self.wait(3)
        self.play(point.animate(rate_func=smooth, run_time=2).move_to(path.get_start()))
        self.wait()
        self.play(MoveAlongPath(point, path, run_time=2))
        BlueGear.remove_updater(dependent)
        self.wait()
