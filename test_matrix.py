array0 = [ [ 0, 0, 0], [ 0, 0, 0], [0, 0, 0] ]
array1 = [ [ 1, 2, 3], [ 4, 5, 6], [7, 8, 9] ]


m0 = Matrix(array0)
m1 = Matrix(array1)
m2 = Matrix(array1)

print("m0:")
m0.print()

print("m1:")
m1.print()

print("m2:")
m2.print()

m2.mulc(2)
print("m2:")
m2.print()

class MyMatrix(Matrix):
    def print(self):
        for y in range(self._dy):
            for x in range(self._dx):
                if self._array[y][x] == 0:
                    print("□", end='')
                elif self._array[y][x] == 1:
                    print("■", end='')
                else:
                    print("XX", end='')
            print()

m8 = MyMatrix(array0)
m8.print()

m9 = MyMatrix(array1)
m9.print()


try:
    m3 = m1.clip(1, 1, 3, 3)
    print("m3:")
    m3.print()

    array2 = [ [ 0, 0], [ 0, 0] ]
    m4 = Matrix(array2)
    m1.paste(m4, 1, 1)
    print("m1:")
    m1.print()
   
except MatrixError as e:
    print(e)

m5 = m1 + m0
print("m5:")
m5.print()


print('nAlloc = %d' % m1.get_nAlloc())
print('nFree = %d' % m1.get_nFree())

