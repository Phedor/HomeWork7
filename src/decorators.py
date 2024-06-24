from typing import Any


def log_file(filename: str, text_in_log: str) -> None:
    """
    Функция выдачи лога
    :param filename: Имя файла для логирования, если не указано, то выдаем на конслоь
    :param text_in_log: Строка для выдачи в лог
    :return: Ничего не возвращает
    """
    if filename != '':
        with open("log.txt", "w") as text_file:
            text_file.write(text_in_log)
    else:
        print(text_in_log)


def log(filename: str = '') -> Any:
    """
    Функция декоратор для логирования
    :param filename: Имя файла для лога, если пусто, то выводится на консоль
    :return: Результат
    """
    def decorator(func: object) -> Any:
        """
        Декоратор функции-обертки
        :param func: Функция для обертки
        :return: Возвращает результат выполнения переданной функции
        """
        def wrapper(*args, **kwargs) -> Any:
            """
            Функция получения параметров для обертки
            :param args: Параметры
            :param kwargs: Именнованые аргументы
            """
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_file(filename, f'{func.__name__} error: {e.__class__} Inputs: {args} {kwargs}')
                result = None
            else:
                log_file(filename, f'{func.__name__} ok')
            return result

        return wrapper

    return decorator
