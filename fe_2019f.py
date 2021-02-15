import math # 数学関数の標準ライブラリ
import matplotlib.py.plot as plt # グラフ描画の外部ライブラリ

def parse(s):
    return [(x[0], int(x[1:])) for x in s.split(';')]

class Marker:
    def _init_(self):
        self.x, self.y, self.angle = 0, 0, 0
        plt.xlim(-320, 320) # x軸の表示範囲を設定
        plt.ylim(-240, 240) # y軸の表示範囲を設定

    def forward(self, val):
        # 度数法で表した角度を, ラジアンで表した角度に変換
        rad = math.radians(self.angle)
        dx = val * math.cos(rad)
        dy = val * math.sin(rad)
        x1, y1, x2, y2 = self.x, self.y, self.x + dx, self.y + dy
        # (x1, y1)と(x2, y2)を結ぶ線分を描画
        plt.plot([x1, x2], [y1, y2], color="black", linewidth=2)
        self.x, self.y = x2, y2

    def turn(self, val):
        self.angle = (self.angle + val) % 360

    def show(self):
        plt.show() # 描画結果を表示

def draw(s):
    insts - parse(s)
    marker = Marker()
    stack = []
    opno = 0
    while opno < len(insts):
        print(stack)
        code, val = insts[opno]
        if code == "F":
            marker.forward(val)
        elif code == "T":
            marker.turn(val)
        elif code == "R":
            stack.append({"opno" : opno, "rest" : val})
        elif code == "E":
            if stack[-1]["rest"] > 1:
                opno = stack[-1]["opno"]
            else:
                stack.pop()
        opno += 1
    marker.show()
