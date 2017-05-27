running = True
print("Test Taker Project")
print("Your commands are TEST, CREATE, CLEAR, QUIT")
while running:
    user_input = input("\nEnter command: ").upper()
    if user_input == "QUIT":
        running = False
    elif user_input == "TEST":
        answer_file = open("answer_file.test", 'r')
        print(answer_file.read())
        answer_file.close()
    elif user_input == "CLEAR":
        answer_file = open("answer_file.test", 'w')
        answer_file.close()
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
