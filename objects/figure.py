import pyray
from raylib import colors
from objects.base import BaseObject


class Button(BaseObject):
    def __init__(self, x, y, width, height, text, color=pyray.BLACK, hover_color=pyray.LIGHTGRAY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def logic(self):
        mouse_position = pyray.get_mouse_position()
        return (self.x <= mouse_position.x <= self.x + self.width and
                self.y <= mouse_position.y <= self.y + self.height)

    def draw(self):
        # Определяем цвет в зависимости от состояния кнопки
        current_color = self.hover_color if self.logic() else self.color
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, current_color)

        # Отрисовка текста на кнопке
        text_width = pyray.measure_text(self.text, 40)
        text_x = self.x + (self.width - text_width) // 2
        text_y = self.y + (self.height - 20) // 2
        pyray.draw_text(self.text, text_x, text_y, 40, pyray.RED)

    def check_click(self):
        if self.logic() and pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
            return True
        return False


class Rect(BaseObject):
    def __init__(self, x, y, width, height, color=None, outline=False):
        """
        Класс прямоугольника Raylib.
        """
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color if color else colors.RED
        self.__outline = outline

    def set_size(self, w, h):
        self.__width = w
        self.__height = h

    def draw(self):
        draw_func = pyray.draw_rectangle if not self.__outline else pyray.draw_rectangle_lines
        draw_func(self._x, self._y, self.__width, self.__height, self.__color)


class Circle(BaseObject):
    def __init__(self, x, y, radius, color=None, outline=False):
        """
        Класс круга Raylib.
        """
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color if color else colors.RED
        self.__outline = outline

    def resize(self, radius):
        """
        Меняет радиус круга
        """
        self.__radius = radius

    def set_color(self, color):
        """
        Устанавливает цвет круга
        """
        self.__color = color

    def draw(self):
        draw_func = pyray.draw_circle if not self.__outline else pyray.draw_circle_lines
        draw_func(self._x, self._y, self.__radius, self.__color)


class Ellipse(BaseObject):
    def __init__(self, x, y, radius_w, radius_h, color=None, outline=False):
        """
        Класс эллипса Raylib.
        """
        super().__init__(x, y)
        self.__radius_w = radius_w
        self.__radius_h = radius_h
        self.__color = color if color else colors.RED
        self.__outline = outline

    def resize(self, radius_w, radius_h):
        """
        Меняет радиус эллипса
        """
        self.__radius_w = radius_w
        self.__radius_h = radius_h

    def set_color(self, color):
        """
        Устанавливает цвет эллипса
        """
        self.__color = color

    def draw(self):
        draw_func = pyray.draw_ellipse if not self.__outline else pyray.draw_ellipse_lines
        draw_func(self._x, self._y, self.__radius_w, self.__radius_h, self.__color)
