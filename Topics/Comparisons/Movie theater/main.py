number_of_halls = int(input())  # количество залов
capacity = int(input())  # вместимость
number_of_viewers = int(input())  # запланированное количество посетителей
prowerk = number_of_halls * capacity >= number_of_viewers
print(prowerk)
