N = 12

def inOrder(n):
    if n > N:
        return

    inOrder(n * 2)
    print(n, end=" ")
    inOrder(n * 2 + 1)



def postOrder(n):
    if n > N:
        return

    postOrder(n * 2)
    postOrder(n * 2 + 1)
    print(n, end=" ")


print(N)
inOrder(1)
print()
postOrder(1)

