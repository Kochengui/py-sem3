# 1).
import random

n=int(input('введите колличество элементов в массиве от 1 до 5 : '))
num_list=[0]*n
num_list1=[]
search= int(input('введите искомое число: '))

for index in range(n):
    num_list[index]=random.randint(0,10)
print(num_list)
num_list1=[i for i in num_list if search==i]
print(len(num_list1))


# 2).
import random

n=int(input('введите колличество элементов в массиве: '))
num_list=[0]*n

for index in range(n):
    num_list[index]=random.randint(0,10)
print(num_list)
search= int(input('введите искомое число от 1 до 5: '))

num_list1=[count for count in num_list if count>search]
num_list2=[count for count in num_list if count<search]

num_list1.sort()
num_list2.sort()
min_num=search-num_list2[-1]
max_num=search-num_list1[0]

if min_num<0:
        min_num*=(-1)
if max_num<0:
        max_num*=(-1)
if min_num < max_num:
        print(num_list2[-1])
else:
        print(num_list1[0])


# 3).

my_dict = {'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т': 1,
          'Д, К, Л, М, П, У, D, G': 2,
          'B, C, M, P, Б, Г, Ё, Ь, Я': 3,
          'F, H, V, W, Y, Й, Ы': 4,
          'K, Ж, З, Х, Ц, Ч': 5,
          'J, X, Ш, Э, Ю': 8,
          'Q, Z, Ф, Щ, Ъ': 10}
word=input(' Введите слово: ').upper()
total=0
for i in word:
       for k in my_dict:
            if i in k:
                total+=my_dict[k]
print(total)
                     


