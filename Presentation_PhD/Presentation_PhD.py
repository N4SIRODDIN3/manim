from manim import *
import random as rd

# Resetting the defautt values of almost all Mobjs:
VMobject.set_default(color=BLACK)
SingleStringMathTex.set_default(color=BLACK)
Tex.set_default(color=BLACK)

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
        # Resetting default values:
        MathTex.set_default(fill_color=BLACK)
        # It will affect the SurroundingRectangle mobj, but you can set the color from stroke_color
        # Because the set_default(stroke_color) will override the color attribute.
        Rectangle.set_default(stroke_color=BLACK) 
        MarkupText.set_default(color = BLACK)
        Title.set_default(color = BLACK)
        Line.set_default(color = BLACK)
        Arrow.set_default(color = BLACK)
        Tex.set_default(color = BLACK)
        Text.set_default(color = BLACK)
        # Set the background to WHITE
        self.camera.background_color = WHITE

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

        intro_title = Title("Introduction", color = RED)
        self.add(intro_title)

        Int_1 = (
            "\tIn high-seismic countries like Algeria, buildings must be designed to resist"  # from In to resist is max char
            " seismic loading. It’s well know that RC shear walls represent a structurally"  # smartly stoped at efficient
            " efficient system to stiffen an RC building under those loads."
        )
        Int_2 = ( # the spaces after (of:) are helpful because shear is in line and walls in the next line.
            "\tIn general, a shear wall system consists of a combination of:     shear walls and frames"
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

        self.play( # stroke_color is not an param for surroundingrec, but we need this. see the beginning of this class.
            Create(SurroundingRectangle(intro_2[1][0:10], stroke_color=DARK_BLUE)),
            Create(
                SurroundingRectangle(intro_2[1][13:19]), stroke_color=GREEN
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

        self.play(Indicate(fr, 3, color = GREEN), shw.animate.set_opacity(0.2))
        self.wait(0.5)

        frame_definition = (
            MarkupText(  # /!\ Adding a new line \n will affect the justify function./!\
                "A frame is an interconnection between vertical columns and horizontal beams."
                "\nFrames bend predominantly in a shear mode deformation.",
                font_size=120,
                width = 5,
                font="LM Roman 12",
                justify=1,
                unpack_groups=0,
            )
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
                    Write(frame_definition[:3]),
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
            storey_4.animate( rate_func=there_and_back_with_pause)
            .apply_function(  # /!\shear walls should not be included in this deformation
                # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                lambda p: p + np.array([np.sin(p[1]), 0, 0])
            )
            .set_color([RED, YELLOW, RED]),
            Write(frame_definition[3:].shift(DOWN)),  # Write the rest of the text simultaneously
            run_time=3,
        )
        
        self.wait(0.3)
        
        self.play(Unwrite(frame_definition))
        self.wait()
        self.play(fr.animate.set_opacity(0.3).to_edge(LEFT))
        def storey_op(mob):
            mob.set_opacity(0.3)
        storey_4.add_updater(storey_op)
        # /!\ Don't forget to remove this updater afterwards.
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

        self.play(Indicate(shw, 3, color = GREEN))

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

        self.play(loads.set_opacity(1).animate.next_to(shearwalls, LEFT, buff=0).shift(UP * 0.58))
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
        self.remove(loads)
        self.play(
            Unwrite(shearwall_definition),
            shw.animate.next_to(fr, RIGHT, buff=2),
            
        )
        self.wait()
        for l in storey_4:
            l.remove(l[-1]) # Remove the loads form the storey_4
        
        # Now, remove the updater to change the opacity.
        storey_4.clear_updaters() # Clear all updaters even lambdas.
        storey_4.set_opacity(1)
        self.wait(0.2)

        plus = Text("+").next_to(shearwalls, LEFT)
        equal = Text("=").next_to(shearwalls, RIGHT)
        self.play(
            AnimationGroup(
                fr.animate.set_opacity(1),
                ApplyWave(storey_4),
                Indicate(
                    plus , 3
                ),  # next_to(storey_4, RIGHT) try to find
                # the issue later. COMPARE IT WITH SHEARWALLS BECASUE IT WORKS WITH THEM.
                ApplyWave(shearwalls),
                Indicate(equal , 3),
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
        shearwalls.clear_updaters()
        self.play(storey_4.animate.next_to(shw_fr_label, DOWN, buff=0.4),)
        self.play(shearwalls.animate.next_to(storey_4, RIGHT, buff=0),)
        # Remove the residual:
        self.play(Unwrite(plus), Unwrite(equal), Unwrite(shw), Unwrite(fr),)
        # fade the load simultaneously with writting the paragraph:
        sw_frame_def = MarkupText(
            "Since their mode of deflection varies, the frame tends to restrain the "
            "shear wall in upper stories, and the shear wall tends to restrain the "
            "frame in lower stories. \nThis reduces the lateral deflection and improves "
            "the overall efficiency of the structural system.",
                font_size=60,
                width = 6,
                font="LM Roman 12",
                justify=1,
                unpack_groups=0,
            ).align_on_border(LEFT, buff=0.1)
        
        self.play(
            FadeIn(loads.next_to(storey_4, LEFT, buff=0).shift(UP * 0.57), shift = RIGHT*5, scale = 2),
            run_time = 1
        )
        self.wait()
        sw_frame = VGroup(storey_4, shearwalls)
        self.play(
            sw_frame.animate(
                 rate_func=there_and_back_with_pause
            )  # (t=0.3, pause_ratio=0.8)
            .apply_function(
                # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                lambda p: p
                + np.array([np.sin(p[1]), 0, 0])
            )
            .set_color([RED, YELLOW, RED]),
            
            Write(sw_frame_def),
            run_time=3,
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


        # -------------Don't forget to FadeOut the chapter's title before the next scene--------------------
class Shearwall_Systems(Scene):
    def construct(self):
        VMobject.set_default(color=BLACK)
        MarkupText.set_default(color = BLACK)
        SingleStringMathTex.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
        self.camera.background_color = WHITE
        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )


        my_name = Text(
            "N. DJAFAR HENNI", font="ALGERIAN", font_size=27, color=RED
        ).to_edge(DL, buff=0)
        self.add(my_name)

        intro_title = Title("Introduction", color = RED).to_edge(UP, buff=0)
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
        ).scale(0.6).set_style(fill_color=ORANGE) # color can be changed through fill_color
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
        # -------------Don't forget to FadeOut the title of chapter before the next scene--------------------
        self.play(
            Unwrite(shearwall_systems2[12:]),
            Unwrite(shearwall_systems2[8:12]),
        )
        self.wait()
        self.play(
            FadeOut(intro_title, shift = UP*2)
        )
        self.wait()
class Problematic(Scene):
    def construct(self):
        VMobject.set_default(color=BLACK)
        MarkupText.set_default(color = BLACK)
        SingleStringMathTex.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
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

        prob_title = Title("Problem statment", color = RED).to_edge(UP, buff=0)
        self.play(Write(prob_title))
        self.wait()

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
        ).scale(0.4).next_to(prob_title, DOWN, buff = 0.5)
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
        ).scale(0.4).next_to(prob_title, DOWN, buff = 0.5)
        
        self.play(Write(Objective))
        self.wait()
        self.play(Unwrite(Objective))

        # -------------Don't forget to FadeOut the title of chapter before the next scene--------------------
        self.play(FadeOut(prob_title, shift = UP*2))

class Literature(ZoomedScene):
    def __init__(self, **kwargs):  # HEREFROM
        ZoomedScene.__init__(
            self,
            zoom_factor=0.5,  # the scale of the frame = the scale of the vision.
            zoomed_display_height=3,  # height of the frame
            zoomed_display_width=6,  # width of the frame
            image_frame_stroke_width=1,  # stroke of the image frame
            zoomed_camera_config={
                "default_frame_stroke_width": 7, # stroke width of the frame.
                "background_opacity": 1, # Show the background: 0 = transparent
            },
            zoomed_display_corner= UP + LEFT, # self.zoomed_d.... it didn't work
            **kwargs,
        )

    def construct(self):
        # self.camera.init_background()
        # self.camera.background_color = GREY
        # MathTex.set_default(fill_color=BLACK)
        MarkupText.set_default(color = BLACK)
        VMobject.set_default(color=BLACK)
        SingleStringMathTex.set_default(color=BLACK)
        Tex.set_default(color=BLACK)


        self.add(
            ImageMobject("C:/Manim_3_feb/manim/Presentation_PhD/UMKBiskra_Logo.png")
            .set_opacity(0.4)
            .scale(0.5)
        )
        png_path = "C:/Manim_3_feb/manim/Presentation_PhD/simp_python.png"
        self.camera.background_color = WHITE

        biblio_title = Title("Bibliography", color=RED).to_edge(UP, buff=0)
        my_name = Text("N. DJAFAR HENNI", font= 'Algerian', font_size=27, color=RED).to_edge(DL, buff=0)
        self.add(my_name)
        self.play(Write(biblio_title))
        # I should write that researchers have split into 2 groups: one used:
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
        self.play(Write(simp_mobj))
        self.wait()

        simp_title = Text("How SIMP works?", font_size=36, color=RED).to_corner(
            UL, buff=1
        )
        self.play(FadeOut(simp_mobj, shift=UP), FadeIn(simp_title, shift=UP))
        self.wait()
        
        simp_def = (
            "\tThe traditional approach to topology optimization (place, study) is the "
            "discretization of a domain into a grid of a finite element called: \nisotropic"
            " solid microstructures."
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
        # self.add(NumberPlane())
        simp_def_mobj = (
            MarkupText(
                simp_def,
                font_size=120,
                width = 4.5,
                justify=1,
                color=BLACK,
            )
            .next_to(simp_title, DOWN, buff=1)  # next_to() doesn't want to work
            
        )

        simp_def_2 = (
            "\tIt allows Instead of a black and white solution, gray by having in each ele"
            "ment a density design variable that can vary in [0,1]."
        ) 
        # Don't forget to add a colormap label [0,1] using valueTracker.....
        simp_def_mobj_2 = (
            MarkupText(
                simp_def_2,
                font_size=120,
                width = 4.5,
                justify=1,
                color=BLACK,
            )
            .next_to(simp_def_mobj, DOWN, buff=0.4)  # next_to() doesn't want to work
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
        color_map = Rectangle(
                height=3.20,
                width=0.3,
                fill_color=[BLACK, WHITE], # because it's rotated we reversed the colors.
                stroke_width=1,
                stroke_color = BLACK,
                fill_opacity=1,
            ).rotate(PI * 0.5).next_to(simp_def_mobj_2, DOWN, buff=0.2)
        self.play(Create(color_map))
        self.wait()
        
        self.play(
            FadeIn(load, shift=RIGHT * 5),
        )
        # Create iteration effects using valuetracker.
        v = ValueTracker(0)
        iteration_label = Tex('Iteration:').next_to(biblio_title, DOWN, buff= 0.35)
        iteration = always_redraw(lambda: Integer().set_value(v.get_value()).next_to(iteration_label, RIGHT, buff = 0.3))
        
        self.add(iteration, iteration_label)
        self.play(
            v.animate.set_value(10),
            *[
                i.animate.set_opacity(rd.uniform(0, 1)).set_style(fill_color=BLACK)
                for i in sq_small_group
            ]
        )
        # self.wait()
        self.play(
            v.animate.set_value(20),
            *[
                i.animate( rate_func=there_and_back)
                .set_opacity(rd.uniform(0, 1))
                .set_style(fill_color=[WHITE])
                for i in sq_small_group
            ],
            run_time=3,
        )
        # self.wait()
        self.play(
            v.animate.set_value(30),
            *[
                i.animate( rate_func=there_and_back)
                .set_opacity(rd.uniform(0.6, 1))
                .set_style(fill_color=[BLACK])
                for i in sq_small_group
            ],
            shearwall_simp.animate.set_opacity(0.5),
            run_time=3,
        )
        self.play(
            v.animate.set_value(40),
            *[
                i.animate.set_opacity(0).set_style(fill_color=[BLACK])
                for i in sq_small_group
            ],
            shearwall_simp.animate.set_opacity(1),
            run_time=3,
        )
        # Uncreate all objects on the scene except title and my name.
        to_remove = VGroup(simp_title, simp_def_mobj, simp_def_mobj_2, shear_wall, load, SUPPORT, color_map, sw_label, design_domain, iteration, iteration_label)
        # shearwall image can't be added to the group. , shearwall_simp
        self.play(Uncreate(to_remove), FadeOut(shearwall_simp), FadeOut(rec))
        
        # Continuing with what Pooya did.
        pooya_study = (
            MarkupText(
                "\tKaveh and Pooya investigated different types of shear walls with/without opening."
                " Additionally, the effects of shear wall-frame interaction for single and coupled "
                "shear walls were studied. 6 models were developed which are: Four-story shear wall, Eight-story shear wall, "
                "Twelve-story shear wall, Twelve-story shear wall with opening, Eight story shear "
                "wall-frame, Twelve-story shear wall-frame."
                # Conclusion:
                # add the Image before this text.
                "\n\tThe optimization demonstrated that for the highest part, a significant amount of material "
                "can be saved which is also manifested from the lowest part of the structure. \n"
                "\tIt was also visible that the existence of the coupled beams is definitely necessary for the "
                "middle part of the structure, while they are only necessary for the other parts to resist "
                "gravity loads. \n\tThis optimization process has efficiently reached the optimal placement of "
                "openings and optimal removal of inefficient materials upon reaching minimal strengthening "
                "with maximum performance.",
                font_size=60,
                width = 9,
                justify=1,
                color=BLACK,
                unpack_groups = 0,
            )
            .align_on_border(LEFT, buff = 0.1) 
        )
        self.play(Write(pooya_study[:7])) # Conclusion not included
        self.wait()
        # self.play(FadeOut(pooya_study[:7], shift = UP))
        # self.wait(0.5)
        # Pooya conclusion
        pooya_svg = SVGMobject(
            'C:/Manim_3_feb/manim/Presentation_PhD/simp_pooya_1.svg'
        )
        self.play(
            Write(pooya_study[7:]), 
            DrawBorderThenFill(
                pooya_svg[:2].scale(3.5).align_on_border(RIGHT))
        )
        self.wait(0.5)
        #---------------------Zooming part:-------------------------
        zoomed_camera_text = Text("Zoomed structure", color=RED, font_size=32) # label of the zoomed display
        self.zoomed_camera.frame.set_style(stroke_color= RED)
        self.zoomed_display.display_frame.set_style(stroke_color= RED)
        # Change it's initial position
        self.zoomed_camera_frame_starting_position = pooya_svg.get_center() # didn't work 
        self.zoomed_display_corner= UP + LEFT, # didn't work
        self.activate_zooming(
            animate=True
        )  # Add an initial animtaion to activate the zoom.
        zoomed_camera_text.next_to(self.zoomed_display.display_frame, UP, buff = 0.1) # label
        self.play(FadeIn(zoomed_camera_text, shift=UP)) # label
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate.move_to(pooya_svg.get_top()).shift(RIGHT * 1.65).shift(3.5 * DOWN)
        )  # Change the initial zoomed camera frame position
        # to the given position
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate.shift(1.8 * DOWN)
        )  # The output of the zoom
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate.scale([0.35, 1.2, 0]).shift(UP*0.3)
        )  # Change the dimensions of the frame.
        self.wait()
        self.play(
            self.zoomed_camera.frame.animate(rate_func = there_and_back_with_pause).shift(UP*0.6) # they are definetly necessary to....
        )  # Change the dimensions of the frame.
        self.wait()
        self.play(AnimationGroup(
            self.zoomed_camera.frame.animate.shift(UP*1.8), # while they are only necessary to resist...
            self.zoomed_camera.frame.animate.shift(DOWN*0.5),
            lag_ratio = 1
            )  # Change the dimensions of the frame.
        )
        self.wait()
        """self.play(self.camera.frame.animate.scale([x=1/2, y=, z=]) # Change the initial camera frame scale(=1)
        # to the given scale(x=0.5) => shrink the frame
        self.play(self.camera.frame.animate.shift(UR*1)) # shift the camera frame to the given position
        """
        # Animate the deactivation of the zooming.
        zd_rect = BackgroundRectangle(self.zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        #unfold = reveal, uncover
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(self.zoomed_display))

        self.play(Unwrite(zoomed_camera_text), self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(self.zoomed_display.display_frame), FadeOut(self.zoomed_camera.frame))
        self.wait()
        self.play(FadeOut(biblio_title, shift = UP*2))
#----------------------Plan de travail ---------------------#
class work_plan(Scene):
    def construct(self):
        VMobject.set_default(color=BLACK)
        MarkupText.set_default(color = BLACK)
        SingleStringMathTex.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
        # Add the needed mobjs to the scene
        self.camera.background_color = WHITE
        # Work plan 'Chapters'
        plan_title = Title("Chapters", color=RED).to_edge(UP, buff=0)
        self.play(Write(plan_title))

        plan_list = [
            'I-	A literature review on structures with and without shear wall-frame' 
            'interaction, and different analysis methods (linear and nonlinear).', 
            'II- Linear and nonlinear dynamic analyses methods existing in the literature '
            'for RC shear wall structures',
            'III- Nonlinear static pushover method and its recent enhancements.', 
            'IV- Introduction of variants with different shear wall distributions and stiffness ratios',
            'V-	Multiple key parameters are taken in order to evaluate the aforementioned variants in terms '
            'of strength and rigidity.', 
            'VI- Conclusions and recommendations are carried out for future works. ',
        ]

        bulleted_list = BulletedList(
            *[plan_list[i] for i in range(5)], 
            dot_scale_factor=4,
        ).scale(0.7)
        for item in bulleted_list:
            item[0].set_style(fill_color = RED, stroke_width = 4, stroke_color = GREEN_C)
        for item in bulleted_list:
            self.play(LaggedStart(
            *[DrawBorderThenFill(item[0]), Write(item[1:])],
            lag_ratio = 1
            ) # The last item is missing in the scene.
        )
            
