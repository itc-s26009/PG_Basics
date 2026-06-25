# (1) 任意の変数に "three " と "three " と "three" を足し算で結合
text_addition = "three " + "three " + "three"

# (2) 上記の変数をprint文で表示
print("(2) 足し算の結果:")
print(text_addition)

print("-" * 20)  # 区切り線

# (3) 別の任意の変数に "three " を掛け算（3回反復）で結合
# ※元の文字列と同じ状態を作るため3倍にしています
text_multiplication = "three " * 3

# (4) 上記の変数を表示する際に、前後の空白を除去するメソッド（strip）を使う
print("(4) 掛け算 + 空白除去の結果:")
print(text_multiplication.strip())
