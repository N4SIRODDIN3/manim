from manim import *
HOME = "D:\Manim_Tutorial\updaters_gear_train"

class Updater1(Scene):
    def construct(self):
        NP = NumberPlane(
            x_range=range(-4.01,4.01), y_range=range(-4.01,4.01), axis_config={'stroke_with': 5}, background_line_style={'stroke_color':TEAL, 'stroke_width':3, 'stroke_opacity': 0.6},
        )
        (RedGear, BlueGear) = SVGMobject(f"{HOME}\\Gears.svg")
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
            x_range=range(-4.01,4.01), y_range=range(-4.01,4.01), axis_config={'stroke_with': 5}, background_line_style={'stroke_color':TEAL, 'stroke_width':3, 'stroke_opacity': 0.6},
        )
        (RedGear, BlueGear) = SVGMobject(f"{HOME}\\Gears.svg")
        BlueGear.scale(2).center()

        fps = 60
        dt = 1/fps
        run_time = 2
        '''def update_function(mobj):
            mobj.rotate(2 * PI)'''
        
        self.add(BlueGear, NP)
        for _ in range(run_time * fps):
            BlueGear.rotate(dt * 180 * DEGREES)
            self.wait()

        '''BlueGear.add_updater(update_function)
        self.play(BlueGear.animate(rate_func=there_and_back, run_time=2).shift(UP * 2))'''