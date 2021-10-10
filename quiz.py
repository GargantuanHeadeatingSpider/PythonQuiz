# To make the quiz fun. Vital in question generation.
import random

# A list of dictionaries containing questions, choices and answers. It is easy to add, edit and remove entries.
question_dict_list = [{
                          'question': 'What was the original name of Warren Spector\'s pitch that would later become Deus Ex?\n1. Better Red than Undead\n2. Troubleshooter\n3. System Shock 2',
                          'answer': 2
                      },

                      {
                          'question': 'Metal Gear Solid is the creation of which game developer?\n1. Hideki Kamiya\n2. Shinji Mikami\n3. Hideo Kojima',
                          'answer': 3
                      },

                      {
                          'question': 'The Game of Life is the creation of which mathematician?\n1. John Conway\n2. Alan Turing\n3. John Von Neumann',
                          'answer': 1
                      },

                      {
                          'question': 'Which film director created the modern zombie?\n1. David Cronenberg\n2. Lucio Fulci\n3. George A. Romero',
                          'answer': 3
                      },

                      {
                          'question': 'Are you feeling lucky?\n1. No\n2. Yes\n3. You\'re not even trying anymore, are you?',
                          'answer': 3
                      },

                      {
                          'question': 'What is the name of the video game series inspired by the novel, "Roadside Picnic"?\n1. Codename Outbreak\n2. S.T.A.L.K.E.R\n3. Metro 2033',
                          'answer': 2
                      },

                      {
                          'question': 'What is the name of Valve\'s proprietary game engine?\n1. IdTech\n2. Source\n3. Unreal',
                          'answer': 2
                      },

                      {
                          'question': 'Who is the author of the Discworld novels?\n1. Terry Pratchett\n2. Rob Grant\n3. Neil Gaiman',
                          'answer': 1
                      },

                      {
                          'question': 'Who is the legendary Greek philosopher known for plucking a chicken and yelling, "BEHOLD, A MAN!"?\n1. Diogenes\n2. Plato\n3. Socrates',
                          'answer': 1
                      },

                      {
                          'question': 'Who is the author of Fear and Loathing in Las Vegas?\n1. Oscar Zeta Acosta\n2. Raplh Steadman\n3. Hunter S. Thompson',
                          'answer': 3
                      },

                      {
                          'question': 'How many fingers am I holding up?\n1. Five\n2. Two\n3. None, you\'re a computer, you don\'t have fingers.',
                          'answer': 3
                      },

                      {
                          'question': '2020\'s smash hit metal album, "Doom Eternal" is the work of which famous artist?\n1. Mick Gordon\n2. Hans Zimmer\n3. Andrew Hulshult',
                          'answer': 1
                      },

                      {
                          'question': 'What was the name of the CIA project in which cats were sent to spy on Soviet officials,\nonly to fail as the first cat was immediately hit by a taxi?\n1. Operation Acoustic Kitty\n2. Operation Spy Cat\n3. Operation Covert Feline',
                          'answer': 1
                      },

                      {
                          'question': 'Do you like cats?\n1. No\n2. There is no correct answer to that, it\'s subjective.\n3. Yes',
                          'answer': 3
                      },

                      {
                          'question': 'How much wood could a woodchuck chuck if a woodchuck could chuck wood?\n1. 5 woods\n2. 10 woods\n3. This is a trick question and I shall have no part in it!',
                          'answer': 3
                      },

                      {
                          'question': 'Who holds the title of "World\'s worst director"?\n1. Michael Bay\n2. M. Night Shyamalan\n3. Uwe Boll',
                          'answer': 3
                      },

                      {
                          'question': 'How did King George II die?\n1. Honourably in battle\n2. Pushing too hard for a poo, causing an aortic aneurysm\n3. Hitting his head too hard on a door frame',
                          'answer': 2
                      },

                      {
                          'question': 'What was the name of the genius who died in March 1809 after his \nknife-swallowing habit caught up to him?\n1. Allan Pinkerton\n2. William Snyder\n3. John Cummings',
                          'answer': 3
                      },

                      {
                          'question': 'Name the Darwin Award recipient known for his golf ball cleaner-related misadventure.\n1. Everitt Sanchez\n2. Garry Hoy\n3. Professor Alexander Zhankov',
                          'answer': 1
                      },

                      {
                          'question': 'What number am I thinking of?\n1. How on Earth would I know?\n2. 1\n3. Pi',
                          'answer': 1
                      }]

# _________Variables_________ #

# Names and scores go here
user_dict = {}


correct_list = []
                        # These lists will be used for viewing correct and incorrect answers after quiz.
incorrect_list = []


c_answer = []
                        # For int values corresponding to quiz answers, used to show which answers were incorrect.
i_answer = []

# Max quiz length will never exceed the number of questions available.
max_quiz_length = len(question_dict_list)

# Answered questions are dispensed here, ready to be transferred back to dict list and cleared upon restarting.
used_questions = []

# Keeps track of number of times quiz function repeats
round_count = []


# A welcome message to set the mood.
def welcome():
    print('BEHOLD! A QUIZ!', '\n' * 2)


welcome()


# Initialises the program.
def main():
    quiz()


# Where questions are made
def generate_questions():
    question = random.choice(question_dict_list)
    question_text = question.get('question')
    print(question_text)
    return question


# Handles input for answering questions
def process_answer():
    content = generate_questions()
    answer = content.get('answer')
    guess = get_valid_answer('Pick an option from 1-3. Or else. ')

    list_content = content.get('question')
    list_answer = content.get('answer')

    # Checks if integer input by user matches that of the 'answer' key's value from question_dict_list
    if guess == answer:
        correct_list.append(list_content)
        c_answer.append(list_answer)
        question_dict_list.remove(content)
        used_questions.append(content)
        return True
    else:
        incorrect_list.append(list_content)
        i_answer.append(list_answer)
        question_dict_list.remove(content)
        used_questions.append(content)
        return False


# Whether true or false, the question will be removed from the question list and added to the used questions list


# The star of the show. Runs most of the functions, gets name and score, adds them to user_dict to generate scoreboard.
def quiz():

    score = 0

    name = get_valid_name('What is thy name, foolish mortal?  ')

    print('\n')

    quiz_length = get_valid_length('Please enter a quiz length of ' + str(max_quiz_length) + ' or under.  ')

    round_count.append(1)

    num = round_count

    print('You have chosen to answer ' + str(quiz_length) + ' questions.\n')
    print('Round', num.count(1), '...')

    # For loop has its range set by the int entered for quiz length, generates a question and
    # calls for input on each iteration.
    for i in range(quiz_length):
        correct = process_answer()
        if correct:
            score += 1
            print('\nTh-that\'s impossible!\n\n')
        else:
            print('\nW R O N G !\n\n')

    # Presenting score as both the amount of correct answers out of total, and as percentage.

    percentage = 0

    if score > 0:
        percentage = round((score / quiz_length) * 100, 0)

    user_dict[name] = int(percentage)
    print(name, ',', 'Your score was {}/{}, '.format(score, quiz_length, ), percentage, '%\n')
    view_answers()
    return user_dict


# Borrows the interaction of the restart function to let users decide whether they would like to see the answers.
def view_answers():
    c_list_content = correct_list
    i_list_content = incorrect_list
    c_list_text = '\n\n'.join([str(elem) for elem in c_list_content])
    i_list_text = '\n\n'.join([str(elem) for elem in i_list_content])

    reply = str(input('Would you like to know which answers you got correct and incorrect? (y/n): ')).lower().strip()

    if reply[:1] == 'y':
        print('Coming right up.')
        print('\n' * 2)
        print('Correct answers:\n', c_list_text, '\n' * 2)
        print('Incorrect answers:\n', i_list_text, '\n\nThe correct answers were: ', str(i_answer), '\n' * 2)
        restart()
        return True
    if reply[:1] == 'n':
        print('\n' * 3)
        restart()
        return False
    else:
        print('Please enter \'y\' or \'n\' \n')
        view_answers()
    return


# Creates and displays the list of user dictionaries (containing names and scores) in descending order,
# presenting their scores as a percentage, along with an average between all users.
def scoreboard():
    print('_________Scoreboard_________\n')
    [print(key, ':', value, '%') for (key, value) in sorted(user_dict.items(), key=lambda x: x[1], reverse=True)]
    values = list(user_dict.values())
    average = round(sum(values) / len(user_dict), 0)
    print('Average score: ', average, '%')
    return


# Handles input for entering name
def get_valid_name(n):
    valid = False
    while not valid:
        try:
            name = str(input(n))
            valid = check_valid_name(name)
        except ValueError:
            print('Please enter a valid name\n')
    else:
        return name


# Ensures name is written in alphabetical characters only
def check_valid_name(s):
    if (str(s)).isalpha():
        return True
    else:
        print('Please enter only alpha characters\n')
        return False


# Processes input
def get_valid_answer(v):
    valid = False
    while not valid:
        try:
            num = int(input(v))
            valid = check_answer_valid(num)
        except ValueError:
            print('\nInvalid input\n')
    else:
        return num


# Checks if input for answer is within the available options
def check_answer_valid(i):
    if type(int(i)) == int:
        if int(i) <= 3:
            if int(i) > 0:
                return True
            else:
                print('Please enter a valid answer from 1-3\n')
                return False


# Handles input for determining quiz length
def get_valid_length(i):
    valid = False
    while not valid:
        try:
            num = int(input(i))
            valid = check_length(num)
        except ValueError:
            print('Invalid input')
    else:
        return num


# Checks whether the get_valid_length input is suitable. In this case, the int must within the length of the question list
def check_length(n):
    if type(int(n)) == int:
        if int(n) > 0:
            if int(n) <= max_quiz_length:
                return True
            else:
                print('Invalid input.')
                return False


# A handy restart function
def restart():
    reply = str(input('Does anyone else dare to challenge the machine? (y/n): ')).lower().strip()
    if reply[:1] == 'y':

        # To restore used questions
        question_dict_list.extend(used_questions)
        used_questions.clear()
        print('\n' * 3 + 'Here we go again.\n')

        # To start the quiz again
        main()
        return True
    if reply[:1] == 'n':

        # Shows final score
        print('\n' * 3)
        scoreboard()
        return False
    else:

        # If an invalid input is selected, this will print and the function will begin again.
        print('Please enter \'y\' or \'n\'. The fate of the world depends on it.\n')
        restart()
    return


main()
