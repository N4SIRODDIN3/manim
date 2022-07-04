from manim import *
import numpy as np
import sympy as sy


def area(plane, graph1, boundary1, x_range, area_color):
    integral = plane.get_area(
        graph=graph1,
        x_range=x_range,
        # stroke_width=0.1,
        color=area_color,
        # dx=dx, #This is a parameter and is optional.
        # It's not a variable
        bounded_graph=boundary1,
    )

    return integral


BackG_image = "C:\Manim_3_feb\manim_ce\SVGs_Images"


class CalculusArea(Scene):
    def construct(self):
        # img = ImageMobject(f"{BackG_image}\\Desert_Sahara.JPG").scale(3)

        plane = NumberPlane()

        axes = (
            Axes(
                x_range=[-5, 5],
                x_length=8,
                y_range=[-10, 10],
                y_length=7,
                x_axis_config={
                    "numbers_to_include": np.arange(
                        -5, 5.5, 1
                    ),  # 10.01 because it doesn't inclueded.
                    "numbers_with_elongated_ticks": np.arange(
                        -5, 5.5, 1
                    ),  # Elongated ticks: means -10,-8,-6... have long ticks
                },
            )
            .to_corner(DR)
            .scale(0.7)
        )

        Vtrack = ValueTracker(-3)  # Don't name it VT, you'll get an ERROR

        def func1(c):
            function = lambda x: x
            # if you get this error: TypeError: 'tuple' object is not callable.
            # Then it's because "comma," has been put it accidentally.
            return function

        def func2(c):
            function = lambda x: -x
            # if you get this error: TypeError: 'tuple' object is not callable.
            # Then it's because "comma," has been put it accidentally.
            return function

        def func3(c):
            function = lambda x: (c - 2) * x + 2
            # if you get this error: TypeError: 'tuple' object is not callable.
            # Then it's because "comma," has been put it accidentally.
            return function

        formulla1 = Tex("\[f(x)=c: \]", color=WHITE).scale(0.7).to_corner(UL)

        # Label for the variable Vtrack
        num = always_redraw(
            lambda: DecimalNumber(include_sign=True)
            .set_value(Vtrack.get_value())
            .next_to(formulla1, RIGHT, buff=0)
            .scale(
                0.7
            )  # I want Vtrack to be a decimal number instead, so set k as is but before
        )

        # If you get this ERROR: TypeError: get_value() takes 1 positional argument but 2 were given: that's because you wrote get_value(2)
        # it should be blank because it will auto get the value from k.
        graphLine = always_redraw(
            lambda: axes.plot(func3(Vtrack.get_value()), x_range=[-5, 5], color=BLUE_E)
        )
        # graphLine2 = axes.plot(lambda x: 3*x, x_range=[-10,10], color=GREEN)
        graph2 = axes.plot(lambda x: -x, x_range=[-5, 0], color=YELLOW)
        graph = axes.plot(lambda x: x, x_range=[0, 5], color=YELLOW)

        # Vtrack_label= always_redraw(lambda: Text("The value of C is: C="))

        def f(x):
            return -(x ** 6) + x ** 3 - x + 4

        x = sy.Symbol("x")
        area1 = DecimalNumber(include_sign=True).set_value(
            sy.integrate(f(x), (x, -1, 1))
        )
        self.add(area1)
        area1_1 = area(axes, graph, x_range=[0, 5], color=BLUE)

        # arrow= always_redraw(lambda: Line(start=formulla1.get_corner(direction=DL),end=graph.get_center()).add_tip())
        # self.play(Create(box))

        self.play(Create(plane), run_time=3)
        self.wait()

        self.add(axes, formulla1, num, graph, graph2, graphLine)
        self.wait()

        self.play(FadeIn(area1_1))
        self.wait(2)

        # self.play(Create(arrow))
        # self.wait(2)
        self.play(Vtrack.animate.set_value(3), run_time=3, rate_func=smooth)
        self.wait(0.5)
