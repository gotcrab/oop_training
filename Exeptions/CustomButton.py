class CustomButton:
    def __init__(self, text: str, **kwargs):
        self.text = text
        for i, j in kwargs.items():
            setattr(self, i, j)

    def config(self, **kwargs):
        for i, j in kwargs.items():
            setattr(self, i, j)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')


if __name__ == '__main__':
    d = CustomButton('Go', sl=5, t=9)
    print(d.__dict__)
    d.config(m=6, sl=56)
    print(d.__dict__)


    def func():
        print('Оно живое')


    btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
    btn.click()  # Кнопка не настроена
    btn.config(command=func)
    btn.click()  # Оно живое
