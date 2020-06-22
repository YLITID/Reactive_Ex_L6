import rx
tempa = 0
tempb = 0
tempop = 0

def savea():
    global tempop
    global tempa
    global tempb
    a = input("Waiting operand a or b - ")
    if a == 'a':
        tempop = a

        a = int(input("a = "))

        tempa = a
    elif a == 'b':
        tempop = a
        a = int(input('b = '))

        tempb = a
    else:
        error('invalid literal for operands(a or b is legal) ')


def saveb():
    global tempop
    global tempa
    global tempb
    if tempop == 'a':
        tempb = int(input('b = '))


    elif tempop == 'b':
        tempa = int(input('a = '))


    else:
        error('invalid literal for operands(a or b is legal) ')

def error(e):
    print('Error occured ', e, "Stopping...")
    exit()

C0 = 281
C1 = 286
C2 = 285

print('r = C2*a + C1*b + C0\n'
          'C0 = 281\n'
          'C1 = 286\n'
          'C2 = 285  ==>\n'
          'r = 285*a + 286 * b + 281\n'
          '')

## Observer, Observable, Subject
# noinspection PyArgumentList
def inputa(observer, scheduler):
    observer.on_next(savea())
    observer.on_next(saveb())
    observer.on_completed()



source = rx.Observable(inputa)

while True:
    source.subscribe(
        on_next = lambda i: print('r = 285*', tempa, ' + 286*', tempb, ' + 281','\n r = ', 285 * tempa + 286 * tempb + 281),
        on_error = lambda e: error(e),
        on_completed = lambda: print('Done!')
)

#def inputb(observer, scheduler):
#    observer.on_next(saveb())
#    observer.on_next(saveb())


#sourceb = rx.create(inputb)

#sourceb.subscribe(
#    on_next=lambda a: print('r = 285*', tempa, ' + 286*', tempb, ' + 281'),
#    on_error=lambda: print('Error Occurred:'),
#    on_completed=lambda: print('r = ', 285 * tempa + 286 * tempb + 281,
#                               'Done!'),
#)
