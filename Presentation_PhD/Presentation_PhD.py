from manim import *
import random as rd


def make_component(text, color=YELLOW, scale=0.7):
    # geometry is first index, TextMob is second index
    text_mob = Tex(text).scale(scale)
    rect = Rectangle(color=color, height=1.1, width=2.3)
    return VGroup(rect, text_mob)


class Intro(MovingCameraScene):
    def construct(self):
        plan = NumberPlane()
        intro = Text(r"Introduction", stroke_width=0.3, color="#189651")
        bg = Rectangle(
            fill_opacity=1, fill_color=BLACK, stroke_color="#ff073a"
        ).round_corners(0.8)
        bg.to_corner(UL, buff=0)
        title = Title("Shear walls explained").to_edge(UP, buff=0.2)
        # bg.add_updater(lambda mobj: mobj.round_corners().surround(intro))
        def update_function(mobj):
            mobj.move_to(bg.get_center())

        self.add(plan, bg)  # Order matter, else you won't see the text
        intro.add_updater(update_function)
        self.play(Write(intro), rate_func=smooth)
        self.wait()
        self.play(ApplyWave(bg))
        self.wait(0.4)
        self.play(ReplacementTransform(bg, title), FadeOut(intro), rate_func=linear)
        self.wait()
        # Moving the camera:
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=title.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))

        lecture_component = make_component("Lecture")
        examples_component = make_component("Examples", color=ORANGE)
        homework_component = make_component("Homework", color=RED)
        exam_component = make_component("Exam", color=PURE_GREEN)
        forget_component = make_component("Forget", color=BLUE)

        first_encounter_components = VGroup(
            lecture_component,
            examples_component,
            homework_component,
            exam_component,
            forget_component,
        ).arrange(DOWN * 2)

        first_encounter_components.next_to(title, DOWN)

        for component in first_encounter_components:
            self.play(Create(component[0]), Write(component[1]))
            self.wait()
        self.play(
            AnimationGroup(
                *[
                    component.animate.shift(LEFT * 5)
                    for component in first_encounter_components
                ],
                lag_ratio=0.05
            )
        )
        self.wait(0.4)
        self.play(first_encounter_components[1:].animate.set_opacity(0.3))
        self.wait(0.4)


class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))
        np.arange(-10, 10.01, 2),


class JustifyText(Scene):
    def construct(self):
        self.camera.background_color = BLUE

        intro_title = Title("Introduction")
        self.add(intro_title)

        Int_1 = (
            "\tIn high-seismicity countries, buildings must be designed to resist"  # from In to resist is max char
            " seismic loading. It’s well know that RC shear walls represent a structurally"  # smartly stoped at efficient
            " efficient system to stiffen an RC building under those loads."
        )
        Int_2 = (
            "\tIn general, a shear wall system consists of a combination of shear walls and frames"
            " because this type of systems normally provide the required stiffness and strength"
            " to withstand lateral loads in medium-high and even low rise buildings."
        )

        intro_1 = (
            MarkupText(
                Int_1,
                font_size=60,
                unpack_groups=0,
                font="LM Roman 12",
                line_spacing=1.8,
                disable_ligatures=1,
                justify=1,  # : that is only available in MarkupText
            )
            .scale(0.4)
            .next_to(intro_title, DOWN, buff=0.5)
        )

        intro_2 = (
            MarkupText(
                Int_2,
                font_size=60,
                unpack_groups=0,
                font="LM Roman 12",
                line_spacing=1.8,
                disable_ligatures=1,
                justify=1,  # : that is only available in MarkupText
            )
            .scale(0.4)
            .next_to(intro_1, DOWN)
        )

        self.play(
            LaggedStart(Write(intro_1), Write(intro_2), lag_ratio=1),
            run_time=2,
        )
        self.wait(0.4)

        self.play(
            Create(SurroundingRectangle(intro_2[1][0:10], color=RED)),
            Create(
                SurroundingRectangle(intro_2[1][13:19]), color=RED
            ),  # 's' of frames is included
            run_time=2,
            rate_func=there_and_back_with_pause,
        )
        #
        self.wait(0.4)

        shw = intro_2[1][0:10].copy()
        fr = intro_2[1][13:19].copy()
        self.play(
            shw.animate.to_edge(UR, buff=1.5),
            fr.animate.next_to(intro_title, DOWN),
            Unwrite(intro_2),
            Unwrite(intro_1),
            run_time=4,
        )
        self.wait(1)

        self.play(Indicate(fr, 3), shw.animate.set_opacity(0.2))
        self.wait(0.5)

        frame_definition = (
            MarkupText(
                "A frame is an inter-\nconnection between \nvertical columns and \nhorizontal beams that \n"
                "bends predominantly \nin a shear mode deformation.",
                font_size=60,
                font="LM Roman 12",
                justify=1,
            )
            .scale(0.4)
            .align_on_border(LEFT)
        )

        L_column = Line().set_style(stroke_width=10).rotate(PI * 0.5)
        R_column = L_column.copy().shift(RIGHT * 3)
        roof = always_redraw(
            lambda: Line(start=L_column.get_end(), end=R_column.get_end())
        )
        load = always_redraw(
            lambda: Arrow(
                start=roof.get_start() - [1, 0, 0], end=roof.get_start(), buff=0
                # Try -[rd.uniform(0.3,1.6), 0, 0]
            )
        )
        shearwall = Rectangle(
            fill_color=BLUE,
            fill_opacity=1,
            height=L_column.get_length(),
            width=roof.get_length() * 0.6,
        )
        shearwall.set_color_by_gradient(GREY_C).scale(0.6)
        frame = VGroup(L_column, R_column, roof, load).scale(0.6)  # , shearwall
        # frames = frame.copy()
        storey_4 = always_redraw(
            lambda: VGroup(*[frame.copy() for _ in range(4)])
            .arrange(UP, buff=-0.1)
            .next_to(
                fr, DOWN, buff=0.4
            )  # Force buffer to be 0 even in the presence of arrow tips.
        )

        # storey_4[0].add(fix1,fix1) # just put them inside ( , ), not in a list like that []

        loads = VGroup()
        for element in storey_4:
            if element == storey_4[0]:
                self.play(
                    Create(element[:-1]), Write(frame_definition), run_time=3
                )  # shear walls and loads are not included (-1, -2)
                # here add support for the first storey
            else:
                self.play(Create(element[:-1]))
            loads.add(element[3])
        # shearwalls.add(element[4])
        self.wait()

        self.play(FadeIn(loads, shift=RIGHT * 7, scale=2))
        self.wait(0.05)

        self.play(
            storey_4.animate(run_time=2)
            .apply_function(  # /!\shear walls should not be included in this deformation
                # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                lambda p: p
                + np.array([np.sin(p[1]), 0, 0])
            )
            .set_color([RED, YELLOW, RED]),
        )
        self.wait(0.3)

        self.play(Unwrite(frame_definition))
        self.wait()
        self.play(fr.animate.set_opacity(0.3).to_edge(LEFT))
        storey_4.set_opacity(0.3)
        self.wait()

        shearwalls = VGroup()
        for i in range(4):
            shearwalls.add(shearwall.copy())
            print(shearwalls)

        shearwalls.arrange(UP, buff=0).next_to(shw, DOWN, buff=0.6)
        shw.set_opacity(1)

        self.play(Indicate(shw, 3))

        self.wait(0.5)

        # self.add(Rectangle(height=1, width=3, fill_color=GREY, fill_opacity=1).next_to(shearwalls[0], DOWN, buff=0))

        for element in shearwalls:
            self.play(
                Create(element)
            )  # shear walls and loads are not included (-1, -2)
        self.wait(1)
        shearwall_definition = (
            MarkupText(
                "Shear walls are vertical elements \nof the horizontal force"
                " resisting \nsystem. \nShear walls deflects predominantly \nin a "
                "bending mode deformation \nlike a cantilever, as illustrated "
                "in \nthe following animation.",
                font_size=60,
                font="LM Roman 12",
                justify=1,
            )
            .scale(0.4)
            .next_to(shearwalls, LEFT, buff=1)
        )

        self.play(Write(shearwall_definition))
        self.wait(0.5)
        self.play(loads.animate.next_to(shearwalls, LEFT, buff=0).shift(UP * 0.58))
        self.wait()

        interactions = VGroup()
        # for jf, fd in zip(range(4), [1, 0.6, 0.3, 0.15])
        inter1 = always_redraw(
            lambda: Arrow(
                start=storey_4[0][3].get_corner(UL),
                end=storey_4[0][1].get_end(),
                color=RED_B,
                buff=0,
            )
        )
        # self.add(inter1)
        # self.play(shearwalls.animate(run_time = 2).shift(RIGHT*3))
        # self.wait() #Always end with wait
        #


class Bibliography(ZoomedScene):
    def __init__(self, **kwargs):   #HEREFROM
        ZoomedScene.__init__( 
            self, 
            zoom_factor=0.5, # the scale of the frame = the scale of the vision.
            zoomed_display_height=3, # height of the frame
            zoomed_display_width=6,  # width of the frame
            image_frame_stroke_width=1,  # stroke of the image frame
            zoomed_camera_config={  
                "default_frame_stroke_width": 3,  
            },  
            **kwargs  
        )      
    def construct(self):
        # self.camera.background_image = 'C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png'
        # self.camera.init_background()
        # self.camera.background_color = GREY
        self.add(
            ImageMobject(
                "C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png"
            ).set_opacity(0.4).scale(0.5)
        )
        png_path = "C:/Manim_3_feb/manim/Presentation_PhD/simp_python.png"
        self.camera.background_color = WHITE

        biblio_title = Title("Bibliography", color=RED).to_edge(UP, buff=0)
        my_name = Text('N.DJAFAR HENNI', font_size=20, color=RED).to_edge(DL, buff=0)
        self.add(my_name)

        simp = (
            r"(Zakian &amp; Kaveh, 2020) developed a topology optimization formulation based on "  # &amp; used to write &.
            "the SIMP (stands for: solid isotropic material with penalization) approach to"
            " find the stiffest structure with desirable material distribution subjected to"
            " seismic loads by investigating different types of shear walls with and"
            " without openings."
        )

        simp_mobj = (
            MarkupText(simp, font_size=60, justify=1, color=BLACK)
            .scale(0.4)
            .next_to(biblio_title, DOWN, buff=1.5)
        )
        self.play(LaggedStart(Write(biblio_title), Write(simp_mobj), lag_ratio=1))
        self.wait()

        simp_title = (
            Text("How SIMP works?", font_size=36, color=RED).to_corner(UL, buff=1)
        )
        self.play(FadeOut(simp_mobj, shift=UP), FadeIn(simp_title, shift=UP))
        self.wait()

        simp_def = (
            "The traditional approach to topology \noptimization (place, study) is the \n"
            "discretization of a domain into a grid \nof a finite elements called isotropic"
            " \nsolid microstructures."
        )

        sq = Square(0.5, fill_color=GREY, fill_opacity=0.2)
        sq_small = Square(0.2)
        shear_wall = (
            VGroup(*[sq.copy().add(Integer(i).rotate(-PI*0.5)) for i in range(1, 61)])
            .arrange_in_grid(6, 10, buff=0)
            .rotate(PI * 0.5)
        )
        sq_small_group = (
            VGroup(*[sq_small.copy().set_style(stroke_width=0.4) for _ in range(350)])
            .arrange_in_grid(14, 25, buff=0)
            .rotate(PI * 0.5)
        )
        rec = Rectangle(
            height=3, width=5, stroke_width=0, fill_color=GREY, fill_opacity=1
        ).rotate(PI * 0.5)
        SUPPORT = always_redraw(
            lambda: Rectangle(
                height=4 * 1.15,
                width=0.3,
                fill_color=GREY,
                stroke_width=0,
                fill_opacity=1,
            )
            .rotate(PI * 0.5)
            .next_to(rec, DOWN, buff=0)
        )

        load = always_redraw(
            lambda: Arrow(
                start=rec.get_corner(UL) - [1, 0, 0], end=rec.get_corner(UL), buff=0, color=BLACK
                # Try -[rd.uniform(0.3,1.6), 0, 0]
            )
        )

        shearwall_simp = (
            ImageMobject(png_path).rotate(PI * 0.5).next_to(SUPPORT, UP, buff=0)
        )
        shearwall_simp.stretch_to_fit_width(width=rec.width).stretch_to_fit_height(
            rec.height
        ).shift(UP * 0.535)

        simp_def_mobj = (
            MarkupText(
                simp_def, font_size=60, justify=1, color=BLACK,
            )
            .next_to(simp_title, DOWN, buff=0) # next_to() doesn't want to work
            .scale(0.4)
        )

        simp_def_2 = (
            "It allows Instead of a black and white \nsolution, gray by having in each ele-\n"
            "ment a density design variable that \ncan vary in [0,1]."
        )
        simp_def_mobj_2 = (
            MarkupText(
                simp_def_2, font_size=60, justify=1, color=BLACK,
            )
            .next_to(simp_def_mobj, DOWN, buff=0) # next_to() doesn't want to work
            .scale(0.4)
        )

        sw_label = Text('RC Shear wall', color=BLACK, font_size=37).next_to(SUPPORT, DOWN, buff=0.3)
        design_domain = MathTex(
            r'Design\ domain\ \Omega ', color=BLACK
        ).scale(0.7).move_to(rec.get_center())
        
        self.play(
            Write(simp_def_mobj)
        )
        self.wait()
        
        self.play(FadeIn(rec, shift=UP), FadeIn(SUPPORT, shift=UP), Write(sw_label))
        self.play(FadeIn(design_domain))
        self.wait()
        self.add(shearwall_simp.set_opacity(0))

        self.play(LaggedStart(
            Indicate(simp_def_mobj[-30:-1], color=RED),
            ReplacementTransform(simp_def_mobj[-30:-1].copy(), shear_wall[0]),
            lag_ratio=1
            )
        )
        self.play(
            AnimationGroup(*[FadeIn(i) for i in shear_wall], lag_ratio=0.1),
        )
        self.wait()
        
        self.play(Transform(shear_wall, sq_small_group))
        # self.wait()

        self.play(
            Write(simp_def_mobj_2)
        )
        self.wait()

        # Here add a text definition for colors: gray, black, white
        
        self.play(
            FadeIn(load, shift=RIGHT*5),
        )
        
        self.play(
            *[
                i.animate.set_opacity(rd.uniform(0, 1)).set_style(fill_color=BLACK)
                for i in sq_small_group
            ]
        )
        # self.wait()
        self.play(
            *[
                i.animate(run_time=3, rate_func=there_and_back)
                .set_opacity(rd.uniform(0, 1))
                .set_style(fill_color=[WHITE])
                for i in sq_small_group
            ]
        )
        # self.wait()
        self.play(
            *[
                i.animate(run_time=3, rate_func=there_and_back)
                .set_opacity(rd.uniform(0.6, 1))
                .set_style(fill_color=[BLACK])
                for i in sq_small_group
            ],
            shearwall_simp.animate.set_opacity(0.5),
        )
        self.play(
            *[
                i.animate.set_opacity(0).set_style(fill_color=[BLACK])
                for i in sq_small_group
            ],
            shearwall_simp.animate.set_opacity(1),
            run_time=3
        )
        # self.play(), run_time=2),FadeIn(shearwall_simp)

        self.activate_zooming(animate=True) # Add an initial animtaion to activate the zoom.
        self.wait()
        self.play(self.zoomed_camera.frame.animate.move_to(rec.get_center())) # Change the initial zoomed camera frame position
        # to the given position
        self.wait()
        self.play(self.zoomed_camera.frame.animate.shift(2*UP)) # The output of the zoom
        self.wait()
        '''self.play(self.camera.frame.animate.scale(1/2)) # Change the initial camera frame scale(=1)
        # to the given scale(=0.5) => shrink the frame
        self.play(self.camera.frame.animate.shift(UR*1)) # shift the camera frame to the given position
'''