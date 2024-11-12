# TODO Найдите количество книг, которое можно разместить на дискете
ob = 1.44
stra = 100
stk = 50
sim = 25
obs = 4
obvbit = ob * 1024 * 1024
knigi = obvbit // (stra * stk * sim * obs)
knigi = round (knigi)
print("Количество книг, помещающихся на дискету:", knigi)
