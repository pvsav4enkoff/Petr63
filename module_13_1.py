import asyncio
import time
async def add_ending(number, endings):
  index = 0
  if number % 100 in [11, 12, 13, 14]:
      index = 2
  elif number % 10 == 1:
      index = 0
  elif number % 10 in [2, 3, 4]:
      index = 1
  else:
      index = 2
  return endings[index]
endings = ('шар', 'шара', 'шаров')
async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    i=1
    while i <= 5:
        await asyncio.sleep(2/power)
        task = asyncio.create_task(add_ending(i,endings))
        await task
        print(f"Силач {name} поднял {i} {task.result()}")
        i+=1
    print(f"Силач {name} закончил соревнования.")
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Вася', 1))
    task2 = asyncio.create_task(start_strongman('Сережа', 2))
    task3 = asyncio.create_task(start_strongman('Коля', 3))
    await task1
    await task2
    await task3
asyncio.run(start_tournament())



