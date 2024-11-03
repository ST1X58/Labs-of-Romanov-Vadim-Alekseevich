def find_common_participants(participants_first_group, participants_second_group, separator=","):
    group1 = participants_first_group.split(separator)
    group2 = participants_second_group.split(separator)
    set1 = set(group1)
    set2 = set(group2)
    common_participants = set1.intersection(set2)
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)
result = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(result)