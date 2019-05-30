def swapList(List):

    List[0], List[-1] = List[-1], List[0]

    return List


x = input().split(",")
y = len(x)

List = []

for i in range(0, y):
    List.append(x[i])


print(swapList(List))
