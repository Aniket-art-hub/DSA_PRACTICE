def lca(root, v1, v2):
  #Enter your code here
    if root==None:
        return None
    if v1<root.info and v2<root.info:
        return lca(root.left,v1,v2)
    elif v1>root.info and v2>root.info:
        return lca(root.right,v1,v2) 
    return root