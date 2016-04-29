# coding : utf-8

# 円の中心座標から見て、絶対値rだけx軸またはy軸方向に移動した点が、
# それぞれ長方形の幅(w)または高さ(h)より小さく、かつ0以上であれば、
# 円は長方形の中にあるといえる。
def is_inner_rectangle(x, y, w, h, r):
    def helper(i, j, r):
        if 0 <= i + r <= j and 0 <= i - r <= j:
            return True

    return helper(x, w, r) and helper(y, h, r)


w, h, x, y, r = [int(i) for i in input().rstrip().split(" ")]
print("Yes" if is_inner_rectangle(x, y, w, h, r) else "No")
