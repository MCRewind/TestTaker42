running = True
attempts = 0
print("Test Taker Project")
print("Your commands are TEST, CREATE, CLEAR, QUIT")
while running:
    user_input = input("\nEnter command: ").upper()
    if user_input == "QUIT":
        running = False
    elif user_input == "TEST":
        score = 0
        attempts += 1
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
        score_file = open("test_score.test", 'a')
        score_file.write('\n' + "Attempt: " + str(attempts) + '\n' + "Score: " + str(score) + '\n')

    elif user_input == "CLEAR":
        answer_file = open("answer_file.test", 'w')
        answer_file.close()
        score_file = open("test_score.test", 'w')
        score_file.close()
        attempts = 0
    elif user_input == "CREATE":
        new_problem = input("Write the problem: ")
        answer_file = open("answer_file.test", 'a')
        answer_file.write('\n' + new_problem)
        num_answers = input("Input the number of answers: ")
        while not num_answers.isnumeric():
            print("Not a number.")
            num_answers = input("Input the number of answers: ")
        num_answers = int(num_answers)
        for each in range(0,num_answers):
            new_answer = input("Input an answer, put a dash after correct answers: ")
            answer_file.write('\n' + new_answer)
        answer_file.write('\n')
        answer_file.close()
