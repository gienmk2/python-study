from class_lesson1 import ReversedText           #classを呼び出し
    
rtext1 = ReversedText("さかさことば")             #インスタンスを作成して変数rtext1に代入
if rtext1.is_plindrome():
    print(f"{rtext1.sorce} → {rtext1} 「{rtext1.sorce}」は回文です")
else:
    print(f"{rtext1.sorce} → {rtext1} 「{rtext1.sorce}」は回文ではありません")

rtext2 = ReversedText("とまと")
if rtext2.is_plindrome():
    print(f"{rtext2.sorce} → {rtext2} 「{rtext2.sorce}」は回文です")
else:
    print(f"{rtext2.sorce} → {rtext2} 「{rtext2.sorce}」は回文ではありません")

rtext3 = ReversedText("たけやぶやけた")
if rtext3.is_plindrome():
    print(f"{rtext3.sorce} → {rtext3} 「{rtext3.sorce}」は回文です")
else:
    print(f"{rtext3.sorce} → {rtext3} 「{rtext3.sorce}」」は回文ではありません")