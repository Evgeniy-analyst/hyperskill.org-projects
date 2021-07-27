# put your python code here
days = abs(int(input()))
food = abs(int(input()))
cost_fly = abs(int(input()))
night_in_hotel = abs(int(input()))
print(cost_fly * 2 + days * food + night_in_hotel * (days - 1))
