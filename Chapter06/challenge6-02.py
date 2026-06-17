# (1) 任意の変数にinput文で文字列をセットする
first_word = input("1つ目の文字を入力してください: ")

# (2) 上記(1)とは違う別の変数にinput文で文字列をセットする
second_word = input("2つ目の文字を入力してください: ")

# (3) print文で表示する際に、書式化操作のメソッドを使って値を指定する
print("入力されたのは「{}」と「{}」です。".format(first_word, second_word))
