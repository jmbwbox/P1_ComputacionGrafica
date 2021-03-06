import Point


class Line:

    def __init__(self, start_point, end_point):
        if start_point.x < end_point.x:
            self.start_point = start_point
            self.end_point = end_point
            self.y_len = int(self.end_point.y - self.start_point.y)
            self.x_len = int(self.end_point.x - self.start_point.x)
            self.slope = float(self.y_len) / float(self.x_len)

        elif start_point.x > end_point.x:
            self.start_point = end_point
            self.end_point = start_point
            self.y_len = int(self.end_point.y - self.start_point.y)
            self.x_len = int(self.end_point.x - self.start_point.x)
            self.slope = float(self.y_len) / float(self.x_len)

        else:
            self.start_point = start_point
            self.end_point = end_point
            self.y_len = int(end_point.y - start_point.y)
            self.x_len = 0
            self.slope = None

        self.name = self.start_point.name + self.end_point.name

    def get_digital_discretion(self):
        x_k = None
        y_k = None
        digital_difference_analysis = []

        if self.slope is None:
            for k in range(abs(self.y_len)+1):

                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue

                digital_difference_analysis.append(Point.Point(x_k, y_k + 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif -1 <= self.slope <= 1:
            for k in range(self.x_len+1):

                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue

                digital_difference_analysis.append(Point.Point(x_k + 1, y_k + self.slope, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif self.slope > 1:
            for k in range(self.y_len+1):

                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue

                digital_difference_analysis.append(Point.Point(x_k + 1/self.slope, y_k + 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif self.slope < -1:
            for k in range(abs(self.y_len)+1):

                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue

                digital_difference_analysis.append(Point.Point(x_k + 1/abs(self.slope), y_k - 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        return digital_difference_analysis

    def get_dimensions(self):
        if abs(self.start_point.x) > abs(self.end_point.x):
            x_min = -abs(self.start_point.x) - 7
            x_max = abs(self.start_point.x) + 7
        elif abs(self.start_point.x) < abs(self.end_point.x):
            x_min = -abs(self.end_point.x) - 7
            x_max = abs(self.end_point.x) + 7
        else:
            x_min = -abs(self.start_point.x)-7
            x_max = abs(self.start_point.x)+7

        if abs(self.start_point.y) > abs(self.end_point.y):
            y_min = -abs(self.start_point.y) - 7
            y_max = abs(self.start_point.y) + 7
        elif abs(self.start_point.y) < abs(self.end_point.y):
            y_min = -abs(self.end_point.y) - 7
            y_max = abs(self.end_point.y) + 7
        else:
            y_min = -abs(self.start_point.y)-7
            y_max = abs(self.start_point.y)+7

        return [x_min, x_max, y_min, y_max]

    def get_bresenham_discretion(self):
        k = 0
        x_k = self.start_point.x
        y_k = self.start_point.y


        if 0 < self.slope <= 1:
            p_k = 2 * abs(self.y_len) - self.x_len

            bresenham_data = [Point.Point(self.start_point.x, self.start_point.y, str(k))]
            k += 1
            for point in range(self.x_len):
                new_values = self.get_decision_parameter(p_k, x_k,y_k,self.y_len,self.x_len,1,1)
                x_k = new_values[0]
                y_k = new_values[1]
                p_k = new_values[2]
                bresenham_data.append(Point.Point(x_k, y_k, str(k)))
                k += 1

        elif 0 > self.slope >= -1:
            p_k = 2 * abs(self.y_len) - self.x_len

            bresenham_data = [Point.Point(self.start_point.x, self.start_point.y, str(k))]
            k += 1
            for point in range(self.x_len):
                new_values = self.get_decision_parameter(p_k, x_k,y_k,abs(self.y_len),self.x_len, 1, -1)
                x_k = new_values[0]
                y_k = new_values[1]
                p_k = new_values[2]
                bresenham_data.append(Point.Point(x_k, y_k, str(k)))
                k += 1

        elif self.slope > 1:
            p_k = 2 * abs(self.x_len) - abs(self.y_len)

            bresenham_data = [Point.Point(self.start_point.x, self.start_point.y, str(k))]
            k += 1
            for point in range(abs(self.y_len)):
                new_values = self.get_decision_parameter(p_k, y_k, x_k, abs(self.x_len), abs(self.y_len), 1, 1)
                x_k = new_values[1]
                y_k = new_values[0]
                p_k = new_values[2]
                bresenham_data.append(Point.Point(x_k, y_k, str(k)))
                k += 1

        elif self.slope < -1:
            p_k = 2 * abs(self.x_len) - abs(self.y_len)

            bresenham_data = [Point.Point(self.start_point.x, self.start_point.y, str(k))]
            k += 1
            for point in range(abs(self.y_len)):
                new_values = self.get_decision_parameter(p_k, y_k, x_k, abs(self.x_len), abs(self.y_len), -1 , 1)
                x_k = new_values[1]
                y_k = new_values[0]
                p_k = new_values[2]
                bresenham_data.append(Point.Point(x_k, y_k, str(k)))
                k += 1

        return bresenham_data

    @staticmethod
    def get_decision_parameter(old_p, x_k, y_k, y_len, x_len, x, y):
        if old_p < 0:
            new_x = x_k + x
            new_y = y_k
            p_k = old_p + 2*y_len
        else:
            new_x = x_k + x
            new_y = y_k + y
            p_k = old_p + 2*y_len - 2*x_len
        return [new_x, new_y, p_k]

AB = Line(Point.a, Point.b)
#  print(AB.start_point.x, AB.end_point.y, AB.slope)
point_array = AB.get_digital_discretion()
#  for point in point_array:
#      print(point)
