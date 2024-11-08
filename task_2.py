def find_common_participants(first, second, splitter=','):
    participants = []
    first_split = list(first.split(splitter))
    second_split = list(second.split(splitter))
    for person in first_split:
        if person in second_split:
            participants.append(person)
    participants.sort()
    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
