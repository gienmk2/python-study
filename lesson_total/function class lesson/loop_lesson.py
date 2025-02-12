#内包表記（繰り返し処理を使ってリストを作る文法）下記はfor文のようだがfor句という
numlist = [f"{x}点" for x in range(10, 100, 10)]
print(numlist)


#上記の内包表記を普通のfor文で書いた場合
numlist = []
for x in range(10, 100, 10):
    numlist.append(f"{x}点")
print(numlist)


#continnueを使った処理（処理を一回スキップする）
numlist = [40, -10, 83, -2, 15]
for x in numlist:
    if x < 0:
        continue
    print(f"値は{x}")


#whileを使った無限ループ（プロンプトに数字を入力）
total = 0
while True:
    text = input("数字を入力 (0で終了)")
    #数字の０かfloatの数字が入力されたらループ終了
    if text == "0":
        break
    if text.isdigit() == False:
        break
    total += int(text)
    print(total)


