users = ["Bob", "Tom", "Ken"]  # A-1
print(users)

int_numbers = [1, 2, 3, 4, 5]  #A-2
print(int_numbers)

kazuma_info = ["Kazuma", "Takahashi", 35]  #A-3
print(kazuma_info)

members = ["Makoto", "Kazu", "Kazuma"]  #A-4
print(members[0], members[2])

print("Name:" + kazuma_info[1] + kazuma_info[0] + ",Age:" + str(kazuma_info[2]))  #A-5

odd_numbers = [1, 3, 7, 9]  # A-6
for number_1 in odd_numbers:
    print(number_1)

even_numbers = [2, 4, 6, 8]  # A-7
for numbers_2 in even_numbers:
    print(numbers_2 * 2)

users_info = [["Kazuma", 35], ["Tom", 57], ["Bob", 77]]  # A-8
for users_list in users_info:
    print("Name: " + users_list[0] + ", Age: " + str(users_list[1]))
# こうなれば良い
# "Name: Kzuma, Age: 35"
# "Name: Tom, Age: 57"
# "Name: Bob, Age: 77"
