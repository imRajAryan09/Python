from manim import *

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.get_graph(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.get_graph(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        area_1 = ax.get_area(curve_1, x_range=[0.3, 0.6], dx_scaling=40, color=BLUE)
        area_2 = ax.get_area(curve_2, [2, 3], bounded=curve_1, color=GREY, opacity=0.2)

        self.add(ax, labels, curve_1, curve_2, line_1, line_2, area_1, area_2)