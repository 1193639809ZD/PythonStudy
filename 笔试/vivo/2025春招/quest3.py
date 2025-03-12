"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-07 16:17:51
lastModified:  2025-03-07 16:17:52
"""

# 问题：给定一个数组data，每次取出并移除2个数，使这两个数满足异或值最大，如果有多组数可以取得最大值，则优先取数组中靠前的数，请问第二次取出的数的异或值是多少


class TrieNode:
    def __init__(self):
        self.children = [None, None]  # 0 和 1 的子节点
        self.index = -1  # 存储数的索引


class BinaryTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num, index):
        node = self.root
        for i in range(31, -1, -1):  # 从最高位到最低位
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.index = index

    def find_max_xor(self, num, data):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # 尽量走相反的位
            if node.children[1 - bit]:
                node = node.children[1 - bit]
            elif node.children[bit]:
                node = node.children[bit]
            else:
                break
        return data[node.index] ^ num, node.index


def optimized_second_xor(data):
    if len(data) < 4:
        return "数组长度不足，无法进行两次取数"

    # 第一次取数
    trie = BinaryTrie()
    for i in range(len(data)):
        trie.insert(data[i], i)

    max_xor = -1
    first_pair = None
    for i in range(len(data)):
        xor_val, j = trie.find_max_xor(data[i], data)
        if xor_val > max_xor:
            max_xor = xor_val
            first_pair = (i, j) if i < j else (j, i)  # 保证靠前索引优先

    # 移除第一次取出的数
    remaining = [data[i] for i in range(len(data)) if i != first_pair[0] and i != first_pair[1]]
    print(f"第一次取出: {data[first_pair[0]]}, {data[first_pair[1]]}, 异或值: {max_xor}")
    print(f"剩余数组: {remaining}")

    # 第二次取数
    if len(remaining) < 2:
        return "剩余元素不足，无法进行第二次取数"

    trie = BinaryTrie()
    for i in range(len(remaining)):
        trie.insert(remaining[i], i)

    max_xor_second = -1
    second_pair = None
    for i in range(len(remaining)):
        xor_val, j = trie.find_max_xor(remaining[i], remaining)
        if xor_val > max_xor_second:
            max_xor_second = xor_val
            second_pair = (i, j) if i < j else (j, i)

    print(f"第二次取出: {remaining[second_pair[0]]}, {remaining[second_pair[1]]}, 异或值: {max_xor_second}")
    return max_xor_second


# 测试示例
data = [1, 2, 3, 4]
result = optimized_second_xor(data)
print(f"第二次取出的数的异或值: {result}")

data2 = [1, 2, 3, 4, 5]
result2 = optimized_second_xor(data2)
print(f"第二次取出的数的异或值: {result2}")
