class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # метод вычисления площади
    def square(self):
        return self.width * self.height

    # метод вычисления периметра
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle_1 = Rectangle(3, 4)
rectangle_2 = Rectangle(5, 6)
rectangle_3 = Rectangle(7, 2)

print(f'1-ый прямоугольник: площадь = {rectangle_1.square()}, периметр = {rectangle_1.perimeter()}')
print(f'2-ой прямоугольник: площадь = {rectangle_2.square()}, периметр = {rectangle_2.perimeter()}')
print(f'3-ий прямоугольник: площадь = {rectangle_3.square()}, периметр = {rectangle_3.perimeter()}')

print('\n')

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # метод сложения
    def addition(self):
        return self.a + self.b

    # метод вычитания
    def subtraction(self):
        return self.a - self.b

    # метод умножения
    def multiplication(self):
        return self.a * self.b

    # метод деления
    def division(self):
        return self.a / self.b

digits = Math(6, 3)
print(f'{digits.a} + {digits.b} = {digits.addition()}')
print(f'{digits.a} - {digits.b} = {digits.subtraction()}')
print(f'{digits.a} * {digits.b} = {digits.multiplication()}')
print(f'{digits.a} / {digits.b} = {digits.division()}')

print('\n')

class SidebarButtons:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.locator = ''

    def click(self):
        return f'Клик по кнопке {self.text}'

buttons = [
    SidebarButtons('Text Box'),
    SidebarButtons('Check Box'),
    SidebarButtons('Radio Button'),
    SidebarButtons('Web Tables'),
    SidebarButtons('Buttons'),
    SidebarButtons('Links'),
    SidebarButtons('Broken Links - Images'),
    SidebarButtons('Upload and Download'),
    SidebarButtons('Dynamic Properties')
]

for button in buttons:
    print(f'Текст: {button.text}')
    print(button.click())
