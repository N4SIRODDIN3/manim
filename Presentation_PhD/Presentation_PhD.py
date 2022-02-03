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
        bg = Rectangle(fill_opacity=1, fill_color=BLACK,
                        stroke_color='#ff073a').round_corners(0.8)
        bg.to_corner(UL, buff=0)
        title = Title("Shear walls explained").to_edge(UP, buff=0.2)
        # bg.add_updater(lambda mobj: mobj.round_corners().surround(intro))
        def update_function(mobj):
            mobj.move_to(bg.get_center())
        self.add(plan, bg) # Order matter, else you won't see the text
        intro.add_updater(update_function)
        self.play(Write(intro), rate_func = smooth)
        self.wait()
        self.play(ApplyWave(bg))
        self.wait(0.4)
        self.play(ReplacementTransform(bg, title), FadeOut(intro), rate_func = linear)
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
        self.play(AnimationGroup(*[component.animate.shift(LEFT*5) for component in first_encounter_components], lag_ratio=0.05))
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
            
                intro_title = Title("Introduction")
                self.add(intro_title)
                
                Int_1 = (
                    "\tIn high-seismicity countries, buildings must be designed to resist" # from In to resist is max char
                    " seismic loading. It’s well know that RC shear walls represent a structurally" # smartly stoped at efficient
                    " efficient system to stiffen an RC building under those loads."
                )
                Int_2 = (
                    "\tIn general, a shear wall system consists of a combination of shear walls and frames" 
                    " because this type of systems normally provide the required stiffness and strength" 
                    " to withstand lateral loads in medium-high and even low rise buildings."
                )
                
                intro_1 = MarkupText(Int_1,
                     font_size=60, 
                     unpack_groups=0, 
                     font='LM Roman 12', 
                     line_spacing=1.8, 
                     disable_ligatures=1,
                     justify=1 # : that is only available in MarkupText
                ).scale(0.4).next_to(intro_title, DOWN, buff=0.5)
                
                intro_2 = MarkupText(Int_2,
                     font_size=60, 
                     unpack_groups=0, 
                     font='LM Roman 12', 
                     line_spacing=1.8, 
                     disable_ligatures=1,
                     justify=1 # : that is only available in MarkupText
                ).scale(0.4).next_to(intro_1, DOWN)
                
                
                self.play(LaggedStart(
                    Write(intro_1), Write(intro_2), lag_ratio=1
                    ),run_time=2,
                )
                self.wait(0.4)
                
                self.play(
                    Create(SurroundingRectangle(intro_2[1][0:10], color=RED)), 
                    Create(SurroundingRectangle(intro_2[1][13:19]), color=RED), # 's' of frames is included 
                    run_time=2,
                    rate_func=there_and_back_with_pause
                )
                # 
                self.wait(0.4)
                
                shw = intro_2[1][0:10].copy()
                fr = intro_2[1][13:19].copy()
                self.play(
                    shw.animate.to_edge(UR, buff=1.5),
                    fr.animate.next_to(intro_title, DOWN),
                    Unwrite(intro_2),Unwrite(intro_1),
                    run_time=4,
                )
                self.wait(1)
                
                self.play(Indicate(fr, 3), shw.animate.set_opacity(0.2))
                self.wait(0.5)
                
                frame_definition = MarkupText(
                "A frame is an inter-\nconnection between \nvertical columns and \nhorizontal beams that \n" 
                "bends predominantly \nin a shear mode deformation.",
                     font_size=60,
                     font='LM Roman 12',
                     justify=1
                ).scale(0.4).align_on_border(LEFT)
                
                
                L_column = Line().set_style(stroke_width=10).rotate(PI*0.5)
                R_column = L_column.copy().shift(RIGHT*3)
                roof = always_redraw(lambda:Line(start=L_column.get_end(),end=R_column.get_end()))
                load = always_redraw(lambda:
                    Arrow(start=roof.get_start()-[1,0,0],end=roof.get_start(), buff=0)
                )
                shearwall = Rectangle(fill_color=BLUE, fill_opacity=1, height= L_column.get_length(), width=roof.get_length()*0.6)
                shearwall.set_color_by_gradient(GREY_C).scale(0.6)
                frame = VGroup(L_column, R_column, roof, load).scale(0.6) # , shearwall
                # frames = frame.copy()
                storey_4 = always_redraw(lambda:
                    VGroup(*[frame.copy() for _ in range(4)]).arrange(UP, buff=-0.1).next_to(fr, DOWN, buff=0.4) # Force buffer to be 0 even in the presence of arrow tips.
                )
                
                
                # storey_4[0].add(fix1,fix1) # just put them inside ( , ), not in a list like that []

                loads = VGroup()
                for element in storey_4:
                    if element==storey_4[0]:
                        self.play(Create(element[:-1]), Write(frame_definition), run_time=3) # shear walls and loads are not included (-1, -2)
                        # here add support for the first storey
                    else:
                        self.play(Create(element[:-1]))
                    loads.add(element[3])
                   # shearwalls.add(element[4])
                self.wait()

                self.play(FadeIn(loads, shift=RIGHT*7, scale=2))
                self.wait(0.05)
                
                
                self.play(
                    storey_4.animate(run_time=2).apply_function( # /!\shear walls should not be included in this deformation
                        # lambda p: p + np.array([np.sqrt(abs(p[1]))*p[1]**2,0, 0]
                        lambda p: p + np.array([np.sin(p[1]), 0, 0]
                    )
                ).set_color([RED, YELLOW ,RED]),)
                self.wait(0.3)

                self.play(AnimationGroup(
                    Unwrite(frame_definition), fr.animate.shift(LEFT*5), 
                    # fr.animate.set_opacity(0.3), #??????????
                    # storey_4.animate.set_opacity(0.3), #??????????
                    lag_ratio=1
                )                
                )
                
                self.wait()
                
                shearwalls = VGroup()
                for i in range(4):
                    shearwalls.add(shearwall.copy())
                    print(shearwalls)

                shearwalls.arrange(UP, buff=0).next_to(shw, DOWN, buff=0.6)

                self.play(shw.animate.set_opacity(1), fr.animate.set_opacity(0.2), 
                )
                self.wait(0.5)
                for i in storey_4:
                    self.play(i.animate(run_time=0.2, rate_func=smooth).set_opacity(0.2))
                self.play(Indicate(shw, 3))

                self.add(Rectangle(height=1, width=3, fill_color=GREY, fill_opacity=1).next_to(shearwalls[0], DOWN, buff=0))
                
                for element in shearwalls:
                    self.play(Create(element)) # shear walls and loads are not included (-1, -2)
                self.wait(1)
                shearwall_definition = MarkupText('Shear walls are vertical elements \nof the horizontal force' 
                                                  'resisting \nsystem. \nShear walls deflects predominantly \nin a '
                                                  'bending mode deformation \nlike a cantilever, as illustrated '
                                                  'in \nthe following animation.',
                                                  font_size=60,
                                                  font='LM Roman 12',
                                                  justify = 1,

                ).scale(0.4).next_to(shearwalls, LEFT, buff=1)

                self.play(Write(shearwall_definition))
                self.wait(0.5)
                self.play(loads.animate.next_to(shearwalls, LEFT, buff=0).shift(UP*0.58))
                self.wait()
                '''
                interactions = VGroup()
                # for jf, fd in zip(range(4), [1, 0.6, 0.3, 0.15])
                inter1 = always_redraw(lambda:
                    Arrow(start=storey_4[0][4].get_corner(UL),end=storey_4[0][1].get_end(), color=RED_B, buff=0)
                )
                # self.add(inter1)
                # self.play(shearwalls.animate(run_time = 2).shift(RIGHT*3))
                # self.wait() #Always end with wait
                # 
                '''

class Bibliography(MovingCameraScene):
    def construct(self):
    
        self.camera.background_color=WHITE
        sq = Square(0.5, fill_color=GREY, fill_opacity=0.2)
        sq_small = Square(0.2)
        shear_wall = VGroup(*[sq.copy() for _ in range(60)]).arrange_in_grid(6,10, buff=0).rotate(PI*0.5)
        sq_small_group = VGroup(*[sq_small.copy().set_style(stroke_width=0.4) for _ in range(350)]).arrange_in_grid(14,25, buff=0).rotate(PI*0.5)
        rec = Rectangle(height=3, width=5,stroke_width=0, fill_color=GREY, fill_opacity=1).rotate(PI*0.5)
        SUPPORT = always_redraw( lambda: Rectangle(height=4*1.15, width=0.3,fill_color=GREY,stroke_width=0, fill_opacity=1).rotate(PI*0.5).next_to(rec, DOWN, buff=0))
        shearwall_simp = ImageMobject('simp_python.png').rotate(PI*0.5).next_to(SUPPORT, UP, buff=0)
        shearwall_simp.stretch_to_fit_width(width = rec.width).stretch_to_fit_height(rec.height).shift(UP*0.535)
        self.play(Create(rec),Create(SUPPORT))
        self.wait()
        self.add(shearwall_simp.set_opacity(0))
        self.play(AnimationGroup(*[FadeIn(i) for i in shear_wall], lag_ratio=0.1))
        # self.wait()
        self.play(Transform(shear_wall, sq_small_group))
        # self.wait()
        self.play(*[i.animate.set_opacity(rd.uniform(0,1)).set_style(fill_color=BLACK) for i in sq_small_group])
        # self.wait()
        self.play(*[i.animate(run_time=3, rate_func=there_and_back).set_opacity(rd.uniform(0,1)).set_style(fill_color=[WHITE]) for i in sq_small_group])
        # self.wait()
        self.play(*[i.animate(run_time=3, rate_func=there_and_back).set_opacity(rd.uniform(0.6,1)).set_style(fill_color=[GREY_D]) for i in sq_small_group])
        self.play(*[i.animate.set_opacity(0).set_style(fill_color=[BLACK]) for i in sq_small_group], shearwall_simp.animate.set_opacity(1), run_time=4)
        # self.play(), run_time=2),FadeIn(shearwall_simp)