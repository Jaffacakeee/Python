A = [5, 12, 72, 55, 89]

A = A + [1]
print(A)

A = A + ["BCD"]
A = A + list("BCD")
print(A)

A = A + list(str(123))
print(A)

B = [5, 12, 72, 55, 89] 
B = B + [[5, 6, 7, 8]]
B.append([1, 2, 3, 4])
B.insert(3, 100)
B.insert(2,[100, 200, 300])
B[0] = 5
print(B)


