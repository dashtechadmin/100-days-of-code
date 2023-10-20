
def challenge_1():
    '''Print sum of the digits of a two-digit number'''
    two_digit_number = input()
    return int(two_digit_number[0]) + int(two_digit_number[1])

def challenge_2(a, b):
    '''Calculate BMI: weight (kg) / height (m^2)'''
    '''
        BMI Categories: 
        Underweight = <18.5
        Normal weight = 18.5–24.9 
        Overweight = 25–29.9 
        Obesity = BMI of 30 or greater
    '''
    height = input() or a
    weight = input() or b
    return int(weight) // float(height) ** 2

def challenge_3(a):
    '''Life in Weeks'''
    WEEKS_IN_A_YEAR = 52
    AVG_LIFESPAN = 90
    age = input() or a
    weeks_left = (AVG_LIFESPAN - int(age)) * WEEKS_IN_A_YEAR
    return f"You have {weeks_left} weeks left."

def boss_challenge(a, b, c):
    '''Tip Calculator'''
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $") or a)
    percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? ") or b)
    friends = int(input("How many people to split the bill? ") or c)
    # print(type(total_bill), type(percentage), type(friends))
    final_bill = total_bill * ( 1 + percentage / 100 )
    split_amount = round(final_bill / int(friends), 2)
    return f"Each person should pay: ${split_amount}"

if __name__ == "__main__":
    # challenge 1
    # print(challenge_1())
    # print(3 * (3 + 3) / 3 - 3)
    
    # challenge 2
    # input_1 = 1.57
    # input_2 = 52
    # print(challenge_2(input_1, input_2))
    
    # challenge 3 
    # input_1 = "56"
    # print(challenge_3(input_1))

    # boss challenge
    input_1 = "124.56"
    input_2 = "12"
    input_3 = "7"
    print(boss_challenge(input_1, input_2, input_3))