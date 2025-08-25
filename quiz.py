# Make a quiz game that accepts, edits, or deletes questions with it's corresponding answer
# The program can run the quiz and will display the correct answer after answering, and will display all of the correct answers and guesses
running = True
questions = []
answer_choices = []
correct_choices = []

choices = ("A", "B", "C", "D")
guess = []

total_score = 0

while running:
    option = input("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                   "[q] Quit \n"
                   "[1] Add Question \n"
                   "[2] Remove Question and Answers \n"
                   "[3] View Questions Options, & Answers \n"
                   "[4] Run Quiz \n"
                   "Please enter an option (q,1,2,3,4):")
    if (option.lower() == "q"):
        running = False
        print("Closing...")

    elif option == "1":
        questions.append(input("Please enter your question: "))
        total_questions = len(questions)
        answer_choices.append([])
        for x in range(len(choices)):
            answer = input(
                f"Please enter answer for choice {choices[x]}: ")
            answer_choices[total_questions-1].append(f"{choices[x]}. {answer}")
        correct_choices.append(
            input("Please enter correct answer(a, b, c, d): ").upper())
        print(f"Here's your answers: {answer_choices[total_questions - 1]}")
        input("Please enter to continue...")
    elif option == "2":
        question_counter = 1
        if len(questions) == 0:
            input("There are no questions to delete! Please press enter to continue...")
        else:
            for question in questions:
                print(f"{question_counter}. {question}")
                question_counter += 1
            select = input("Please select question or (q) quit: ")
            num_select = int(select)
            if question_counter-1 >= num_select:
                questions.pop(num_select-1)
                answer_choices.pop(num_select-1)
                correct_choices.pop(num_select-1)
            elif select == "q":
                break
            else:
                input("Invalid! Please press enter to continue...")
    elif option == "3":
        question_counter = 1
        if len(questions) == 0:
            input("There are no questions to view! Please press enter to continue...")
        else:
            for question in questions:
                print(f"{question_counter}. {question}")
                for x in range(len(choices)):
                    print(answer_choices[question_counter-1][x], end=" ")
                print(
                    f"\nCorrect Answer: {correct_choices[question_counter-1]}")
                question_counter += 1
            input("Please enter to continue...")
    elif option == "4":
        if len(questions) == 0:
            input("There are no questions added! Please press enter to continue...")
        else:
            question_counter = 1
            for question in questions:
                print(f"{question_counter}. {question}")
                for x in range(len(choices)):
                    print(answer_choices[question_counter-1][x], end=" ")
                current_guess = input(
                    "\nPlease select your answer(a, b, c, d): ")
                guess.append(current_guess.upper())
                if guess[question_counter-1] == correct_choices[question_counter-1]:
                    total_score += 1
                    print("Good job! You got it right!")
                else:
                    print(
                        f"Incorrect! The correct answer was {correct_choices[question_counter-1]}")
                question_counter += 1
                input("Please enter to continue...")
            total_questions = len(questions)
            percent_score = int((total_score / total_questions) * 100)
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("RESULTS")
            print(
                f"Congrats! You got a score of {total_score} out of {total_questions} ({percent_score}%)")
    else:
        print("Option invalid!")
