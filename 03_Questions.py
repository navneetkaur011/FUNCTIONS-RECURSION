print("Ques.1- Write a program to print the length of a list.")

cities = ["Delhi", "Gurgaon", "Noida", "Mumbai", "Pune"]
heroes = ["thor", "ironman", "captain america", "batman"]

def print_len(list_item):
    print("Total items:", len(list_item))
    for item in list_item:
        print(item, end=" ")
    print()

print_len(cities)
print_len(heroes)