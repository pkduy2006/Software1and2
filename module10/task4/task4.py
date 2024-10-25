import random
from race import Race

cars = []
hour_passed = 0
cnt = 0
for i in range(10):
    random_max_speed = random.randrange(100, 200)
    cnt += 1
    regis_num = "ABC-" + str(cnt)
    cars.append((regis_num, random_max_speed))

race1 = Race("Grand Demolition Derby", 8000, cars)
while not race1.race_finished():
    race1.hour_passes()
    hour_passed += 1
    if hour_passed % 10 == 0:
        print(f"After {hour_passed} hours:")
        race1.print_status()
print("Final result:")
race1.print_status()