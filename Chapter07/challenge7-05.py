# (1) 2つのリストをセットする（例として2つの数値リストを作成）
list1 = [1, 2, 3]
list2 = [10, 20]

# (2) 計算結果を格納するための空のリストを用意する
result_list = []

# (3) 外側のループ：1つめのリストの値を取得
for x in list1:
    
    # ① 内側のループ：2つめのリストの値を取得
    for y in list2:
        
        # a) 外側の値(x)と内側の値(y)を乗算する
        calc_result = x * y
        
        # b) 計算した値を(2)のリストに追加する
        result_list.append(calc_result)
        
        # c) list2の要素すべてに対して繰り返す

    # ② list1の要素すべてに対して繰り返す

# (4) 完成したリストを表示する
print(result_list)
