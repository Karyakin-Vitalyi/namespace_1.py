# Пространство имен

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываем inner_function внутри test_function
    inner_function()

# Вызываем test_function
test_function()

# Теперь попробуем вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(e)



