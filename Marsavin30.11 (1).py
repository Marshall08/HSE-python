#9. На входе список чисел, получить список квадратов этих чисел / use map

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, numbers)))

#10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
#На выходе получить словарь из самой точки и расстояния до этой точки из начала координат (0, 0)

coords = [(1, 1), (2, 3), (5, 3)]
#distance = ???
#print(distance)

#11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.

square = [x * x for x in range(2, 28) if x % 2 == 0]
print(square)

#12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точки от начала координат (0, 0) в первой четверти. # max()

points = [(3, 1), (4, 5), (6, 2)]
max_distance = max(point for point in points)
print(max_distance)

#13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...] # list(map(..., nums_first, nums_second))

nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
result = list(map(lambda x, y: (x + y, x - y), nums_first, nums_second))
print(result)

#14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
#print(list(map(int, "1 2 3".split())))

array = ['43141', '32441', '4', '4154', '43121']
new_array = []
result_array = []
for i in range(len(array)):
    if int(array[i])**2 % 2 == 0:
        new_array.append(int(array[i]))
        result_list = list(map(lambda x: x * x, new_array))
print(result_list)

#15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит # slice, split, map, zip

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""


#Мы хотим получить нормальную таблицу, чтобы импортировать в csv

#[
#  {
#    'name': 'Petya',
 #   'grade': '5'
  #  'subject': 'math'
   # 'year': '1999'
  #},
  #{
   # 'name': 'Vasya',
    #'grade': '5'
    #'subject': 'language'
    #'year': '2000'
 # },
  #...
#]


#16. Получить сумму по столбцам у двумерного списка # sum, zip

#a = [[11.9, 12.2, 12.9],
#    [15.3, 15.1, 15.1], 
#    [16.3, 16.5, 16.5],
 #   [17.7, 17.5, 18.1]]
    
#result = [61.2, 61.3, 62.6]   


#print(list(zip(*a)))
