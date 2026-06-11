matsumoto = {
        "名前": "松本空",
        "好きな色": "青",
        "好きな作家": "理不尽な孫の手",
}

ask = input("知りたい特徴を入力してください->")
if ask in matsumoto:
    print(matsumoto)
else:
    print("それはわからないです。こんど聞いておきますね")
