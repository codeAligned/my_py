def tower_builder(n_floors):
    piramid = []
    f = n_floors*2-1
    for i in range(n_floors):
        piramid.append(' '*((f-(i*2+1))//2)+'*'*(i*2+1)+' '*((f-(i*2+1))//2))
    return piramid


n = 5
a = tower_builder(n)
print(a)
