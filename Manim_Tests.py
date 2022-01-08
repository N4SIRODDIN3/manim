from PIL.Image import linear_gradient
from manim import *
import numpy as np
from itertools import takewhile
from textwrap import wrap

from manim.mobject.mobject import T


class writting1(Scene):
    def construct(self):
        phrase1 = Text(
            "This is a text in normal mode.", fill_color="#E45", font="ALGERIAN"
        ).to_corner(UL)
        phrase2 = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)").next_to(
            phrase1, direction=DOWN, buff=1
        )
        formulla1 = Tex(
            "\[f(x)=0.1 * (x - 4) * (x - 1) * (x + 3) {0}\]", color=WHITE
        ).to_corner(UL)
        # Label for the variable Vtrack

        # ---------------------------
        k = ValueTracker(0)  # I want to track this number

        num = always_redraw(
            lambda: DecimalNumber().set_value(
                k.get_value()
            )  # I want k to be a decimal number instead, so set k as is but before
        )
        box = SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.5, fill_color=GREEN, buff=2
        )
        self.play(Create(box))
        self.play(FadeIn(num))
        self.wait(0.5)
        self.play(k.animate.set_value(20), runtime=3, rate_func=smooth)


class writting2(Scene):
    def construct(self):
        formulla1 = Tex("\[f(x)=\sqrt{5x}\]", color=WHITE).scale(0.7).to_corner(UL)
        # Label for the variable Vtrack
        phrase1 = Text(
            "This is a text in normal mode {}.", fill_color="#E45", font="ALGERIAN"
        ).to_corner(UL)

        # ---------------------------
        k = ValueTracker(0)  # I want to track this number

        num = always_redraw(
            lambda: DecimalNumber().set_value(
                k.get_value()
            )  # I want k to be a decimal number instead, so set k as is but before
        )
        box = SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.5, fill_color=GREEN, buff=2
        )
        self.play(Create(formulla1))
        # self.play(FadeIn(num))
        self.wait(0.5)
        self.play(k.animate.set_value(20), runtime=3, rate_func=smooth)
        self.wait(0.5)


class Tracker(Scene):
    def construct(self):
        Vtrack = ValueTracker(0)
        formulla1 = Tex(
            "\[f(x)=0.1 * (x - 4) * (x - 1) * (x + 3)+\]", color=WHITE
        ).to_corner(UL)
        # Label for the variable Vtrack
        num = always_redraw(
            lambda: DecimalNumber()
            .set_value(Vtrack.get_value())
            .next_to(
                formulla1, RIGHT
            )  # I want Vtrack to be a decimal number instead, so set k as is but before
        )
        box = SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.5, fill_color=GREEN, buff=0.3
        )
        self.play(Write(formulla1, run_time=3))
        self.wait(0.3)
        self.play(Create(box))
        self.wait(0.3)
        self.play(FadeIn(num))
        self.wait(0.5)
        self.play(Vtrack.animate.set_value(20), runtime=3, rate_func=linear)


class Push1(Scene):
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

        Vtrack = ValueTracker(0)  # Don't name it VT, you'll get an ERROR

        def func(c):
            function = lambda x: 0.1 * (x - 4) * (x - 1) * (x + 3) + c
            # if you get this error: TypeError: 'tuple' object is not callable.
            # Then it's because "comma," has been put it accidentally.
            return function

        formulla1 = Tex("\[f(x)=\sqrt{5x}\]", color=WHITE).scale(0.7).to_corner(UL)
        # Label for the variable Vtrack
        num = always_redraw(
            lambda: DecimalNumber(include_sign=True)
            .set_value(Vtrack.get_value())
            .next_to(
                formulla1, RIGHT
            )  # I want Vtrack to be a decimal number instead, so set k as is but before
        )
        graph = always_redraw(
            lambda: axes.plot(func(Vtrack.get_value()), x_range=[0, 5], color=YELLOW)
        )

        # If you get this ERROR: TypeError: get_value() takes 1 positional argument but 2 were given: that's because you wrote get_value(2)
        # it should be blank because it will auto get the value from k.

        graphLine = axes.plot(lambda x: x, x_range=[0, 7], color=WHITE)
        # graphLine2 = axes.plot(lambda x: 3*x, x_range=[-10,10], color=GREEN)

        # Vtrack_label= always_redraw(lambda: Text("The value of C is: C="))
        area = always_redraw(
            lambda: axes.get_area(
                graph=graph,
                x_range=[0, 5],
                # stroke_width=0.1,
                color=[GREEN_B, GREEN_E],
            ),
            # dx=dx, #This is a parameter and is optional.
            # It's not a variable
            bounded_graph=graphLine,
        )

        print(area)

        arrow = always_redraw(
            lambda: Line(
                start=formulla1.get_corner(direction=DL),
                end=graph.get_corner(direction=DL),
            ).add_tip()
        )
        # self.play(Create(box))

        self.add(plane, axes, formulla1, num, graph, graphLine)
        self.wait()

        self.play(FadeIn(area))
        self.wait(2)

        self.play(Create(arrow))
        self.wait(2)

        self.play(Vtrack.animate.set_value(10), runtime=3, rate_func=smooth)
        self.wait(0.9)

        """
        self.play(Vtrack.animate.set_value(-10), run_time=3, rate_func=smooth)
        self.wait(0.5)"""


class laggedWrit(Scene):
    def construct(self):
        intro_title = Text("Introduction").to_corner(UP)
        Intro = (
            Tex(
                "Optimum design in civil structures like domes and vaults is a very old and ongoing research field. These structures are preferably designed to transport loads via membrane action."
            )
            .next_to(intro_title, DOWN)
            .scale(0.7)
        )
        plane = NumberPlane()

        self.play(Create(plane))
        self.wait()

        self.play(Write(intro_title, shift=DOWN))
        self.play(LaggedStart(Write(Intro), run_time=3, rat_func=there_and_back))
        self.wait()


class AntiDeriv(Scene):
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

        Vtrack = ValueTracker(0)  # Don't name it VT, you'll get an ERROR

        def func(c):
            function = lambda x: 0.1 * (x - 4) * (x - 1) * (x + 3) + c
            # if you get this error: TypeError: 'tuple' object is not callable.
            # Then it's because "comma," has been put it accidentally.
            return function

        formulla1 = Tex("\[f(x)=\sqrt{5x}\]", color=WHITE).scale(0.7).to_corner(UL)
        # Label for the variable Vtrack
        num = always_redraw(
            lambda: DecimalNumber(include_sign=True)
            .set_value(Vtrack.get_value())
            .next_to(
                formulla1, RIGHT
            )  # I want Vtrack to be a decimal number instead, so set k as is but before
        )
        graph = always_redraw(
            lambda: axes.plot(func(Vtrack.get_value()), x_range=[0, 5], color=YELLOW)
        )

        # If you get this ERROR: TypeError: get_value() takes 1 positional argument but 2 were given: that's because you wrote get_value(2)
        # it should be blank because it will auto get the value from k.

        graphLine = axes.plot(lambda x: x, x_range=[0, 7], color=WHITE)
        # graphLine2 = axes.plot(lambda x: 3*x, x_range=[-10,10], color=GREEN)

        # Vtrack_label= always_redraw(lambda: Text("The value of C is: C="))
        area = always_redraw(
            lambda: axes.get_area(
                graph=graph,
                x_range=[0, 5],
                # stroke_width=0.1,
                color=[GREEN_B, GREEN_E],
            ),
            # dx=dx, #This is a parameter and is optional.
            # It's not a variable
            bounded_graph=graphLine,
        )

        print(area)

        arrow = always_redraw(
            lambda: Line(
                start=formulla1.get_corner(direction=DL),
                end=graph.get_corner(direction=DL),
            ).add_tip()
        )
        # self.play(Create(box))

        self.add(plane, axes, formulla1, num, graph, graphLine)
        self.wait()

        self.play(FadeIn(area))
        self.wait(2)

        self.play(Create(arrow))
        self.wait(2)

        self.play(Vtrack.animate.set_value(10), runtime=3, rate_func=smooth)
        self.wait(0.9)

        """
        self.play(Vtrack.animate.set_value(-10), run_time=3, rate_func=smooth)
        self.wait(0.5)"""


class GetAreaExample(Scene):
    def construct(self):
        ax = Axes(y_range=[0, 6]).add_coordinates()
        curve1 = ax.plot(lambda x: x, x_range=[0, 5], color=DARK_BLUE)

        curve3 = ax.plot(lambda x: -x, x_range=[-5, 0], color=WHITE)

        Vtrack = ValueTracker(4.9)

        curve2 = always_redraw(
            lambda: ax.plot(
                lambda x: Vtrack.get_value() * x + Vtrack.get_value(),
                x_range=[-5, 5],
                color=YELLOW,
            )
        )
        # If you get this error:TypeError: <lambda>() takes 0 positional arguments but 1 was given,
        # means that you're saying that lambda should in function of nothing rather than x.

        area2 = always_redraw(
            lambda: ax.get_area(
                curve1,
                x_range=[0, 5],
                color=(GREEN),
                opacity=1,
                bounded_graph=curve2,
            )
        )
        area3 = always_redraw(
            lambda: ax.get_area(
                curve3,
                x_range=[-5, 0],
                color=(RED),
                opacity=1,
                bounded_graph=curve2,
            )
        )
        self.add(ax, curve1, curve2, curve3, area2, area3)

        """for i in 
                      #Doesn't work
                            self.play(Vtrack.animate.set_value(-5), run_time=5, rate_func=rush_into) #If you set a runtime to a value but you get 1s 
                            #duration then you're writting runtime instead of run_time.
                            #run_time is True.
                            self.wait(0.9)
                    else:
                        self.play(FadeToColor(area3,"#012369"))"""

        self.wait(1)

        """self.play(ApplyWave(area3), run_time=2, rate_func=rush_into)
                    self.wait(0.5)"""


"""
                    self.play(Vtrack.animate.set_value(0), run_time=5) #If you set a runtime to a value but you get 1s 
                    #duration then you're writting runtime instead of run_time.
                    #run_time is True.
                    self.wait(0.9)"""

# Using updaters:
class update1(Scene):
    def construct(self):

        rec = RoundedRectangle(
            stroke_width=8, stroke_color=WHITE, fill_color=BLUE, width=4.5, height=2
        ).shift(UP * 3 + LEFT * 4)
        math = (
            MathTex("\\frac{3}{4} =0.75")
            .set_color_by_gradient(GREEN, PINK)
            .set_height(1.5)
        )
        math.move_to(rec.get_center())
        math.add_updater(lambda x: x.move_to(rec.get_center()))  # take the coords of
        # center of rec and gives it to x then assign it as an add_updater to math Mobj.

        self.play(Write(rec))
        self.play(FadeIn(math))
        self.play(math.animate.shift(DR))
        self.wait()
        self.play(Rotate(math, PI, X_AXIS, (0, 0, 0)))
        math.clear_updaters()  # clear all updater assigned to the math Mobj
        self.play(rec.animate.shift(UL))


class updater2(Scene):
    def construct(self):
        r = ValueTracker(1)
        cir = always_redraw(lambda: Circle(2.6 * r.get_value(), RED))
        self.play(Create(cir))
        line = always_redraw(
            lambda: Line(cir.get_center(), cir.get_bottom(), 0, stroke_width=3)
        )
        self.play(DrawBorderThenFill(line))
        tri = always_redraw(
            lambda: Polygon(cir.get_top(), cir.get_left(), cir.get_right())
        )
        self.play(DrawBorderThenFill(tri))
        lined = always_redraw(
            lambda: Line(stroke_color=BLUE, stroke_width=2)
            .next_to(cir, DOWN, 0.2)
            .set_length(6 * r.get_value())
        )
        # I can write set_length(6*len(line)) not 6*line => ERROR
        self.play(ReplacementTransform(cir.copy(), lined))
        self.play(r.animate.set_value(0.3), run_time=3)

        self.wait()


# 2D graphs
class tuto2(Scene):
    def construct(self):
        plane = NumberPlane()
        self.play(Create(plane))
        axes = (
            Axes(
                x_range=[0, 5, 1],
                y_range=[0, 3, 1],
                x_length=5,
                y_length=3,
                color=YELLOW,
                axis_config={
                    "include_tip": True,
                    "numbers_to_exclude": [0],
                },
            )
            .add_coordinates()
            .to_edge(2 * UR)
        )
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(
            lambda x: x ** 0.5, x_range=[0, 4], color=GREEN
        )  # How to edit the width
        grouping = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.wait()
        self.play(grouping.animate.shift(3 * DOWN))
        self.wait()
        self.play(graph.animate.shift(6 * LEFT))


class drawOnPlane(Scene):
    def construct(self):
        plane1 = NumberPlane()  # Just to notice the amount of shift which is 3
        plane = (
            NumberPlane(x_range=[-6, 6], y_range=[-6, 6], x_length=5, y_length=5)
            .add_coordinates()
            .shift(3 * RIGHT)
            .set_color_by_gradient(BLUE, GRAY)
        )
        graph = plane.plot(
            lambda x: 0.1 * (x - 5) * x * (x + 5), x_range=[-6, 6], color=RED_C
        )  # If you write 0.5*x*(x-5)*(x+5), you'll get an ERROR
        # because of (x) and not x
        # Label of func
        graph_label = MathTex("f(x)=0.5x(x-5)(x+5)").next_to(plane, UP, buff=0.3)

        area = plane.get_area(graph, x_range=[-5, 5])

        # coords_to_point from the plane and not graph. /!\
        hz_line = Line(
            start=plane.coords_to_point(0, graph.underlying_function(-2)),
            end=plane.coords_to_point(-2, graph.underlying_function(-2)),
            stroke_width=5,
        )

        self.add(plane1)
        self.play(DrawBorderThenFill(plane))
        self.wait()
        self.play(Create(graph), Create(graph_label))
        self.play(DrawBorderThenFill(area))
        self.wait()
        self.play(DrawBorderThenFill(hz_line))


class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2, 2, 0), color=RED)

        self.add(plane, dot_scene, ax, dot_axes, lines)


#   Multiple axes tuto


class MultiAxes(Scene):
    def construct(self):
        plane1 = NumberPlane().set_opacity(
            0.4
        )  # Just to notice the amount of shift which is 3
        plane2 = (
            NumberPlane(x_range=[-4, 4], y_range=[0, 20, 5], x_length=8, y_length=5)
            .add_coordinates()
            .scale(0.4)
            .shift(3 * LEFT + 2 * DOWN)
        )

        graph = plane2.plot(lambda x: x ** 2, x_range=[-4, 4], color=YELLOW)

        axes = Axes(
            x_range=[-4, 4], x_length=8, y_range=[-20, 20, 5], y_length=10
        ).add_coordinates()
        axes.next_to(plane2, RIGHT, buff=2).scale(0.4)
        # next to should be in a new line. /!\

        graph_ax = axes.plot(lambda x: 2 * x, color=YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(
            graph_ax, x_range=[-3, 3], num_lines=12
        )
        graph_label = (
            MathTex("f(x)=x^2")
            .next_to(plane2, UP, buff=0.3)
            .set_color_by_gradient(WHITE, YELLOW)
        )

        # coords_to_point from the plane and not graph. /!\
        hz_line = Line(
            start=plane2.coords_to_point(0, graph.underlying_function(-2)),
            end=plane2.coords_to_point(-2, graph.underlying_function(-2)),
            stroke_width=10,
        )

        self.add(plane1)
        self.play(Create(plane2), Create(axes))
        self.wait()
        self.play(Create(graph), Create(graph_label), Create(graph_ax), run_time=4)
        self.play(Create(hz_line), Create(v_lines))
        self.wait()


#   Polar plane
class PolPlane(Scene):  # Don't name it PolarPlane(Scene) it's already a predifiended
    def construct(self):
        #   We can make it without ValueTracker
        # for animating dots, we should add a ValueTracker. else it won't work.
        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT * 2)
        graph1 = ParametricFunction(
            lambda t: plane.polar_to_point(2 * np.sin(3 * t), t),  # (r,theta)
            t_range=[0, PI],
            color=GREEN,
        )
        dot1 = always_redraw(
            lambda: Dot(fill_color=GREEN, fill_opacity=0.8)
            .scale(0.9)
            .move_to(graph1.get_end())
        )

        axes = Axes(
            x_range=[0, 4, 1], x_length=3, y_range=[-3, 3, 1], y_length=3
        ).shift(RIGHT * 4)
        axes.add_coordinates()
        graph2 = axes.plot(lambda x: 2 * np.sin(3 * x), x_range=[0, PI], color=GREEN)

        dot2 = always_redraw(
            lambda: Dot(fill_color=GREEN, fill_opacity=0.8)
            .scale(0.5)
            .move_to(graph2.get_end())
        )

        title = MathTex("f(\\theta) = 2sin(3\\theta)", color=GREEN).next_to(
            axes, UP, buff=0.2
        )

        self.play(
            LaggedStart(
                Write(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5
            )
        )

        self.play(
            Create(graph1),
            Create(dot1),
            Create(dot2),
            Create(graph2),
            run_time=10,
            rate_func=linear,
        )

        self.wait()


# Vectors and Matrices. from VECTORSCENE
class Vecto(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW)

        base_vectors = self.get_basis_vectors()
        self.add(base_vectors)
        self.vector_to_coords(vector=vector)

        vector2 = self.add_vector([2, 2])
        self.write_vector_coordinates(vector=vector2)


#       LinearTransformationScene
class Matrix(LinearTransformationScene):
    def __init__(self):  #   Should be added in the beginning.
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
        )
        # ....
        # ...
        # ...
        # ...


# Or we can use the Scene class instead of VectorScene or LinearTransformationScene
class vecTors(Scene):
    def construct(self):
        plane1 = NumberPlane(x_range=[-5, 5], y_range=[-4, 4]).add_coordinates()
        plane1.scale(0.8)  # Auto at the center
        self.play(Write(plane1))
        vect_v = Line(
            plane1.coords_to_point(0, 0), plane1.coords_to_point(3, 2), color=YELLOW
        ).add_tip()
        v_label = MathTex("\\vec{w}", color=YELLOW).next_to(vect_v, RIGHT, buff=0.4)

        self.play(GrowFromPoint(vect_v, vect_v.get_start()), Write(v_label))

        vect_w = Line(
            plane1.coords_to_point(0, 0), plane1.coords_to_point(-2, 1), color=RED_C
        ).add_tip()
        w_label = MathTex("\\vec{w}", color=RED_C).next_to(vect_w, LEFT, buff=0.4)
        notall = VGroup(vect_w, w_label)
        self.play(GrowFromPoint(vect_w, vect_w.get_start()), Write(w_label))

        vect_vw = Line(
            plane1.coords_to_point(0, 0), plane1.coords_to_point(1, 3), color=YELLOW
        )
        vect_vw.add_tip().set_color_by_gradient(YELLOW, RED_C)
        vw_label = MathTex("\\vec{v} + \\vec{w}").next_to(vect_vw, LEFT)
        vw_label.set_color_by_gradient(YELLOW, RED_C)

        everything = VGroup(plane1, vect_v, v_label, vect_w, w_label, vect_vw, vw_label)

        self.play(notall.animate.shift(vect_v.get_end()))
        round_rec = RoundedRectangle(height=3, width=5).to_edge(DL)
        round_rec.set_color_by_gradient(PINK, RED)
        self.add(round_rec)
        self.play(GrowFromPoint(vect_vw, vect_v.get_start()), Write(vw_label))
        self.play(everything.animate.scale(0.2).move_to(round_rec.get_center()))


# 3D Graphing
# Camera movements
class graphMove(ThreeDScene):
    def construct(self):
        threeDAx = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        graph2d = threeDAx.plot(lambda x: x ** 2, x_range=[-2, 2, 1], color=YELLOW)
        rect = threeDAx.get_riemann_rectangles(
            graph2d, x_range=[-2, 2], dx=0.1, stroke_color=BLUE_B
        )

        graph3d = threeDAx.get_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2 * PI, 2 * PI],
            color=RED,
        )  # np.array([x, y, z])
        self.add(threeDAx, graph2d)
        self.wait()

        # Camera is auto set to PHI=0, and THETA = -90 (Radians)
        # so it's a 2D scene so far
        # Let's move the camera to give a 3D look

        self.move_camera(
            phi=60 * DEGREES
        )  # phi: around x(UP or DOWN movements), theta: around z(right or left movements)
        self.wait()

        self.move_camera(theta=45 * DEGREES, phi=30 * DEGREES)
        self.wait()

        self.begin_ambient_camera_rotation(
            rate=PI / 10,
            about="theta"
            # means rotate at PI/10 per second.==> speed.
        )
        self.wait()

        self.play(
            Write(graph3d), Write(rect)
        )  # play these stuff while rotating the camera.
        self.wait(0.4)

        self.stop_ambient_camera_rotation()
        self.wait()

        self.begin_ambient_camera_rotation(rate=-PI / 8, about="phi")
        self.wait(2)

        self.stop_ambient_camera_rotation()
        self.wait(0.3)


# 3D Graphing
# Demo
class threeDgraphSurface(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes(y_range=[-3, 10, 3], y_length=7).add_coordinates()
        graph = axes.plot(lambda x: x, x_range=[0, 3], color=YELLOW)
        area = axes.get_area(graph, x_range=[0, 3])

        e = ValueTracker(0)
        # Let's plot a 3D graph with surface.
        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.coords_to_point(v, v * np.cos(u), v * np.sin(u)),
                # u_min=0,       u_min and max .... are no longer available in this version
                # u_max=2*PI,
                # v_min=0,
                # v_max=3,
                u_range=[0, e.get_value()],
                v_range=[0, 3],
                checkerboard_colors=["#302145", "#789541"],
            )
        )
        threedstuff = VGroup(axes, graph, surface)
        self.add(axes, surface)  # no surface will be plotted at e=0
        self.begin_ambient_camera_rotation(rate=PI / 20, about="theta")
        self.play(LaggedStart(Create(graph), Create(area)))
        self.play(Create(surface))

        # rotation of 360 deg
        self.play(
            Rotating(area, axis=X_AXIS, angle=2 * PI, about_point=axes.c2p(0, 0, 0)),
            e.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear,
        )  # rotating and drawing the surface simultanuously
        self.stop_ambient_camera_rotation()
        self.wait(0.3)


#   Derivative tutorial


class DrivativeTuto(Scene):
    def construct(self):
        ###  In order to not complicate the code, we NEED some HELPERS:
        # We need to declare which graph/axes,function, x, width and color(optional) as arguments.

        def get_horiz_line_and_dot_to_graph(
            axes, function, x, width, color
        ):  # graph or function is the same.
            #                   /!\ Where is the self parameter here (self, axes....)????????
            hz_line = DashedLine(
                start=axes.c2p(
                    0, function.underlying_function(x)
                ),  # 0:means always parallel to x |
                # if x=x, y=0: parallel to Y_axis
                end=axes.c2p(x, function.underlying_function(x)),
                stroke_width=width,
                stroke_color=color,
                dashed_ratio=0.5,  # It can be variable also.
            )
            # this means take these coords and plot a point on the axes plane.
            dot = (
                Dot(radius=0.08)
                .set_color(color)
                .move_to(axes.c2p(x, function.underlying_function(x)))
            )
            result = VGroup()  # Emplty list of VMobjs
            result.add(hz_line, dot)
            return result

        k = ValueTracker(-3)

        # Defining Mobjs of the original function's plot (f(x))
        # length of x and y as a square 5*5
        plane = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[-8, 9, 2], y_length=5)
            .add_coordinates()
            .shift(3.5 * LEFT)
        )

        graph = plane.plot(lambda x: (1 / 3) * x ** 3, x_range=[-3, 3], color=RED)

        graph_label = MathTex("f(x) = \\frac{1}{3} {x}^{3}").next_to(
            plane, UP, buff=0.2
        )  # ,tex_to_color_map="#842258" didn't work
        graph_label.set_color("#842258")

        graph_slope = always_redraw(
            lambda:
            # /!\ always call the plane NOT the graph when you want to plot something. graph.get_sec... NOT graph.get_..
            plane.get_secant_slope_group(
                x=k.get_value(),
                graph=graph,
                dx=0.05,
                # include_secant_line=False,
                # if we set dx=1 for example, we will have additional vertical+hz lines
                secant_line_length=4,
                secant_line_color=YELLOW,
            )
            #  dx= is the difference between to consecutive points, for dx=0.05: no much difference
        )

        # dot = get_horiz_line_and_dot_to_graph(plane,graph, graph, k.get_value(), 0, color)

        """dot = always_redraw(lambda: 
            Dot(radius=0.08).move_to(plane.c2p(k.get_value(),graph.underlying_function(k.get_value())))
        )"""

        box = Rectangle(YELLOW, height=5, width=5).shift(3.5 * LEFT)

        # Defining Mobjs of the derivative function's plot (f'(x))
        # control the scale with length of x and y as a square 5*5 rather than .scale()
        plane2 = (
            NumberPlane(x_range=[-3, 4, 1], x_length=5, y_range=[0, 11, 2], y_length=5)
            .add_coordinates()
            .shift(3.5 * RIGHT)
        )

        graph2 = always_redraw(
            lambda: plane2.plot(
                lambda x: x ** 2,
                x_range=[-3, k.get_value()],
                color=RED,  # for plotting in real_time
            )
        )

        graph2_label = MathTex("f'(x) = {x}^{2}").next_to(
            plane2, UP, buff=0.2
        )  # ,tex_to_color_map="#842258" didn't work
        graph2_label.set_color("#842258")
        graph2_hzline = always_redraw(
            lambda:
            # /!\ always call the plane NOT the graph when you want to plot something. graph.get_sec... NOT graph.get_..
            get_horiz_line_and_dot_to_graph(
                axes=plane2, function=graph2, x=k.get_value(), width=2, color=WHITE
            )
            #  dx= is the difference between to consecutive points, for dx=0.05: no much difference
        )

        # dot = get_horiz_line_and_dot_to_graph(plane,graph, graph, k.get_value(), 0, color)

        dot = always_redraw(
            lambda: Dot(radius=0.08).move_to(
                plane.c2p(k.get_value(), graph.underlying_function(k.get_value()))
            )
        )

        ##---- Adding the slope value tracker Label.
        ## Lets create a point variable for the slope
        """slope_point= plane.c2p(k.get_value(),graph.underlying_function(k.get_value()))
        slope_value_text = always_redraw( lambda:
            Tex("Slope value: ").move_to(slope_point)
        )"""  ###--------- /!\ We couldn't write this, everything should be inside the alwas_redraw function.

        slope_value_text = always_redraw(
            lambda: Tex("Slope value: ").move_to(
                plane.c2p(k.get_value(), graph.underlying_function(k.get_value()))
            )
        )
        # slope_value_text.set_width(1) # Has been deprecated
        slope_value_text.set_color_by_gradient([RED_E, GRAY_BROWN])

        slope_value_num = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(k.get_value())
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color_by_gradient([YELLOW, GRAY_BROWN])
        ).add_background_rectangle()  # /!\ What happens if we don't add this method???.

        # Playing the animations:

        # /! My note\ laggedStart is better when you want to animate everything but one by one with a lag ratio
        self.play(
            LaggedStart(
                Write(box),
                Write(plane),
                Write(plane2),
                Create(graph),
                Write(graph_label),
                Create(graph2),  # At the first k value=-3, nothing will happen
                Write(graph2_label),
                run_time=5,
                lag_ratio=0.5,
            )
        )
        self.wait(0.3)
        self.add(graph2_hzline, slope_value_text, slope_value_num, dot, graph_slope)
        #  We then need to change the value of k by animation
        self.play(k.animate.set_value(3), run_time=16, rate_func=linear)
        self.wait(0.2)


# Additive_function


class additivFunc(Scene):
    def construct(self):

        axes = Axes(
            x_range=[0, 2.1, 1],
            y_range=[0, 7, 2],
            tips=True,
        ).add_coordinates()

        func1 = axes.plot(lambda x: x ** 2, x_range=[0, 2], color=YELLOW)
        func1_label = MathTex("y = {x}^{2}").scale(0.8).next_to(func1.get_end())

        func2 = axes.plot(lambda x: x, x_range=[0, 2], color=GREEN)
        func2_label = MathTex("y = {x}").scale(0.8).next_to(func2.get_end())

        func3 = axes.plot(lambda x: x ** 2 + x, x_range=[0, 2], color=PINK)
        func3_label = MathTex("y = {x}^{2}+{x}").scale(0.8).next_to(func3.get_end())

        self.add(axes, func1, func2, func3, func1_label, func2_label, func3_label)

        for k in np.arange(0, 2.1, 0.2):  # if you write np.arange()
            V_Line1 = DashedLine(
                start=axes.c2p(k, 0),  # It should be a point, not just "k".
                end=axes.c2p(k, func1.underlying_function(k)),
                dashed_ratio=0.4,
                color=YELLOW,
            )

            V_Line2 = DashedLine(
                start=axes.c2p(k, 0),  # It should be a point, not just "k".
                end=axes.c2p(k, func2.underlying_function(k)),
                dashed_ratio=0.4,
                color=GREEN,
            )
            V_Line3 = Line(
                start=axes.c2p(k, 0),  # It should be a point, not just "k".
                end=axes.c2p(k, func3.underlying_function(k)),
                color=PINK,
            )
            #   Create Line 1 and 2 anyway.
            self.play(Create(V_Line1))
            self.play(Create(V_Line2))

            # For the ploting of Line 3:

            if len(V_Line1) < len(V_Line2):
                self.play(
                    V_Line2.animate.shift(UP * V_Line1.get_length())
                )  # Line 1 is less than Line 2, so we need
                # to shift it up by line 1 because line1+2=3
            else:
                self.play(
                    V_Line1.animate.shift(UP * V_Line2.get_length())
                )  # Line 1 is greater than Line 2, so no need to draw Line2
                # Just draw draw a dashed line for func3=line3
            self.play(Create(V_Line3))  # Line to be always drawn
            self.wait(0.3)

            # Area
        area1 = axes.get_riemann_rectangles(
            func1, x_range=[0, 2], dx=0.1, stroke_color=[YELLOW, GREEN]
        )
        self.play(Create(area1), run_time=5)
        self.wait(0.5)
        self.play(area1.animate.set_opacity(0.4))

        area2 = axes.get_riemann_rectangles(
            func2, x_range=[0, 2], dx=0.1, stroke_color=[YELLOW, RED_C]
        )
        self.play(Create(area2), run_time=5)
        self.wait(0.5)

        for c in np.arange(0, 20, 1):  # simillar to from 0 to 2 with 0.1 step
            # But we need to access the list of area[] by indexes so we can't write area[0.2]...
            self.play(
                area2[c].animate.shift(UP * area1[c].get_height()),
                run_time=1,
            )


# ArcLength Scene ==> >80% is True
class ArcLen(Scene):
    def construct(self):
        axes = (
            Axes(
                x_range=[-1, 4.2],
                y_range=[0, 3.2],
                x_length=8,
                y_length=6,
            )
            .add_coordinates()
            .shift(LEFT * 3)
        )

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # axes figure box:
        box = Rectangle(RED, height=6, width=8).move_to(axes.get_center())

        # Plotting the graph
        graph = axes.plot(
            lambda x: 0.1 * x * (x + 1) * (x - 3) + 1,
            x_range=[-1, 4],
            stroke_color=BLUE_B,
        )

        k = ValueTracker(1)  # distance as a value tracker.

        # Drawing the dx line
        dx_line = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(2, graph.underlying_function(2)),
                end=axes.c2p(2 + k.get_value(), graph.underlying_function(2)),
                stroke_color=GREEN,
            )
        ).set(width=0.4)
        # dx Bracket length
        dx_length = always_redraw(
            lambda: Brace(dx_line, DOWN, buff=0.1).next_to(dx_line, DOWN, buff=0.1)
        )
        # dx label
        dx_label = always_redraw(lambda: Tex("dx").next_to(dx_length, DOWN, buff=0.1))

        # Drawing the dy line
        dy_line = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(
                    2 + k.get_value(), graph.underlying_function(2 + k.get_value())
                ),
                end=axes.c2p(2 + k.get_value(), graph.underlying_function(2)),
                stroke_color=GREEN,
            )
        )
        # dy Bracket length
        dy_length = always_redraw(
            lambda: Brace(dy_line, RIGHT, buff=0.1).next_to(dy_line, RIGHT, buff=0.1)
        )
        # dy label
        dy_label = always_redraw(lambda: Tex("dy").next_to(dy_length, RIGHT, buff=0.1))

        # Drawing the dL line
        # First, let's calculate its length
        # dL_value= np.sqrt((dx_line.get_length())**2 + (dy_line.get_length())**2)
        dL_line = always_redraw(
            lambda: Line(
                start=axes.c2p(2, graph.underlying_function(2)),
                end=axes.c2p(
                    2 + k.get_value(), graph.underlying_function(2 + k.get_value())
                ),
                stroke_color=GREEN,
            )
        ).set(width=0.4)
        # dL Bracket length
        # In case of inclined line, we use BraceBetweenPoints istead of Brace.
        dL_length = always_redraw(
            lambda: BraceBetweenPoints(
                point_1=dL_line.get_end(), point_2=dL_line.get_start()
            )
        ).next_to(dL_line, UP, buff=0.1)
        # Don't put direction as=UP/Down, refer to the definition.
        # We can remove .next_to(dL_line, UP,buff=0.1)  because we're already calling an updater by dL_line.get_end()
        # dL label
        dL_label = always_redraw(lambda: Tex("dL").next_to(dL_length, UP, buff=0.2))

        self.add(axes, graph)
        self.wait()

        # integr = VGroup(dx_length, dy_length, dL_length, dx_label,dy_label,dL_label)
        """self.play(
            LaggedStart(
                Create(integr),
                k.animate.set_value(3),
                run_time=3,
                lag_ratio=0.4,
            )
        )
        self.wait(2)"""

        """self.play(
            Create(dx_line),
            
            Create(dy_line),
            
            Create(dL_line),
        )
        self.add(dx_length, dx_label,dy_length, dy_label,dL_length, dL_label)

        self.wait(1)

        self.play(k.animate.set_value(0.5), run_time=10, rate_func=linear)
        self.wait(0.3)"""

        # Drawing integral lines that make the graph
        # For simplicity , we define a function:
        def integral_line_func(
            plane, graph, dx=1, line_width=1, line_color=YELLOW, x_min=None, x_max=None
        ):
            # A list of dots
            dots = VGroup()
            # A list of lines
            lines = VGroup()
            result = VGroup(dots, lines)

            # The range of the graph
            x_range = np.arange(x_min, x_max, dx)  # arange() because it can be float.
            # color of dots
            colors = color_gradient([YELLOW, BLUE_E], len(x_range))

            # Explanation: for valueTr=1=dx, for x in x_range(-1,0,1,2,3,4),
            # it makes dots(p1,p2), dots(p1,p2;p1,p2)...

            for x, color in zip(x_range, colors):
                # To draw a line we need a 2 points:
                # dots:
                p1 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x, graph))
                # we need to provide the move_to() with coords and not point.
                # /!\ p2 is at (x+dx) not like p1(x)
                p2 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x + dx, graph))

                dots.add(p1, p2)
                # colors.append(color)
                dots.set_fill(colors, opacity=0.8)

                # Now we can draw lines at the same time of creating 2 dots.
                line = Line(
                    p1.get_center(),
                    p2.get_center(),
                    stroke_color=line_color,
                    stroke_width=line_width,
                )
                lines.add(
                    line
                )  # Add() is a method of manim only to turn a mob to a submoj
                # the first time (valueTracker=1=dx) will produce 5 lines.
                # for dx=0.5 ==> len(x_range)=10 ==> 10 lines
                # .....dx=1==>(-1,0,...)=>(line,line...)
                if dx < 0.7:
                    lines.set_opacity(0.3),
                else:
                    lines.set_opacity(1),
                    # We can write pass also.
            return result
            # We can't do this:
            # return dots, lines

        # Let's animate
        dx_changer = ValueTracker(1)
        line_intergral = always_redraw(
            lambda: integral_line_func(
                plane=axes,
                graph=graph,
                dx=dx_changer.get_value(),
                line_width=5,
                line_color=WHITE,
                x_max=4,
                x_min=-1,
            )
        )
        self.play(Create(line_intergral))
        self.play(dx_changer.animate.set_value(0.5), run_time=5, rate_func=rush_from)
        self.wait(1)

        num = always_redraw(
            lambda: DecimalNumber(include_sign=True)
            .set_value(Vtrack.get_value())
            .next_to(formulla1, RIGHT, buff=0)
            .scale(0.7)
        )
        mydic = {"fjdl": 52, "ff": 52, "rfd": 52}
