users = ["Bob", "Tom", "Ken"]  # A-1
print(users)

int_numbers = [1, 2, 3, 4, 5]  #A-2
print(int_numbers)

kazuma_info = ["Kazuma", "Takahashi", 35]  #A-3
print(kazuma_info)

members = ["Makoto", "Kazu", "Kazuma"]  #A-4
print(members[0], members[2])

print("Name:" + kazuma_info[1] + kazuma_info[0] + ",Age:" + str(kazuma_info[2]))  #A-5

odd_numbers = [1, 3, 7, 9]  #A-6
for number_1 in odd_numbers:
    print(number_1)

even_numbers = [2, 4, 6, 8]  #A-7
for numbers_2 in even_numbers:
    print(numbers_2 * 2)

users_info = [["Kazuma", 35], ["Tom", 57], ["Bob", 77]]  #A-8
for users_list in users_info:
    print("Name: " + users_list[0] + ", Age: " + str(users_list[1]))
# こうなれば良い
# "Name: Kzuma, Age: 35"
# "Name: Tom, Age: 57"
# "Name: Bob, Age: 77"

kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": 35}  # A-9
print(kazuma_info["first_name"])  # "Kazuma"
print(kazuma_info["family_name"])  # "Takahashi"
print(kazuma_info["age"])  # 35

import random  # A-10


def dice():
    print(random.choice([1, 2, 3, 4, 5, 6]))  # 1〜6の整数をランダムに出力


dice()

# A-11
# 小数点第2位まで表示
# BMI＝ 体重kg ÷ (身長m)2
# 適正体重＝ (身長m)2 ×22

weight = float(input("体重を入力してください(kg): "))
height = float(input("身長を入力してください(m): "))

bmi = round(weight / (height * height), 2)  # BMI＝ 体重kg ÷ (身長m)2

print("あなたのBMIは" + str(bmi) + "です。")
