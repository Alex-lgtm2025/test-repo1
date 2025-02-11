
my_list = [1, 4, 1, 6,"hello","a", 5,"hello"]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Повторяющиеся элементы в списке:", duplicates)
