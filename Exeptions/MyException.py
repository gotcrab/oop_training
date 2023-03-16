class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyException ({self.message})'
        return 'MyException is Empty'

raise MyException('this is error', 666)
