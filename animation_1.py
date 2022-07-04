# from typing_extensions import runtime :     This has auto imported because I clicked on runtime= instead of not run_time=
from manim import *

class MobCreation(Scene):
    def construct(self):
        Cir =Circle(radius=0.2, fill_color="#984168").to_edge(UL, buff=2)
        
        name = Tex("Djafar Henni Nesreddine", color=WHITE).next_to(Cir, RIGHT)
        
        self.play(Write(name), run_time=1.5)
        self.wait(0.3)

        self.play(DrawBorderThenFill(Cir, run_time=1.5))
        self.wait()
        
        #shift_Cir=Cir.next_to(name, RIGHT)
        #self.play(ApplyWave(Cir, run_time=2),
        #)
        self.wait(0.1)

        self.play(ApplyWave(Cir))
        self.wait(0.5)
        cir2star= Star(6, color="#105897").next_to(name, RIGHT, buff=0.2)
        self.play(Transform(Cir,cir2star, path_arc=1, replace_mobject_with_target_in_scene=1)
                ,
                run_time=2
        )
        #cir2star= Star(6, color="#105897").to_edge(DOWN)
         # 2 play methods
        #self.play(Transform(Cir,cir2star), run_time=3, rate_func=smooth)
        self.wait(0.3)
        #Let's remove the star. /!\Read down
        self.play(FadeOut(Cir)) #/!\ Not cir2start because it's just a transformation of the Cir Mobject
        self.wait()
        #self.play(Cir.animate.shift(3*DR), runtime=3) # 2 play methods
        
        