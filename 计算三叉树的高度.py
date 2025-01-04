
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = self.mid = None


class Ternary_Search_Trie:

    def get_height(self,root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        mid_height = self.get_height(root.mid)
        return max(left_height,right_height,mid_height) +1

    def insert_value(self,root,val):
        if not root:
            return TreeNode(val)
        if val < root.val - 500:
            root.left = self.insert_value(root.left, val)

        elif  root.val - 500 <= val <= root.val + 500:
            root.mid = self.insert_value(root.mid,val)

        elif val > root.val + 500:
            root.right = self.insert_value(root.right, val)

        return root


if __name__ == '__main__':
    tree = Ternary_Search_Trie()
    N = int(input())
    numbers = list(map(int,input().split()))
    root = None
    for num in numbers:
        root = tree.insert_value(root,num)

    height = tree.get_height(root)
    print(height)



