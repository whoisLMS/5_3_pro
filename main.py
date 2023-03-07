def main():
    months = []
    with open("astronauts.csv", "r") as source:
        for line in source:
            infos = line.split(",")
            if infos[0] == 'Name':
                continue
            else:
                months.append(infos[4].split("/")[0])
    full_len = len(months)
    first = max(set(months), key=months.count)
    first_percentage = ((months.count(first) / full_len) * 100).__round__(1)
    while first in months:
        months.remove(first)
    second = max(set(months), key=months.count)
    second_percentage = ((months.count(second) / full_len) * 100).__round__(1)
    while second in months:
        months.remove(second)
    third = max(set(months), key=months.count)
    third_percentage = ((months.count(third) / full_len) * 100).__round__(1)
    print(f'A leggyakoribb hónap: {first}, százaléka: {first_percentage}%\n'
          f'A második leggyakoribb hónap: {second}, százaléka: {second_percentage}%\n'
          f'A harmadik leggyakoribb hónap: {third}, százaléka: {third_percentage}%')


main()
