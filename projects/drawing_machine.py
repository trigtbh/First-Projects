from turtle import *
def turtle_contrtoller(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backwar(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Unrecognizable command.')
        
