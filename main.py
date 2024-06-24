from src.decorators import log


@log(filename="log.txt")
def my_function(x, y):
    return x / y


@log(filename="")
def my_function_console(x, y):
    return x / y


def main() -> None:
    print('Записывем лог в файл log.txt')
    print(my_function(2, 0))
    print('Теперь выводим тоже на консоль')
    print(my_function_console(2, 0))


if __name__ == "__main__":
    main()
