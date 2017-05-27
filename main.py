lines = [line.rstrip('\n') for line in open('answer_file.test')]
for x in range(0, len(lines)):
    if lines[x].endswith('-'):
        print((lines[x])[:-1])
        correct = x
    else:
        print(lines[x])
if int(input()) == correct:
    print("Correct")
else:
    print("Incorrect")
