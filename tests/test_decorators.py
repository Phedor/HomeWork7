from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x % y

@log()
def my_function_console(x, y):
    return x % y

def test_log():
    assert my_function(2, 1) == 0
    assert my_function(3, 2) == 1
    assert my_function(5, 0) is None
    assert my_function_console(2, 1) == 0
    assert my_function_console(3, 2) == 1
    assert my_function_console(5, 0) is None
