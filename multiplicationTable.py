print('', end='\t\t')
for column in range (0, 10):
    print(column, end='\t')
print('\n')
for verse in range (0, 10):
    print (verse, end='\t\t')
    for column in range (0, 10):
        print (verse * column, end ='\t')
    print()

