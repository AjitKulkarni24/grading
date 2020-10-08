score = input('Enter Score: ')
sc = float(score)
if sc >= 9 and sc < 11:
    print('A')
elif sc >= 8:
    print('B')
elif sc >= 7:
    print('C')
elif sc >= 6:
    print('D')
elif sc < 6:
    print('F')
else:
    print('Value out of range.Try adding value between 0.1 and 1.0')
    print('Done!')
