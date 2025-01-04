
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = self.mid = None


class Ternary_Search_Trie:

    def get_height(self):
        pass

    def insert_value(self,root,val):
        if not root:
            return TreeNode(val)
        if val < root.val -500:
            self.insert_value(root.left,val)

        elif  root.val -500 < val < root.val +500:
            self.insert_value(root.mid,val)

        elif val > root.val +500:
            self.insert_value(root.right,val)

        return root


if __name__ == '__main__':
    tree = Ternary_Search_Trie()
    N = int(input())
    numbers = list(map(int,input().split()))
    root = None
    for num in numbers:
        tree.insert_value(root,num)

