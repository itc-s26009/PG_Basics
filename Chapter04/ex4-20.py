a = input("何か数字を入力してください")
b = input("さっきとは別の数字を入力してください")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("ゼロの入力はナシでお願いします")

