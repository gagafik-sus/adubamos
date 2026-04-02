print('adubam calc v0.2')
print('Введите пример (например: 2 + 2)')
primer = input("calc shell: ")
allowed_chars = "0123456789+-*/. ()"
is_safe = all(char in allowed_chars for char in primer)
if is_safe and primer.strip() != "":
    try:
        result = eval(primer)
        print("= " + str(result))
    except Exception:
        print("Ошибка в вычислении")
else:
    print("Можно использовать только эти символы: ", allowed_chars)