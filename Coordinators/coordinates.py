leftdownCoordx1=int(input('Введите координату x левого нижнего угла 1 прямоугольника: '))
leftdownCoordy1=int(input('Введите координату y левого нижнего угла 1 прямоугольника: '))
leftdownCoordx2=int(input('Введите координату x левого нижнего угла 2 прямоугольника: '))
leftdownCoordy2=int(input('Введите координату y левого нижнего угла 2 прямоугольника: '))
ASideLength1=int(input('Введите длину стороны A 1 прямоугольника: '))
BSideLength1=int(input('Введите длину стороны B 1 прямоугольника: '))
ASideLength2=int(input('Введите длину стороны A 2 прямоугольника: '))
BSideLength2=int(input('Введите длину стороны B 2 прямоугольника: '))
if leftdownCoordx1>leftdownCoordx2 and leftdownCoordy1>leftdownCoordy2:
    print(leftdownCoordx1+ASideLength1, leftdownCoordy1+BSideLength1,'- координаты верхнего правого угла прямоугольника')
    print(leftdownCoordx2, leftdownCoordy2, '- координаты нижнего левого угла прямоугольника')
else:
    print(leftdownCoordx2+ASideLength2, leftdownCoordy2+BSideLength2, '- координаты верхнего правого угла прямоугольника')
    print(leftdownCoordx1, leftdownCoordy1, '- координаты нижнего левого угла прямоугольника')

