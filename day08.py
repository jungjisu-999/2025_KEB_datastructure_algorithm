class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None
    node = TreeNode()
    node.data = numbers[0]
    root = node
    for group in numbers[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move
    print("BST 구성 완료")
    find_group = int(input())
    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right
def dfs(g, i, visited):
    visited[i] = 1
    print(visited)
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
visited = [0] * len(graph)
dfs(graph, 4, visited)
"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1] E
[0, 0, 1, 0, 1] C
[1, 0, 1, 0, 1] A
[1, 0, 1, 1, 1] D
D -> A -> C
[1, 1, 1, 1, 1] B
B -> C -> E
"""

