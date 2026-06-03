try:
    a = input("何か数字を入力してください")
    b = input("さっきとは別の数字を入力してください")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("正しい値を入力してください")

