from manim import *
import numpy as np

 
class NonLinearTransform(Scene):
    def construct(self):
        # Create the grid and add it to screen
        grid = NumberPlane()
        self.add(grid)
        self.play(Create(grid, run_time=3, lag_ratio=.1))
        
        self.wait()
        
        grid.prepare_for_nonlinear_transform()
        # Transform
        self.play(
        grid.animate.apply_function(
                    lambda p: p + np.array(
                        [np.cos(p[1]), np.exp(2*np.sin(p[0]) + np.tan(p[0])), 0,]
                )
            ),
            run_time=3,
        )
        
        self.wait()

