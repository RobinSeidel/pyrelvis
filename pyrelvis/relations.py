import cairo
import math
import random
from operator import itemgetter


class RelationPresenter:
    def __init__(
        self,
        path,
        width=700,
        radius=280,
        font_size=28,
        line_width=2,
        arrow_angle=160,
        arrow_length=20,
    ):
        self.path = path
        self.radius = radius
        self.font_size = font_size
        self.width = width
        self.line_width = line_width
        self.arrow_angle = arrow_angle
        self.arrow_length = arrow_length

        self.surface = cairo.SVGSurface(path, width, width)
        self.ctx = cairo.Context(self.surface)
        self.ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        self.ctx.set_source_rgb(1, 1, 1)
        self.ctx.select_font_face(
            "Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD
        )
        self.ctx.set_font_size(font_size)
        self.ctx.set_line_width(line_width)
        self.ctx.paint()
        self.ctx.set_source_rgb(0, 0, 0)

    def close(self):
        if self.surface:
            self.surface.finish()
            self.ctx = self.surface = None

    def __arrow(self, theta, n_from, n_to):
        x1, y1 = self.__get_node(n_from, theta)
        x2, y2 = self.__get_node(n_to, theta)
        if n_from == n_to:
            self.ctx.move_to(x1 - 6, y1 - 12)
            self.ctx.curve_to(x1 - 20, y1 - 30, x1 + 20, y1 - 30, x1 + 6, y1 - 12)
            self.ctx.move_to(x1 + 6, y1 - 12)
            self.ctx.line_to(x1 + 5, y1 - 17)
            self.ctx.move_to(x1 + 6, y1 - 12)
            self.ctx.line_to(x1 + 11, y1 - 14)
            self.ctx.stroke()
            return
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        vector_x = (x2 - x1) / length
        vector_y = (y2 - y1) / length
        start_x = x1 + 30 * vector_x
        start_y = y1 + 30 * vector_y
        end_x = x2 - 30 * vector_x
        end_y = y2 - 30 * vector_y
        self.ctx.move_to(start_x, start_y)
        self.ctx.line_to(end_x, end_y)

        px1 = vector_x * math.cos(math.radians(self.arrow_angle)) - vector_y * math.sin(
            math.radians(self.arrow_angle)
        )

        py1 = vector_x * math.sin(math.radians(self.arrow_angle)) + vector_y * math.cos(
            math.radians(self.arrow_angle)
        )

        px2 = vector_x * math.cos(
            math.radians(-self.arrow_angle)
        ) - vector_y * math.sin(math.radians(-self.arrow_angle))

        py2 = vector_x * math.sin(
            math.radians(-self.arrow_angle)
        ) + vector_y * math.cos(math.radians(-self.arrow_angle))

        arrow_x1 = end_x + self.arrow_length * px1
        arrow_y1 = end_y + self.arrow_length * py1
        arrow_x2 = end_x + self.arrow_length * px2
        arrow_y2 = end_y + self.arrow_length * py2

        self.ctx.move_to(end_x, end_y)
        self.ctx.line_to(arrow_x1, arrow_y1)
        self.ctx.move_to(end_x, end_y)
        self.ctx.line_to(arrow_x2, arrow_y2)
        self.ctx.stroke()

    def __get_node(self, node, theta):
        angle = -theta * node + 0.5 * math.pi
        x = self.radius * math.cos(angle) + self.width / 2
        y = self.radius * math.sin(angle) + self.width / 2
        return (x, y)

    def print_nodes(self, count):
        theta = 2 * math.pi / count
        _, _, text_width, text_height, _, _ = self.ctx.text_extents("5")
        for node in range(1, count + 1):
            x, y = self.__get_node(node, theta)
            self.ctx.move_to(x - 0.5 * text_width, y + 0.5 * text_height)
            self.ctx.show_text(str(node))

    def print_relation(self, relation, min_nodes=4):
        count = max(min_nodes, max(list(relation), key=itemgetter(1))[0])
        if not isinstance(relation, set):
            raise ValueError("Relation must be a set of tuples")
        for entry in relation:
            if not isinstance(entry, tuple):
                raise ValueError("Relation must be a set of tuples")
            self.__arrow(2 * math.pi / count, entry[0], entry[1])

    def print(self, relation, count):
        self.print_nodes(count)
        self.print_relation(relation, count)


def rel_to_svg(path, relation, min_nodes=4):
    presenter = RelationPresenter(path)
    presenter.print(relation, min_nodes)
    presenter.close()


if __name__ == "__main__":
    rel = set()
    for _ in range(5):
        rel.add((random.randint(1, 4), random.randint(1, 4)))
    rel_to_svg("out.svg", rel)
