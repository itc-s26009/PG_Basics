# (1) 任意のリストをセットする（例として曜日のリストを作成）
days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]

# (2) for文でenumerate関数を使ってインデックス値と要素を取得する
# (3) 取得したインデックス値と要素をformat関数（またはf文字列）で表示する
for index, element in enumerate(days):
    # format関数を使う場合
    print("インデックス: {}, 要素: {}".format(index, element))
