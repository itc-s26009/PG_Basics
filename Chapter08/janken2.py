"""
処理しやすくするため、じゃんけんの手に番号を振っておきます
　　1…グー 2…チョキ 3…パー
"""
import random
rsp = ["", "グー", "チョキ", "パー"]  #rsp[0]は使わない
#じゃんけんの手を入力し、任意の変数に代入します
you = int(input("じゃんけんぽん！(グー:1,チョキ:2,パー:3)->") )
#乱数でコンピュータ側の手を決め、任意の変数に代入します
computer = random.randint(1,3)
print(f"あなたの手：{ rsp[you] }　コンピュータ：{ rsp[computer] }" )   
#入力した手コンピュータの手を比較して、勝ち/負け/あいこを判定する
if you == 1:    #グー
    if computer == 1:
        print("あいこです")
    elif computer == 2:
        print("あなたの勝ちです")
    else:
        print("あなたの負けです")
elif you == 2:  #チョキ
    if computer == 1:
        print("あなたの負けです")
    elif computer == 2:
        print("あいこです")
    else:
        print("あなたの勝ちです")
elif you == 3:  #パー
    if computer == 1:
        print("あなたの勝ちです")
    elif computer == 2:
        print("あなたの負けです")
    else:
        print("あいこです")
else:   #入力間違い
    print("1か2か3を入力してください")





#勝負の結果を表示する
"""
勝負の結果を表示する
　　例）
　　「じゃんけんぽん！(グー:1,チョキ:2,パー:3)」
    (1を入力後)
　　「あなた：グー　コンピュータ：パー」
　　「あなたの勝ちです」
"""
