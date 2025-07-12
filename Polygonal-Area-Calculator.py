class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        output = f'Rectangle(width={self.width}, height={self.height})'
        return output

    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        picture = ''

        for _ in range(self.height):
            for _ in range(self.width):
                picture+='*'
            picture+='\n'
        return picture

    def get_amount_inside(self, shape):
        if not isinstance(shape, Rectangle):
            return 'invalid shape'
        if self.height < shape.height or self.width < shape.width:
            return 0
        return self.width//shape.width * self.height//shape.height

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        output = f'Square(side={self.width})'
        return output
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        
    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height
    
    

rectangle = Rectangle(15, 10)
square = Square(7)
insert_rec = Rectangle(2, 3)
insert_sqr = Square(5)
'''
print(rectangle)
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.get_diagonal())
print(rectangle.get_picture())'''
print(rectangle.get_amount_inside(insert_rec))
print(rectangle.get_amount_inside(insert_sqr))
'''
print(square)
print(square.get_area())
print(square.get_perimeter())
print(square.get_diagonal())
print(square.get_picture())'''
print(square.get_amount_inside(insert_rec))