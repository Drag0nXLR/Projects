class Widget:
    """Class Widget"""
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def print_info(self):
        print(f"Text: {self.text}\nCoordinates: ({self.x}, {self.y})")

class Button(Widget):
    def __init__(self, x, y, text, is_clicked=False):
        super().__init__(x,y,text)
        self.clicked = is_clicked
    def click(self):
        self.clicked = True
    def print_info(self):
        print(f'Clicked: {self.clicked}')
        return super().print_info()
    
widget = Widget(10, 10, 'Test')
widget.print_info()
button = Button(30, 40, "Test")
button.print_info()
ans = input('Do you want register? (Y/n)')
if ans:
    if ans == 'Y':
        print('Ви зареєстровані')
        button.click()
        button.print_info()
    elif ans == 'n':
        print('До побачення!')
else:
    print('До побачення!')