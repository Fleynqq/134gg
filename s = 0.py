# put your python code h
print("Здравствуй, мир!")

# put your python code here
print("4 8 15 16 23 42")

# put your python code here
print("4")
print("8")
print("15")
print("16")
print("23")
print("42")

print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

a=input()
print(a,'- чемпион!')
a = input()
b = input()
v = input()
print(a)
print(b)
print(v)

# put your python code here
s = input()
b = input()
d = input()
print(d)
print(b)
print(s)

print('I', 'like', 'Python', sep='***')
a = input()
b = input()
c = input()
d = input()
print(b, c, d, sep=a)

a=input()
print('Привет,', a, end='!')

a=int(input())
c=1
b=+2
print(a)
print(a+c)
print(a+b)

a=int(input())
c=int(input())
b=int(input())
print(a+c+b)

a=int(input())
print ('Объем =', a**3)
print ('Площадь полной поверхности =', a*a*6)

a = int(input())
b = int(input())
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41)

a=int(input())
print('Следующее за числом', a, 'число:', a +1)
print('Для числа', a, 'предыдущее число:', a-1)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print((a+b+c+d)*3)

a = int(input()) 
b = int(input()) 
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

a = int(input())
b = int(input())
c = int(input())
x = a + b * (c - 1)
print(x)

# put your python code here
x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')

# put your python code here
a=int(input())
b=int(input())
c=int(input())
print(a*b**(c-1))

# put your python code here
a=int(input())
print(a//100)

z=int(input())
x=int(input())
print(x//z)
print(x%z)

# put your python code here
z = int(input())
print(z//2 + z%2)

# put your python code here
z = int(input())
print((z + 3) // 4)

# put your python code here
z = int(input())
x = z // 60 
c = z % 60
print(z, "мин - это", x, "час", c, "минут.")

num = int(input())
z = num % 10
x = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + x + z)
print("Произведение цифр =", c * x * z)

zxc = int(input())
c = zxc % 10
x = (zxc % 100) // 10
z = zxc // 100
print(z, x, c, sep='')
print(z, c, x, sep='')
print(x, z, c, sep='')
print(x, c, z, sep='')
print(c, z, x, sep='')
print(c, x, z, sep='')

z = int(input())
x = z // 1000
c = (z // 100) % 10
v = (z // 10) % 10
b = z % 10
print("Цифра в позиции тысяч равна", x)
print("Цифра в позиции сотен равна", c)
print("Цифра в позиции десятков равна", v)
print("Цифра в позиции единиц равна", b)

a = int(input())
f = a // 1000
s = a // 100 - (a // 1000 * 10)
t = (a % 100 - a % 10) / 10
l = a % 10
if f + l == s - t:
    print('ДА')
else:
    print('НЕТ')

z = int(input())
if z >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')