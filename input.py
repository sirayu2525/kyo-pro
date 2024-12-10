#これはすべての記号を見境なく一つの文字としてリスト化する
b = list(input())
print(b)

#これは空白や改行などわかりやすい区切りでリスト化する
list_c = input().split()
print(list_c)

#これは一列で数字間が空白の時に数字をリスト化する
list_a = list(map(int, input().split()))
print(list_a)

#これは一列で数字間がない時に数字をリスト化する
list_b = list(map(int, list(input())))
print(list_b)

#これは一列で数字間が空白の時に数字をそれぞれの変数に格納
n, a, b = map(int, input().split())

#これはN行の入力をリストにまとめるもの
N = int(input())
x = [int(input()) for i in range(N)]
print(x)