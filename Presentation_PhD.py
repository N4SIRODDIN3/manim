from manim import *

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
        