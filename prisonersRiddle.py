import random

class Prisoner:
    def __init__(self, number) -> None:
        self.number = number
        self.successful = None
        self.lastNumber = number

class Box:
    def __init__(self, number) -> None:
        self.number = number

def run():
    # 100 prisoners numbered 1-100
    prisoners = [Prisoner(num) for num in range(1, 100 + 1)]

    # Slips with their numbers are randomly placed in 100 boxes in a room
    boxes = [Box(num) for num in range(1, 100 + 1)]
    random.shuffle(boxes)

    # Each prisoner may enter the room one at a time and check 50 boxes
    for prisoner in prisoners:
        for turn in range(50):
            # random strategy
            # selection = random.randint(0, 99)

            # loop strategy
            selection = prisoner.lastNumber - 1
            prisoner.lastNumber = boxes[selection].number

            # check
            if prisoner.number == boxes[selection].number:
                prisoner.successful = True
                break
        
        if prisoner.successful is None:
            prisoner.successful = False

    # If all 100 prisoners find their number during their turn in the room,
    # they Will all be freed. But if even one fails, they Will all be executed.
    freed = all(prisoner.successful for prisoner in prisoners)
    return freed

# run once
freed = run()
print('The program was run and...', end=' ')
if freed:
    print('The prisoners were freed.')
else: print('The prisoners were executed.')

# calculate probability that prisoners will be freed
successes = 0
n = 1000
for i in range(n):
    success = run()
    if success:
        successes += 1
probability = successes / n
print('The probability that prisoners will be freed is', probability)
