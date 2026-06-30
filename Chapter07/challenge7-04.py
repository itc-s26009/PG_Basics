# (1) 任意のリストに数値を任意の数だけセットする
secret_numbers = [3, 7, 15, 24, 42]

# (2) while文で処理を繰り返す
while True:
    # ① input文で入力を受け付け、変数にセットする
    user_input = input("数字を入力してください('q'で終了): ")
    
    # ② 半角英字の"q"が入力されたらwhileのループを終了する
    if user_input == 'q':
        print("終了します。")
        break
        
    # ③ 例外エラーが発生するかどうかで処理を分ける
    try:
        # 入力された文字列を整数値に変換
        guess = int(user_input)
        
    except ValueError:
        # ④ 例外エラーが発生したら（数字や'q'以外が入力された場合）
        print("数字か'q'を入力してください")
        
    else:
        # ⑤ 例外エラーが出なければ（無事に整数に変換できたら）以下の処理を行う
        # a) 入力値がリストにあれば「正解」
        if guess in secret_numbers:
            print("正解")
        # b) 入力値がリストになければ「不正解」
        else:
            print("不正解")
