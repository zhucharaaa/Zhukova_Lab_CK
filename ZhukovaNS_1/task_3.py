list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
all_players = len(list_players)

center_list = all_players // 2

first = list_players[:center_list]
second = list_players[center_list:]

print(first)
print(second)
