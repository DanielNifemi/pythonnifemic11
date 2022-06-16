animal = 'goat'
target = input("input a character to find :")
for index, letter in enumerate(animal):
    if letter == target:
        print("Letter found in index :", index)
        break
    else:
        print('letter', target, 'not found in ', animal)
