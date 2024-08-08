# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
global sumList,lst2
lst2=[]
sumList = 0
def calculate_structure_sum(lst):
  global sumList
  for i in lst:
    if isinstance(i, (list,dict,tuple,set)):
      # print(i)
      calculate_structure_sum(i)
    if isinstance(i, dict):
      for k,v in i.items():
        # print('dict-v',v)
        lst2.append(v)
        sumList=sumList+v
    else:
      if isinstance(i, str):
        lst2.append(i)
        # print(i)
        sumList=sumList+len(i)
      if isinstance(i, int):
        lst2.append(i)
        # print(i)
        sumList=sumList+i
  # print(lst2)
  return sumList

# if __name__ == '__main__':
#   result = calculate_structure_sum(data_structure)
#   print(result)



