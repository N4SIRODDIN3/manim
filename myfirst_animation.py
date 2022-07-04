
# All class animations CAs like Write(), Create().... have these two universal keyarguments kargs: run_time(): the time
#  and rate_func(): the behavior of the animation
# You can have as many CAs as you want in the play method.
#e.g: self.play: is a method, we can have many CAs there: self.play(sq.animate.to_edge(), ci.animate.....,....,....)
#but in case of CAs: self.play(Write()) just 1 CA

from manim import *
#simple
class Test(Scene):
    def construct(self):
        square1 = Square(
            side_length=6,fill_opacity =0.5,stroke_color=RED, fill_color = GREEN
        ) 
        
        self.play(Create(square1), run_time=3)
        self.wait()
#Animations
class Testing(Scene):
    def construct(self):
        name = Tex('Djafar Henni Nesreddine').to_edge(UL,buff=.8) #buff is a space befor&after or top&bottom
        #to_edge()  but which edge???  to_edge(DL)............
        #not like to_corner()
        nobuff_name =Tex('Djafar Henni Nesreddine. No buff').to_edge(UL)
        sq = Square(side_length=2.3, fill_color=RED, stroke_color=BLUE,fill_opacity=0.6
        ).shift(LEFT*3).to_edge(DR)
        tri = Triangle().scale(.6)
        ax = Axes()
        self.play(Write(name)) #1  class animation CA
        self.play(Write(nobuff_name))
        self.play(DrawBorderThenFill(sq), runtime=2)
        self.play(Create(tri))
        self.wait() 
        self.play(name.animate.to_edge(UR), runtime = 3)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), runtime=5) # 2 play methods
        self.wait()
#using Getters :    get_bottom, get_edge........
class Getters(Scene):
    def construct(self):
        cir = Circle(radius=0.5, fill_color=GREEN, fill_opacity=0).to_edge(DOWN)
        rec = Rectangle(color=BLUE, height=3,width=2, fill_opacity=0.5, fill_color=YELLOW).to_edge(UL, buff=1)
        arrow = Line(start=rec.get_bottom(), end=cir.get_center_of_mass()).add_tip() #tip is an arrow in the end: ---->
        #Get bottom means attach it from from, get center of mass means attach from center.
        #Arrow won't update= meaning that won't change its location 
        #In updating scene: objects will change 

        self.play(Create(VGroup(rec,cir,arrow))) #1  class animation CA
        self.wait() 
        self.play(rec.animate.to_edge(UR)) # 1 play methods

#Using Updaters
class updating(Scene):
    def construct(self):
        cir = Circle(radius=0.5, fill_color=GREEN, fill_opacity=0).to_edge(DOWN)
        rec = Rectangle(color=BLUE, height=3,width=2, fill_opacity=0.5, fill_color=YELLOW).to_edge(UL, buff=1)
        arrow = always_redraw(lambda: #redrawing in function of rec and cir positions
            Line(start=rec.get_bottom(), end=cir.get_center_of_mass()).add_tip() #tip is an arrow in the end: ---->
        )
        self.play(Create(VGroup(cir, rec, arrow)))
        self.wait()
        self.play(rec.animate.to_edge(DR)) ## 1 play methods
        #self.play(cir.animate.to_edge(DR), cir.animate.scale(2), runtime=3) # 2 play methods
        #False
        
class updating2(Scene):
    def construct(self):
        num= MathTex("ln(2)")
        box = SurroundingRectangle(num, color=BLUE, fill_opacity=0.5, fill_color=GREEN, buff=2) #big buff
        #the num obj will be surrounded by a rectangle"blue,........) with big buff
        name = Tex("Nesreddine").next_to(box, DOWN,  buff=0.3)
        self.play(Create(VGroup(num, box, name))) #1 class animation CA
        self.play(num.animate.shift(RIGHT*2), runtime=3) # 1 play methods
        self.wait()

        #ValueTracker Scene
class VTracker(Scene):
    def construct(self):
        k = ValueTracker(10) #I want to track this number

        num = always_redraw (lambda :
            DecimalNumber().set_value(k.get_value()) #I want k to be a decimal number instead, so set k as is but before
            #we need to get the value from k.
            #set_value: the value "num" will overwritten to a decimal one
            #get_value: get the current value of ValueTracker.
            )
        box = SurroundingRectangle(num, color=BLUE, fill_opacity=0.5, fill_color=GREEN, buff=2)
        self.play(Create(box))
        self.play(FadeIn(num))
        self.wait(0.5)
        self.play(k.animate.set_value(0), runtime=3, rate_func=smooth) # Is the behavior 
        #of the animation: rate_func=smooth: means will speed up when in the middle, .......
        #linear : neans with equal steps.
        #so many rate_func ...... see rate_func.py

#Graphing

class Graphing(Scene):
    def construct(self):
        plane_cartizien =  (
            NumberPlane(x_range=[-4,4,2], x_length=7, y_range=[0,16,4], y_length=5)
            .to_edge(DOWN)
            .add_coordinates() #if you don't write this values won't display
        )

        labels = plane_cartizien.get_axis_labels(x_label="x",y_label="f(x)")
        
        #x_range: values of the plane in x
        #x_length: the width of the plane: when we display it, something like scale.
        #y_arange: the hieght of the plane: when we display it, something like scale.
        parabol = plane_cartizien.plot(lambda x: x**2, x_range=[-4,4], color=GREEN)
                            #means plot this functio on plane_car..
        func_label = ( #just to be well organized
            MathTex("f(x)=(x)^(2)")
            .scale(0.6) #scale the text
            .next_to(parabol, UR, buff=0.5)
        )

        #Adding area under the graph
        area = plane_cartizien.get_riemann_rectangles(graph=parabol, x_range=[-2,3], dx=0.2, stroke_width=0.1, stroke_color=WHITE)
                            #means plot on plane_car...
        self.play(DrawBorderThenFill(plane_cartizien)) #1 second
        self.play(DrawBorderThenFill(VGroup(parabol, labels, func_label))) #1 second each=3
        #self.play(DrawBorderThenFill(parabol))
        self.wait() #1 second
        self.play(Create(area)) #1 second
        self.wait() #1 second
        # Sum of 7 s

        #Updaters with graphs
class GraphUpdaters(Scene):
    def construct(self):
        axs = Axes(x_range=[-4,4,1], y_range=[-2,16,2], x_length=10, y_length=6).to_edge(DOWN) #Not a plane just axes
        parabol_func = axs.plot(lambda x: x**2, x_range=[-4,4], color=BLUE)
        #plot slop = tangent
        #get definition of get_secant_slope_group to understand
        slope = axs.get_secant_slope_group(x=3,graph=parabol_func,dx=0.01, secant_line_color="#56d599", secant_line_length=3)
        #slope at x=3 of the function
        
        k=ValueTracker(-3)   #a lot of things are dependent of this k when it comes to tracks and update.
        #for updated secant along the graph, we use updaters: x(is variable)=k.get_value and not x(is constant)=3
        slope = always_redraw(
            lambda:
            axs.get_secant_slope_group(x=k.get_value(),graph=parabol_func,dx=0.01, secant_line_color=GREEN, secant_line_length=3)
        )

        # A point that travel along the curve
        # ??????? I need more time to understand.
        point = always_redraw( lambda : Dot().move_to(
            # We can write c2p instead of coords to point
            #Here is the case of a dot with respect to axes and not the scene. ex: point (1,1) with respect to the current
            # axes is not the same as (1,1,0) with respect to the scene or plane.
            # see the last scene class (CoordsToPointExample) to understand more.
            axs.coords_to_point(k.get_value(), parabol_func.underlying_function(k.get_value())
                            ))
        )

        self.add(slope, parabol_func, axs, point) #to be added at 0second time not like create.
        self.wait()
        #Drawing the tangent up to x=4
        self.play(k.animate.set_value(4), run_time=6) #without updater(always_redraw) nothing will happen
                                        #runtime=3 or run_time=3 are the same,but without parenthesis (3)=False
                # Sum of 7 seconds

# SVGs

svg_path= "C:\Manim_3_feb\manim_ce\SVGs_Images"
img_path= "C:\Manim_3_feb\manim_ce\SVGs_Images"


class SVGs(Scene):
    def construct(self):
        icon = SVGMobject(f"{svg_path}\\wheel.svg").to_edge(UL)
        img = ImageMobject(f"{svg_path}\\Desert_Sahara.JPG")  
        self.play(DrawBorderThenFill(icon))
        #Can't apply DrawBorderThen.... animation on Images
        self.play(FadeIn(img))
        self.wait()


#two scenes together by copy/paste
class multi_scenes(Scene):
    def construct(self):
        axs = Axes(x_range=[-4,4,1], y_range=[-2,16,2], x_length=10, y_length=6).to_edge(DOWN) #Not a plane just axes
        parabol_func = axs.plot(lambda x: x**2, x_range=[-4,4], color=BLUE)
        #plot slop = tangent
        #get definition of get_secant_slope_group to understand
        slope = axs.get_secant_slope_group(x=3,graph=parabol_func,dx=0.01, secant_line_color="#56d599", secant_line_length=3)
        #slope at x=3 of the function
        
        k=ValueTracker(-3)   #a lot of things are dependent of this k when it comes to tracks and update.
        #for updated secant along the graph, we use updaters: x(is variable)=k.get_value and not x(is constant)=3
        slope = always_redraw(
            lambda:
            axs.get_secant_slope_group(x=k.get_value(),graph=parabol_func,dx=0.01, secant_line_color=GREEN, secant_line_length=3)
        )

        # A point that travel along the curve
        # ??????? I need more time to understand.
        point = always_redraw( lambda : Dot().move_to(
            # We can write c2p instead of coords to point
            axs.coords_to_point(k.get_value(), parabol_func.underlying_function(k.get_value())
                            ))
        )

        self.add(slope, parabol_func, axs, point) #to be added at 0second time not like create.
        self.wait()
        #Drawing the tangent up to x=4
        self.play(k.animate.set_value(4), run_time=6) #without updater(always_redraw) nothing will happen
                                        #runtime=3 or run_time=3 are the same,but without parenthesis (3)=False
                # Sum of 7 seconds

        icon = SVGMobject(f"{svg_path}\\wheel.svg").to_edge(UL)
        img = ImageMobject(f"{svg_path}\\Desert_Sahara.JPG")  
        self.play(DrawBorderThenFill(icon))
        #Can't apply DrawBorderThen.... animation on Images
        self.play(FadeIn(img))
        self.wait()

class CoordsToPointExample(Scene): #From Manual of manimCE
                def construct(self):
                    ax = Axes().add_coordinates()

                    # a dot with respect to the axes
                    dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
                    lines = ax.get_lines_to_point(ax.c2p(2,2)) #draw the drop lines

                    # a dot with respect to the scene
                    # the default plane corresponds to the coordinates of the scene.
                    plane = NumberPlane()
                    dot_scene = Dot((2,2,0), color=RED)

                    self.add(plane, dot_scene, ax, dot_axes, lines)
