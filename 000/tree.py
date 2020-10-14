# 124 105 

# 任何tree的问题都可以用pre/in/post order遍历解决
# 框架
def traverse(TreeNode root) {
    # preorder
    traverse(root.left)
    # inorder
    traverse(root.right)
    # postorder
}

# 扩展到N叉树
def traverse(TreeNode root) {
    for child in root.children:
        traverse(child)
}