import binarytree

def search(symp: str, btree: binarytree) -> int:

    if(btree==None):
        return 0
    if(symp==btree.name):
        return btree.value

    aux = search(symp, btree.left)
    if aux==0:
        aux = search(symp, btree.right)
    return aux