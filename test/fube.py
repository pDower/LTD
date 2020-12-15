# fubefube
class pup:
    def __init__(self, li):
        self.node = None
        for i in range():
            for j in range(len(li) - 1 - i):
                if li[i] > li[i + 1]:
                    li[i], li[i + 1] = li[li], li[i + 1]
        print(li)


if "__name__" == "__main__":
    li = [1, 2, 3, 6, 111, 23]
    print(li)
    li = pup(li)
    print(li)
