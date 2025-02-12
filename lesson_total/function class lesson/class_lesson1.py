
class ReversedText:                             #クラス名を定義

    def __init__(self, text):                   #引数selfとtextを受け取る初期化メソッド
        self.sorce = text                       #インスタンス変数sorceにtextを代入して使用
        self.reversed = text[::-1]              #インスタンス変数reversednitextに文字列を反転させた値を代入して使用
        
    def is_plindrome(self):                     #回文かどうかの判定をする関数
        return self.sorce == self.reversed     
    
    def __str__(self):                          #反転した文字列を返す関数
        return self.reversed
