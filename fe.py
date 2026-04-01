import random as rd

user_point=0
computer_point=0
data=('r','p','s')
while True:
    user_choice = input("rock, paper or scissors (r/p/s) : ").lower()
    if user_choice !='r' and user_choice != 'p' and user_choice !='s':
        print("Invalid choice")
        continue

    computer_choice= rd.choice(data)

    if user_choice == computer_choice:
        print("tie")
    elif(
        (user_choice== 'r' and computer_choice=='s') or 
        (user_choice=='p' and computer_choice=='r') or 
        (user_choice=='s' and computer_choice=='p')):
            user_point+=1
            print(f"computer choice {computer_choice}")
            print(f"You Won {computer_choice}")
    else:
        computer_point+=1
        print(f'You Lose {computer_choice}')
    should_continue = input('continue ? (y,n)').lower()
    if should_continue=='n':
         print(f'You won {user_point} time(s)')
         print(f'Computer won {computer_point} time(s)')
         break
