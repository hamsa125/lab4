import random

correct = "Well played you got it"
too_low = "Too Low, try using larger  numbers"
too_high = "Too High , try again"




def RangeVelidation( high ):
    while True:
        #Ueing try statement to validate user's input
        try:
            #get user's input
            number = int(input())
            #high is used a temp hold for the  max value
            if high == 0 : return number
            elif high < number:
                print("Please enter a number less then " ,high)
            else: return number

        except ValueError:
            print("Please enter you numbers as digits  ")




def Generate_Number(low, high):
    #Generate a random number for the game #
    return random.randint(low, high)




def get_input():
    # creat a loop and only break if user enters a  integer
    while True:
        # use try to verify input
        try:
            '''get guess'''
            number = int(input('Guess the number I am thinking? \n'))
        except ValueError:
            print("Sorry, I don't understand can you enter it as a decimal \n")
            continue

        break
    return number




def check_guess(guess, secret):
    #compare guess and secret, return string describing result of comparison#
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    print("Welcome to the lab 1 Capstone Guessing game ")
    print("Let's see how fast you can beat this is game ")#i dont know
    print("Please enter the ranges below :")
   #get user's input #
    print("Enter the maximum value of the game ")
    high= RangeVelidation(0)
    #print(high)


    print("Enter the minimum value of the game ")

    low = RangeVelidation(high)

    secret = Generate_Number (low, high)

    count_guess =  0

    while True:
        guess = get_input()
        result = check_guess(guess, secret)
        print(result)
        count_guess = count_guess+1

        if result == correct:
            print("and only in ", count_guess, " turns ")
            break

if __name__ == '__main__':
    main()