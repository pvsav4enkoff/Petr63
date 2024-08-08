from probe.Packets1.hard3 import calculate_structure_sum
from probe.Packets1.Packets2.module_3_4 import get_multiplied_digits

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# global sumList,lst2
# lst2=[]
# sumList = 0

if __name__ == '__main__':
  result = calculate_structure_sum(data_structure)
  print(result)
  result = get_multiplied_digits(409203070804)
  print(result)
  # print(lst2)