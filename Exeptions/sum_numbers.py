def sum_numbers(numbers: list) -> int:
    check_list(numbers)
    check_exist(numbers)
    check_num(numbers)
    return sum(numbers)

def check_list(lst: list) -> bool:
    if not isinstance(lst, list):
        raise TypeError('Аргумент numbers должен быть списком')

def check_exist(something):
    if not something:
        raise ValueError("Пустой список")

def check_num(num):
    for i in num:
        if not isinstance(i, (int, float)):
            raise TypeError('Неправильный тип элемента')



if __name__ == '__main__':
    # check_list(['fff'])
    # check_list([])
    # check_exist(['w'])
    # check_num([1,2,'3'])
    a = ['w',2]
    print(sum_numbers(a))

