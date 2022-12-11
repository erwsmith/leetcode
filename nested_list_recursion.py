'''
Walks through nested list of lists and counts the number of 'leaf items' aka 
list elements which aren't lists
'''

names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

def count_leaves(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print(f'sublist found: {item}\n\n')
            count += count_leaves(item)
        else:
            print(f'leaf item counted: {item}\n\n')
            count += 1
    return count

print(count_leaves(names))
