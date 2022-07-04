from manim import *

svg_path = "C:/Manim_3_feb/manim_ce/SVGs_Images"  # / not \


class GearTrain(Scene):
    def construct(self):
        Gears = SVGMobject(
            "C:/Manim_3_feb/manim_ce/updaters_gear_train/Gears.svg" 
        ).scale(3)
        (RedGear, BlueGear) = Gears.shift(DOWN * 0.5 + RIGHT)
        # RedGear: Driver; BlueGear: Driven

        Readings = VGroup(
            Tex("Angular Acceleration $[rad/{s}^{2}]$"),
            Tex("Driver Gear:", color="#ff073a"),
            Tex("Angular Velocity $[rad/s]$"),
            Tex("Driver Gear:", color="#ff073a"),
            Tex("Driven Gear:", color="#04d9ff"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        GR = 24 / 12  # GearRatio = DrivenTeeth/DriverTeeth

        # RA: RedGear Acceleration; RV: RedGear Velocity
        # BV: BlueGear Velocity
        RA = DecimalNumber(0, 3).next_to(Readings[1])
        RV = DecimalNumber(0, 2).next_to(Readings[3])
        BV = DecimalNumber(0, 2).next_to(Readings[4])
        Readings.add(RA, RV, BV).scale(0.9)
        Readings.to_corner(UL, buff=0.2)

        def Driver(m, dt):
            RV.set_value(RV.get_value() + dt * RA.get_value())
            BV.set_value(-RV.get_value() / GR)
            m.rotate(dt * RV.get_value())

        def Driven(m, dt):
            m.rotate(dt * BV.get_value())

        self.play(
            LaggedStart(
                DrawBorderThenFill(Gears), FadeIn(Readings, scale=0.9), lag_ratio=0.5
            )
        )
        RedGear.add_updater(Driver)
        BlueGear.add_updater(Driven)

        AccTime = [[PI / 3, 6], [0, 2], [-PI / 2, 6], [0, 4]]
        self.wait()  # AccTime = [[Acceleration,WaitTime],...]

        for (a, t) in AccTime:
            self.add_sound("updaters_gear_train\Click.wav")
            self.play(Indicate(RA.set_value(a)), run_time=0.5)
            corr = 2 / 60  # missed frame correction
            self.wait(t + corr - 0.5)  # -0.5 for run_time=0.5

        self.play(FadeOut(RedGear, BlueGear, Readings), run_time=2)
