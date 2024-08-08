def add_ending(number, endings):
    index = 0
    if number % 100 in [11, 12, 13, 14]:
        index = 3
    elif number % 10 == 1:
        index = 0
    elif number % 10 in [2, 3, 4]:
        index = 1
    else:
        index = 2
    return endings[index]

endings = ('участник', 'участника', 'участников')
ending2 = ('задача', 'задачи', 'задач')
ending3 = ('секунда', 'секунды', 'секунд')
team1_num = 5
team2_num = 6
score1 = 45
score2 = 40
team1_time = 1552.512
team2_time = 1550.512
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Мастера кода!'
challenge_result2 = 'Победа команды Волшебники Данных!'

print("В команде Мастера кода: %s %s ! " %(team1_num, add_ending(team1_num, endings)))
print("Итого сегодня в командах: %s и %s %s!" %(team1_num, team2_num, add_ending(team2_num, endings)))

template = '{0} {1} {2} {3}'
print(template.format("Команда Волшебники данных решила:",score1,add_ending(team2_num, ending2), "!"))
template = '{0} {1} {2} {3}'
print(template.format("Волшебники данных решили задачи за ",team1_time,add_ending(team2_num, ending3), "!"))

print(f"Команды решили {score1} и {score2} {add_ending(score2, ending2)}.")
# print(f"Результат битвы: {challenge_result}")

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    print(f"Результат битвы: {challenge_result}")
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    print(f"Результат битвы: {challenge_result2}")
else:
    print('Ничья!')

print(f"Сегодня было решено {score1+score2} {add_ending(score2+score1, ending2)}, "
      f"в среднем по {time_avg} {add_ending(time_avg, ending3)}.")
