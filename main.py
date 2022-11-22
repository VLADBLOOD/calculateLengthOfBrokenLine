from decimal import Decimal
import math


def get_line_total_length(x_coordinates, y_coordinates):
    points = list(zip(x_coordinates, y_coordinates))
    segments = zip(points[:-1], points[1:])
    return sum_segments([calculate_segment_length(temp_x, temp_y) for temp_x, temp_y in segments])


def calculate_segment_length(point_1, point_2):
    return math.hypot(point_2[0] - point_1[0], point_2[1] - point_1[1])


def sum_segments(distances):
    total_length = Decimal(str(sum(distances)))
    return str(total_length.quantize(Decimal("1.00")))


if __name__ == '__main__':
    print(get_line_total_length([0, 2, 3, 7], [1, 4, -1, 5]))
