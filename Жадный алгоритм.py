import random
list_int_ways = [12, 40, 11, 7, 23, 47, 18, 52]
list_complete_ways = []
set_complete_ways = set(list_complete_ways)
while len(set_complete_ways) != 8:
    random_way = random.choice(list_int_ways)
    start_citis_way = 12
    set_complete_ways.add(start_citis_way)
    set_complete_ways.add(random_way)
    if len(set_complete_ways) == 8:
        print(set_complete_ways)
        list_set_complete_ways = list(set_complete_ways)
        print(list_set_complete_ways)
        while sum(list_set_complete_ways) != 210:
            print(sum(list_set_complete_ways))
        if sum(list_set_complete_ways) == 210:
            print('Единнственная комбинация путей -', sum(list_set_complete_ways))





