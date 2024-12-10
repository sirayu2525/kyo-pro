# 幅優先探索（https://atcoder.jp/contests/abc007/tasks/abc007_3）

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

# スタート地点とゴール地点を0インデックスに変換（座標⇒行と列）
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# マップの読み込み
maze = [input() for i in range(r)]

# 移動方向
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# BFSの実装
def bfs(start_y,start_x,goal_y,goal_x):
    que = [(start_y,start_x, 0)] # (y,x,steps)
    visited = set()
    visited.add((start_y,start_x))

    while que:
        # キューの先頭を取り出し
        y,x,steps = que.pop(0)

        #　ゴールに到達した場合
        if y == goal_y and x == goal_x:
            return steps
        
        # 4方向に移動
        for dy,dx in directions:
            ny, nx = y + dy, x + dx
            if maze[ny][nx] != "#" and (ny, nx) not in visited:
                que.append((ny,nx,steps+1)) # キューに追加
                visited.add((ny,nx))
    return -1 # ゴールにたどり着けない場合

# BFSを実行して結果を表示
result = bfs(sy, sx, gy, gx)
if result != -1:
    print(result)

# # dequeを使うBFS

# from collections import deque

# # 入力の受け取り
# R, C = map(int, input().split())  # グリッドの行数と列数
# sy, sx = map(int, input().split())  # スタート地点
# gy, gx = map(int, input().split())  # ゴール地点

# # 盤面データの入力
# maze = [input().strip() for _ in range(R)]

# # スタート地点とゴール地点を0インデックスに変換
# sy -= 1
# sx -= 1
# gy -= 1
# gx -= 1

# # 移動方向 (上下左右)
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# # 幅優先探索 (BFS) の実装
# def bfs(start_y, start_x, goal_y, goal_x):
#     # キューをdequeで管理
#     queue = deque([(start_y, start_x, 0)])  # (y, x, steps)
#     visited = [[False] * C for _ in range(R)]  # 訪問済みを記録
#     visited[start_y][start_x] = True
    
#     while queue:
#         y, x, steps = queue.popleft()  # キューの先頭を取り出し

#         # ゴールに到達した場合
#         if y == goal_y and x == goal_x:
#             return steps

#         # 4方向に移動
#         for dy, dx in directions:
#             ny, nx = y + dy, x + dx

#             # 範囲内かつ空きマスで未訪問の場合
#             if 0 <= ny < R and 0 <= nx < C and maze[ny][nx] == '.' and not visited[ny][nx]:
#                 queue.append((ny, nx, steps + 1))  # キューに追加
#                 visited[ny][nx] = True  # 訪問済みにする

#     return -1  # 到達不能な場合（ただしこの問題では発生しない）

# # BFSを実行して結果を表示
# result = bfs(sy, sx, gy, gx)
# print(result)
