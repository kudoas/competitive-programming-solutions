sx, sy, tx, ty = map(int, input().split())
dx, dy = tx-sx, ty-sy

# -をかけると文字が消える
# 左下と右上に限定
cmd1 = 'R' * dx + 'U' * dy
cmd2 = 'L' * dx + 'D' * dy
cmd3 = 'D' + 'R' * (dx+1) + 'U' * (dy+1) + 'L'
cmd4 = 'U' + 'L' * (dx+1) + 'D' * (dy+1) + 'R'
ans = cmd1 + cmd2 + cmd3 + cmd4
print(ans)
