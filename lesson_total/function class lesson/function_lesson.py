#関数の定義
def reverse_text(text):               #呼び出し側で渡された"さかさことば"をtextに代入して使用
    rtext = text[::-1]                #文字列を逆転させる処理
    print(f"{text} → {rtext}")


reverse_text("さかさことば")           #関数を呼び出す側,引数で"さかさことば"を渡している
reverse_text("とまと")
reverse_text("くるみ")


