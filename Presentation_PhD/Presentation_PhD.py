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
                lag_ratio=0.05,
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
        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )

        # self.camera.background_color = [WHITE]

        my_name = Text(
            "N. DJAFAR HENNI", font="ALGERIAN", font_size=27, color=RED
        ).to_edge(DL, buff=0)
        self.add(my_name)

        intro_title = Title("Introduction")
        self.add(intro_title)

        Int_1 = (
            "\tIn high-seismic countries like Algeria, buildings must be designed to resist"  # from In to resist is max char
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
            MarkupText(  # /!\ Adding a new line \n will affect the justify function./!\
                "A frame is an inter-\nconnection between \nvertical columns and \nhorizontal beams. \n\n"
                "Frames bend predominantly \nin a shear mode deformation.",
                font_size=60,
                font="LM Roman 12",
                justify=1,
                unpack_groups=0,
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
                start=roof.get_start() - [1, 0, 0],
                end=roof.get_start(),
                buff=0
                # Try -[rd.uniform(0.3,1.6), 0, 0]
            )
        )
        shearwall = Rectangle(
            fill_color=BLUE,
            fill_opacity=1,
            height=L_column.get_length(),
            width=roof.get_length(),
        )
        shearwall.set_color_by_gradient(GREY_C).scale(0.6)
        frame = VGroup(L_column, R_column, roof, load).scale(0.6)  # , shearwall
        # Add foundations for the first storey only; It should be inside the frame I think /!\
        """fond1 = Rectangle(
            fill_color=[BLUE, WHITE, BLUE],
            fill_opacity = 1,
        ).scale(0.2).next_to(L_column, DOWN, buff=0)
        fond2 = fond1.copy().scale(0.2).next_to(R_column, DOWN, buff=0)
        fond1.add_updater(lambda mob: mob.next_to(L_column, DOWN, buff=0))
        fond2.add_updater(lambda mob: mob.next_to(L_column, DOWN, buff=0))"""

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
                    # Create(fond1),
                    # Create(fond2),
                    Create(element[:-1]),
                    Write(frame_definition[:4]),
                    run_time=3,
                )  # loads are not included (-1)
                # here add support for the first storey
            else:
                self.play(Create(element[:-1]))
            loads.add(element[3])

        self.wait()

        self.play(FadeIn(loads, shift=RIGHT * 7, scale=2))
        self.wait(0.05)

        self.play(
            storey_4.animate(run_time=2, rate_func=there_and_back_with_pause)
            .apply_function(  # /!\shear walls should not be included in this deformation
                # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                lambda p: p
                + np.array([np.sin(p[1]), 0, 0])
            )
            .set_color([RED, YELLOW, RED]),
            Write(frame_definition[4:]),  # Write the rest of the text simultaneously
        )
        self.wait(0.3)

        self.play(Unwrite(frame_definition))
        self.wait()
        self.play(fr.animate.set_opacity(0.3).to_edge(LEFT))
        self.play(storey_4.animate.set_opacity(0.3))
        self.wait()

        shearwalls = VGroup()
        for i in range(4):
            shearwalls.add(shearwall.copy())
            print(shearwalls)

        sw_support = Rectangle(
            fill_color=[BLUE, WHITE, BLUE],
            fill_opacity=1,
            height=0.6,
            width=shearwall.get_width() + 0.6,
        )

        self.play(shw.animate.set_opacity(1).shift(3 * LEFT))

        self.play(Indicate(shw, 3))

        self.wait(0.5)

        # Adding updaters for support and shear walls.
        sw_support.next_to(shearwalls, DOWN, buff=0)
        sw_support.add_updater(lambda mob: mob.next_to(shearwalls, DOWN, buff=0))
        shearwalls.arrange(UP, buff=0).next_to(shw, DOWN, buff=0.6)
        shearwalls.add_updater(lambda mob: mob.next_to(shw, DOWN, buff=0.6))

        shearwall_definition = (
            MarkupText(
                "Shear walls are vertical elements \nof the horizontal force"
                " resisting \nsystem. \n\nShear walls deflects predominantly \nin a "
                "bending mode deformation \nlike a cantilever, as illustrated "
                "in \nthe following animation.",
                font_size=60,
                font="LM Roman 12",
                justify=1,
                unpack_groups=0,
            )
            .scale(0.4)
            .next_to(storey_4, RIGHT, buff=0.5)
        )

        # Write on the right of the frames.
        self.play(Write(shearwall_definition[:3]))
        self.wait(0.5)
        # Creation of the shearwall support.
        self.play(Create(sw_support))

        # Creation of the shearwall.
        for element in shearwalls:
            self.play(Create(element))
        self.wait(1)

        self.play(loads.animate.next_to(shearwalls, LEFT, buff=0).shift(UP * 0.58))
        self.wait(0.2)

        self.play(
            shearwalls.animate(
                run_time=2, rate_func=there_and_back_with_pause
            )  # (t=0.3, pause_ratio=0.8)
            .apply_function(
                # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                lambda p: p
                + np.array([np.sin(p[1]), 0, 0])
            )
            .set_color([RED, YELLOW, RED]),
            Write(
                shearwall_definition[3:]
            ),  # Write the rest of the shearwall defi simultaneously
        )
        self.wait(0.3)

        self.play(
            Unwrite(shearwall_definition),
            shw.animate.next_to(fr, RIGHT, buff=2),
            FadeOut(loads),
        )
        self.wait()
        self.play(
            AnimationGroup(
                fr.animate.set_opacity(1),
                ApplyWave(storey_4),
                Indicate(
                    Text("+").next_to(shearwalls, LEFT), 3
                ),  # next_to(storey_4, RIGHT) try to find
                # the issue later. COMPARE IT WITH SHEARWALLS BECASUE IT WORKS WITH THEM.
                ApplyWave(shearwalls),
                Indicate(Text("=").next_to(shearwalls, RIGHT), 3),
                lag_ratio=1,
            )
        )
        # Combine the two labels to transform them later
        shw_fr_group = VGroup(fr.copy(), shw.copy())
        shw_fr_label = (
            MathTex(r"\text{frame} + \text{shearwall}")
            .scale(0.7)
            .next_to(shw, RIGHT, buff=2)
        )
        self.play(TransformMatchingShapes(shw_fr_group, shw_fr_label))
        self.wait(0.4)
        # storey_4.remove_updater
        shearwalls.remove_updater(lambda mob: mob.next_to(shw, DOWN, buff=0.6))
        self.play(
            AnimationGroup(
                storey_4.animate.next_to(shw_fr_label, DOWN, buff=0.4),
                shearwalls.animate.next_to(storey_4, RIGHT, buff=0),
                loads.animate.next_to(storey_4, LEFT, buff=0),
                lag_ratio=1,
            )
        )
        """interactions = VGroup()
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
                #"""
        # Don't forget to add an earthquake-resistant system label.
        # Write this: Since their mode of deflection varies, the frame tends to restrain the shear wall in upper stories, and the shear wall tends to restrain the frame in lower stories. This reduces the
        # lateral deflection and improves the overall efficiency of the structural system.
        # --------------------- Cut to the chase --------------------


class Shearwall_Systems(Scene):
    def construct(self):
        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )

        # self.camera.background_color = [WHITE]

        my_name = Text(
            "N. DJAFAR HENNI", font="ALGERIAN", font_size=27, color=RED
        ).to_edge(DL, buff=0)
        self.add(my_name)

        intro_title = Title("Introduction").to_edge(UP, buff=0)
        self.add(intro_title)

        text = ()
        shearwall_systems1 = MarkupText(  # gravity is smth like justify
            "\tThe Algerian seismic code RPA2003 classifies multiple types of earthquake-resistant"
            " systems for the category of RC structures. We’ll only present two of"
            " them as they are the core of our study."
            "\n\n<span gravity='south' weight='bold' foreground='red' underline='single' underline_color='red'>1) Dual earthquake-resistant system insured by shear walls and frames with interaction: </span>"
            "\n\tWhen a building has both shear walls and frames to withstand lateral loads, "
            "shear walls deflect in bending mode and frames deflect in shear mode "
            "under Hz loads. Due to infinity rigidity of the floor diaphragm, the main function "
            "of this structure increases the rigidity for lateral load resistance. Shear walls and "
            "frames have the same deflection each floor, modifies the final behavior (they "
            "restrain each other each floor level) of these elements known as shear wall-"
            "frame interaction."
            "\n\tThe Algerian seismic code RPA2003 dictates as per clause 3.4.4a that for buildings "
            "with dual lateral resisting systems (shear walls + frames), and with interaction "
            "shear wall-frame, these shear walls should retain at most 20% of the vertical loads."
            "\nAnd frames should retain, beside the vertical loads, at least 25% of the story shear."
            # MathTex(equation)
            ,
            font_size=60,
            font="Times New Roman",
            justify=0,
            unpack_groups=0,
        ).scale(0.4)
        self.play(
            Write(shearwall_systems1.next_to(intro_title, DOWN, buff=0.3)), run_time=3
        )
        self.wait()
        equations = MathTex(  # From [0] to [7]
            # Equation 1 and its definition
            r"\bf{\frac{\sum F_{\text {frame }}}{\sum F_{\text {frame }}+\sum F_{\text {shearwall }}} \leq 20 \%}"
            r"\text{: Percentage of loads retained by shear walls.}\\",
            # Equation 2 and its definition
            r"\frac{\sum F_{\text {frame }}}{\sum F_{\text {frame }}+\sum F_{\text {shearwall }}} \geq 80 \%"
            r"\text{: Percentage of loads retained by frames.     }",
            # Equation 3 and its definition
            r"\frac{\sum F_{\text {frame }}}{\sum F_{\text {frame }}+\sum F_{\text {shearwall }}} \leq 25 \%"
            r"\text{: Percentage of loads retained by frames.     }\\",
            # Equation 4 and its definition
            r"\frac{\sum F_{\text {frame }}}{\sum F_{\text {frame }}+\sum F_{\text {shearwall }}} \geq 75 \%"
            r"\text{: Percentage of loads retained by shear walls.}",
            # tex_to_color_map=GRAY
        ).scale(0.6)
        shearwall_systems2 = MarkupText(  # gravity is smth like justify
                                          # /!\ underline is a line takes [] index, too./!\
            # MathTex(equation)
            "The previous statement can be translated into a mathmatical equation as follows:"
            "\n\t<span gravity='south' weight='bold' foreground='red' underline='single' underline_color='red'>a) Under vertical loads:</span>"
            "\nImplicitly means:"
            "\n\t<span gravity='south' weight='bold' foreground='red' underline='single' underline_color='red'>a) Under horizontal loads:</span>"
            "\nImplicitly means:"
            "\n\n<span gravity='south' weight='bold' foreground='red' underline='single' underline_color='red'>2) Earthquake-resistant system for RC framed structures without interaction: </span>"
            "\n\tIn certain cases, the walls are much stiffer than the frames and thus "
            "take most of the lateral load. For this reason, RPA2003 in such systems, "
            "doesn’t take into account the participation of the frame in resisting lateral "
            "load."
            "\n\tTherefore, shear walls should retain at most 20% of the vertical "
            "loads, and the total Hz loads. This may not always be a conservative "
            "procedure and it is therefore, important that the effect of the frames be considered.",
            font_size=60,
            font="Times New Roman",
            justify=0,
            unpack_groups=0,
        ).scale(0.4)
        
        self.play(
            Unwrite(shearwall_systems1),
            FadeIn(
                shearwall_systems2[:2].next_to(intro_title, DOWN, buff=0.3),
                shift=UP * 8,
            ),
            run_time=3,
        )
        self.wait()
        # Under Vertical loads
        self.play(
            LaggedStart(
                Write(
                    shearwall_systems2[2:4]
                    .next_to(shearwall_systems2[1], DOWN)
                ),
                Write(
                    equations[0]
                    .next_to(shearwall_systems2[3], DOWN) 
                    .set_style(fill_color=BLUE)
                    .shift(RIGHT*3)
                ),
                Write(shearwall_systems2[4].next_to(shearwall_systems2[3], DOWN, buff=1.2)),# Implicitly means
                
                lag_ratio=1,
            )
        )
        self.wait()
        self.play( # /!\If you put it inside the previous one it'll make a copy from the first second
            ReplacementTransform(
                    equations[0].copy(), 
                    equations[1].next_to(equations[0], DOWN, buff=0.8)
                    .set_style(fill_color=BLUE)
                ),
        )
        # Under Horizontal loads
        self.play(
            LaggedStart(
                Write(
                    shearwall_systems2[5:7]
                    .next_to(equations[1], DOWN).to_edge(LEFT, buff=1.2)
                ),
                Write(
                    equations[2]
                    .next_to(shearwall_systems2[6], DOWN)
                    .set_style(fill_color=BLUE)
                    .shift(RIGHT*3)
                ),
                Write(shearwall_systems2[7].next_to(shearwall_systems2[6], DOWN, buff=1.2)),
                
                lag_ratio=1,
            )
        )
        self.wait()
        self.play( # /!\If you put it inside the previous one it'll make a copy from the first second
            ReplacementTransform(
                    equations[2].copy(), 
                    equations[3].next_to(equations[2], DOWN, buff=0.8)
                    .set_style(fill_color=BLUE)
                ),
        )
        self.wait()
        self.play(
            Unwrite(shearwall_systems2[:8]), #[7] is : Implicitly....
            Unwrite(equations),
            FadeIn( # Both title and line.
                shearwall_systems2[8:12] # 2 lines for this title
                .next_to(intro_title, DOWN, buff=0.3)
                .to_edge(LEFT, buff=1.2),
                shift=UP * 8,
            ),
        )
        self.wait()
        self.play(
            Write(shearwall_systems2[12:]
            .next_to(shearwall_systems2[8:12], DOWN, buff=0.3)
            )
        )
        self.wait()

class Problematic(Scene):
    def construct(self):
        MathTex.set_default(fill_color=BLACK)
        Rectangle.set_default(stroke_color=BLACK)
        MarkupText.set_default(color = BLACK)
        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )

        self.camera.background_color = WHITE

        my_name = Text(
            "N. DJAFAR HENNI", font="ALGERIAN", font_size=27, color=RED
        ).to_edge(DL, buff=0)
        self.add(my_name)

        intro_title = Title("Problem statment").to_edge(UP, buff=0)
        self.add(intro_title)

        svg='C:/Manim_3_feb/manim/Presentation_PhD/floor_plan.svg'
        # self.play(DrawBorderThenFill(SVGMobject(svg).scale(1.5)))
        
        Problem = MarkupText(  # gravity is smth like justify
                               # /!\ underline is a line takes [] index, too./!\
            "\tGenerally, the design of shear walls is so conservative. This not only affects the "
            "economy, but also the structural behavior under cyclic loads. Using thicker cross-"
            "sections induces large base shear forces, minimizes ductility and (reduced time "
            "period of structures.)\n"
            "\tThe question is how can we determine the number and the position of such "
            "walls while ensuring maximum performance against earthquake damage and "
            "minimizing construction cost as well. \n"
            "\tA structural optimization is required to optimize the total cost of the structure "
            "considering the design criteria to construct lightweight, cheap and high "
            "performance structures.\n"
            "\tInitially, the seismic performance will be determined based on the formulation "
            "of multiple architectural variants, different positions and configurations of shear "
            "walls, using the static nonlinear method ‘Pushover’.",
            font_size=60,
            font="Times New Roman",
            justify=1,
            unpack_groups=0,
        ).scale(0.4)
        self.play(Write(Problem))
        self.wait()
        self.play(Unwrite(Problem))

        Objective = MarkupText(  # gravity is smth like justify
                               # /!\ underline is a line takes [] index, too./!\
            "\tOur study aims to evaluate the seismic performance of shear wall-frame " 
            "structures along with optimizing the number of shear walls to be placed " 
            "while satisfying the criteria code.\n"
            "\tThis work will be done by analyzing different architectural variants "
            "utilizing the pushover analysis as a nonlinear tool to predict the actual " 
            "performance of the structure."
            " Each variant is compared with other cases according to the specified key "
            "parameters to evaluate the seismic performance of the structure in terms of " 
            "strength and rigidity.",
            font_size=60,
            font="Times New Roman",
            justify=1,
            unpack_groups=0,
            line_spacing = 0.25,
        ).scale(0.4)
        
        self.play(Write(Objective))
        self.wait()
        self.play(Unwrite(Objective))

class Bibliography(ZoomedScene):
    def __init__(self, **kwargs):  # HEREFROM
        ZoomedScene.__init__(
            self,
            zoom_factor=0.5,  # the scale of the frame = the scale of the vision.
            zoomed_display_height=3,  # height of the frame
            zoomed_display_width=6,  # width of the frame
            image_frame_stroke_width=1,  # stroke of the image frame
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                "background_opacity": 0,
            },
            **kwargs,
        )

    def construct(self):
        # self.camera.background_image = 'C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png'
        # self.camera.init_background()
        # self.camera.background_color = GREY
        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )
        png_path = "C:/Manim_3_feb/manim/Presentation_PhD/simp_python.png"
        self.camera.background_color = WHITE

        biblio_title = Title("Bibliography", color=RED).to_edge(UP, buff=0)
        my_name = Text("N. DJAFAR HENNI", font_size=27, color=RED).to_edge(DL, buff=0)
        self.add(my_name)

        #----------------------Try-and-error method---------------------#
        Ali_all = MarkupText(
            "1) (Ali et al., 2015) carried out a comparative study by varying "
            "the cross-section and location of RC shear walls for a real stock exchange building"
            " located in Islamabad. Linear dynamic analysis was carried out on four building "
            "models with different shear-wall locations, including the actual building.\n"
            "\tThe responses of the actual and developed building models in terms of time "
            "period, story drift, and induced shear forces at the base were considered in "
            "the analysis and presented in a comparative way.\n"
            "\tResults indicated that the most optimum case came out to be the case where "
            "shear walls incorporated as the least thickness of 153mm among other cases. "
            "This process led to a reduction of the overall weight of the structure (19% "
            "increase in time period and 26% decrease in base shear force).",
                font = 'Times New Roman',
                font_size=60,
                justify=1,
                line_spacing = 0.5,
        ).scale(0.4).next_to(biblio_title, DOWN, buff=0.5)
        self.play(Write(Ali_all))
        self.wait()
        self.play(Unwrite(Ali_all))
        self.wait()

        Titiksh = MarkupText(
            "2) (Titiksh and Bhatt, 2017) carried out an investigation to determine ideal "
            "arrangements and effective locations of shear walls in a 10-story high-rising "
            "building subjected to lateral loads following the Indian standards.\n"
            "\tThe study considered four different cases for the positions of shear walls "
            "utilizing ETABS software package for developing the models as well as input "
            "of seismic loadings.\n"
            "\tThey concluded that the case with box-type shear wall at the center of the "
            "geometry is the ideal framing technique that serves the purpose of shear "
            "walls as well as vertical passages for the movement of the lifts.",
                font = 'Times New Roman',
                font_size=60,
                justify=1,
                line_spacing = 0.5,
        ).scale(0.4).next_to(biblio_title, DOWN, buff=0.5)
        self.play(Write(Titiksh))
        self.wait()
        self.play(Unwrite(Titiksh))
        self.wait()

        Sudhan = MarkupText(
            "3) (sudhan raokondapalli, 2018) conducted a comparative study by comparing "
            "various parameters such as storey drift, storey shear and storey displacement "
            "of a building under lateral loads on strategic location of shear walls.\n"
            "\tIt was found that the optimum location of shear walls is when they placed at "
            "core+edges of the building.",
                font = 'Times New Roman',
                font_size=60,
                justify=1,
                line_spacing = 0.5,
        ).scale(0.4).next_to(biblio_title, DOWN, buff=0.5)
        self.play(Write(Sudhan))
        self.wait()
        self.play(Unwrite(Sudhan))
        self.wait()

        #----------------------Using algorithms---------------------#
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

        simp_title = Text("How SIMP works?", font_size=36, color=RED).to_corner(
            UL, buff=1
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
            VGroup(*[sq.copy().add(Integer(i).rotate(-PI * 0.5)) for i in range(1, 61)])
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
                start=rec.get_corner(UL) - [1, 0, 0],
                end=rec.get_corner(UL),
                buff=0,
                color=BLACK
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
                simp_def,
                font_size=60,
                justify=1,
                color=BLACK,
            )
            .next_to(simp_title, DOWN, buff=0)  # next_to() doesn't want to work
            .scale(0.4)
        )

        simp_def_2 = (
            "It allows Instead of a black and white \nsolution, gray by having in each ele-\n"
            "ment a density design variable that \ncan vary in [0,1]."
        )
        simp_def_mobj_2 = (
            MarkupText(
                simp_def_2,
                font_size=60,
                justify=1,
                color=BLACK,
            )
            .next_to(simp_def_mobj, DOWN, buff=0)  # next_to() doesn't want to work
            .scale(0.4)
        )

        sw_label = Text("RC Shear wall", color=BLACK, font_size=37).next_to(
            SUPPORT, DOWN, buff=0.3
        )
        design_domain = (
            MathTex(r"Design\ domain\ \Omega ", color=BLACK)
            .scale(0.7)
            .move_to(rec.get_center())
        )

        self.play(Write(simp_def_mobj))
        self.wait()

        self.play(FadeIn(rec, shift=UP), FadeIn(SUPPORT, shift=UP), Write(sw_label))
        self.play(FadeIn(design_domain))
        self.wait()
        self.add(shearwall_simp.set_opacity(0))

        self.play(
            LaggedStart(
                Indicate(simp_def_mobj[-30:-1], color=RED),
                ReplacementTransform(simp_def_mobj[-30:-1].copy(), shear_wall[0]),
                lag_ratio=1,
            )
        )
        self.play(
            AnimationGroup(*[FadeIn(i) for i in shear_wall], lag_ratio=0.1),
        )
        self.wait()

        self.play(Transform(shear_wall, sq_small_group))
        # self.wait()

        self.play(Write(simp_def_mobj_2))
        self.wait()

        # Here add a text definition for colors: gray, black, white

        self.play(
            FadeIn(load, shift=RIGHT * 5),
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
            run_time=3,
        )

        # Zooming part:
        self.activate_zooming(
            animate=True
        )  # Add an initial animtaion to activate the zoom.
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate.move_to(rec.get_center())
        )  # Change the initial zoomed camera frame position
        # to the given position
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate.shift(2 * UP)
        )  # The output of the zoom
        self.wait()
        """self.play(self.camera.frame.animate.scale(1/2)) # Change the initial camera frame scale(=1)
        # to the given scale(=0.5) => shrink the frame
        self.play(self.camera.frame.animate.shift(UR*1)) # shift the camera frame to the given position
"""
