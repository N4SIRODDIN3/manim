from manim import *

# from collections import Counter


class fjdk(Scene):
    def construct(self):
        v = ValueTracker(10)
        cir = Circle(radius=3).set(color=BLUE).to_edge(UP)
        j = 1 + v.get_value()
        texti = always_redraw(
            lambda: MathTex(r"f() = {0}".format(j)).move_to(cir.get_center())
        )
        num = always_redraw(
            lambda: DecimalNumber(include_sign=True)
            .set_value(v.get_value())
            .to_edge(LEFT)
        )

        self.add(cir, num, texti)
        self.play(v.animate.set_value(0), run_time=2)


class MultipleFonts(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")
        japanese = Text(
            "日本へようこそ", t2g={"日本": (BLUE, YELLOW_B)}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("Здравствуйте मस नम म ", font="sans-serif")
        hin = Text("नमस्ते", font="sans-serif")
        arb = Text(
            "صباح الخير \n تشرفت بمقابلتك", font="ALGERIAN"
        )  # don't mix RTL and LTR languages nothing shows up then ;-) Right to Left
        chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i - 3))


def label_point(self, x, y, positive=True, contour_value=True):
    point = np.array([x, y, 0])
    value = np.round(self.sample_scalar(positive=positive), 1)
    threshold = False
    threshold_value = 1.1
    if contour_value:
        value = threshold_value
    if value < 3 and value > 1:
        value = threshold_value
        threshold = True
    label = MathTex(r"f({0}, {1}) = {2}".format(x, y, value))
    label.scale(0.8)
    dot = Dot().move_to(point)
    # opposite of convention because of way batman function is defined
    if value > 1 and value != threshold_value:
        dot.set_color(INSIDE_COLOR)
    elif value == threshold_value:
        dot.set_color(YELLOW)
    else:
        dot.set_color(OUTSIDE_COLOR)
    label.add_background_rectangle()
    label.next_to(dot, DOWN)

    self.play(GrowFromCenter(dot))
    self.wait()
    self.play(FadeIn(label))
    self.wait()

    close_enough = Tex("Close enough to target value").scale(0.7)
    close_enough.add_background_rectangle()
    if threshold:
        close_enough.next_to(dot, UP)
        self.play(FadeIn(close_enough))
        self.wait()

        basically_impossible = Tex(
            r"Finding these points randomly" + "\\\\" + "is extremely unlikely"
        ).scale(0.7)

        basically_impossible.add_background_rectangle()
        basically_impossible.next_to(dot, UP)
        self.play(Transform(close_enough, basically_impossible))
        self.wait()

        return VGroup(dot, label, close_enough)

    return VGroup(dot, label)


class MarchingSquaresUtils(Scene):
    # Utilities class for performing marching squares
    def construct(self):
        pass

    def set_sample_space(
        self,
        x_range=(-7.5, 7.5),
        y_range=(-4, 4),
        x_step=0.5,
        y_step=0.5,
    ):
        """
        @param: x_range - (x_min, x_max) by default the min and max of the screen
        @param: y_range - (y_min, y_max) by default the min and max of the screen
        @param: x_step  - step between samples in x direction
        @param: y_step  - step between samples in y direction
        """
        self.sample_space = []
        self.x_step = x_step
        self.y_step = y_step
        self.x_min = x_range[0]
        self.x_max = x_range[1]
        self.y_min = y_range[0]
        self.y_max = y_range[1]
        for x in np.arange(*self.get_iterable_range(x_range, x_step)):
            for y in np.arange(*self.get_iterable_range(y_range, y_step)):
                self.sample_space.append(np.array([x, y, 0.0]))
        self.sample_space = np.array(self.sample_space)

    def get_sample_space(self):
        """
        Returns current sample space
        """
        return self.sample_space

    def get_iterable_range(self, standard_range, step):
        """
        @param: standard_range: a python range tuple (start, end) with start inclusive, end excluse
        @step: step to sample range
        @return: tuple (start, end, step) where end will include current excluded value
        """
        return (standard_range[0], standard_range[1] + step, step)

    def get_implicit_function_samples(self, func):
        """
        @param: func - the implicit function to sample
        @return: samples of implicit function across sample space
        """
        self.function_map = {}
        for sample_point in self.sample_space:
            result = func(sample_point)
            x, y, _ = sample_point
            self.function_map[(x, y)] = result

        return self.function_map

    def get_dots_based_on_condition(self, condition, radius=0.05):
        """
        @param: condition - function which defines boundary for when point is on surface/contour
        @param: radius - radius of the dot
        @return: VGroup of dots
        """
        self.dot_map = {}
        dots = VGroup()
        for key in self.function_map:
            position = np.array([key[0], key[1], 0])
            if condition(self.function_map[key]):
                dot = Dot(radius=radius, color=INSIDE_COLOR).move_to(position)
            else:
                dot = Dot(radius=radius, color=OUTSIDE_COLOR).move_to(position)
            self.dot_map[key] = dot
            dots.add(dot)
        return dots

    def get_values_of_implicit_f(self, scale=0.3):
        values = VGroup()
        self.decimal_map = {}
        for key in self.function_map:
            value = DecimalNumber(
                number=self.function_map[key], num_decimal_places=2
            ).scale(scale)
            value.next_to(self.dot_map[key], DR, buff=0)
            self.decimal_map[key] = value
            values.add(value)
        return values

    def update_dots(self, condition):
        for key in self.function_map:
            if condition(self.function_map[key]):
                self.dot_map[key].set_color(INSIDE_COLOR)
            else:
                self.dot_map[key].set_color(OUTSIDE_COLOR)

    def update_values(self):
        for key in self.function_map:
            self.decimal_map[key].set_value(self.function_map[key])

    def march_squares(
        self,
        condition,
        implicit_function,
        value=1,
        line_width=2,
        gradient=False,
        fill=False,
        color=CONTOUR_COLOR,
    ):
        contour = VGroup()
        count = 0
        for key in self.function_map:
            if key[1] >= self.y_max:
                continue
            if key[0] >= self.x_max:
                continue

            # if count > 100:
            #     break
            marching_square = self.get_marching_square(key)
            square_corners = marching_square.get_corners()
            case = self.get_case(square_corners, condition, implicit_function)
            # case_integer = Integer(case).scale(0.4)
            # case_integer.move_to(np.mean(square_corners, axis=0))
            # self.add(case_integer)
            lines = self.process_case(
                case,
                marching_square,
                implicit_function,
                value=value,
                width=line_width,
                gradient=gradient,
                fill=fill,
                color=color,
            )
            if lines:
                contour.add(lines)
            # print(case)
            count += 1
        return contour

    def get_marching_square(self, key):
        ul_pos = np.array([key[0], key[1] + self.y_step, 0])
        ur_pos = np.array([key[0] + self.x_step, key[1] + self.y_step, 0])
        dr_pos = np.array([key[0] + self.x_step, key[1], 0])
        dl_pos = np.array([key[0], key[1], 0])
        return MarchingSquare(ul_pos, ur_pos, dr_pos, dl_pos, self.function_map)

    def get_case(self, square_corners, condition, implicit_function):
        bin_string = ""
        for corner in square_corners:
            value = get_func_val_from_map(
                self.function_map, (corner[0], corner[1]), implicit_function
            )
            # print(value)
            if condition(value):
                bin_string += "1"
            else:
                bin_string += "0"
        # print(bin_string)
        return int(bin_string, 2)

    def process_case(
        self,
        case,
        marching_square,
        implicit_function,
        value=1,
        width=2,
        gradient=False,
        fill=False,
        color=CONTOUR_COLOR,
    ):
        """
        Draws lines based on the case of marching cubes
        """
        if fill:
            if case == 0:
                return
            polygons = marching_square.get_polygon_for_case(
                case, implicit_function, value=value, gradient=gradient
            )
            return polygons
        if case == 0 or case == 15:
            return
        lines = marching_square.get_lines_for_case(
            case,
            implicit_function,
            value=value,
            width=width,
            gradient=gradient,
            color=color,
        )
        return lines


class GuessImplicitFunctionValues(MarchingSquaresUtils):
    def construct(self):
        plane = NumberPlane()
        self.play(
            Write(plane),
            run_time=2,
        )
        self.wait()

        # self.contour = self.get_contour(batman_function)

        self.introduce_game()
