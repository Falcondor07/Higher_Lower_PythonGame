import random
import hl_resources

print(hl_resources.logo)
print("Welcome to Higher or Lower!")
score = 0
chances = 3
game_over = False

while chances > 0 and not game_over:
    def play_game():
        def choice():
            chosen = random.choice(hl_resources.data)
            name = chosen['name']
            followers = chosen['follower_count']
            description = chosen['description']
            country = chosen['country']
            hl_resources.data.remove(chosen)
            return name, description, country, followers
        choice1 = choice()
        choice2 = choice()
        print(f"Compare A: {choice1[0]}, {choice1[1]}, from {choice1[2]}")
        print(hl_resources.vs)
        print(f"Against B: {choice2[0]}, {choice2[1]}, from {choice2[2]}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_guess == 'A' and choice1[3] > choice2[3]:
            print(f"That's correct!, {choice1[0]} has {choice1[3]}M followers and {choice2[0]} has {choice2[3]}M followers.")
            play_again = 'y'
            global score
            score += 1
            print(f"Your score is {score}")
        elif user_guess == 'B' and choice1[3] < choice2[3]:
            print(f"That's correct!, {choice1[0]} has {choice1[3]}M followers and {choice2[0]} has {choice2[3]}M followers.")
            play_again = 'y'
            score += 1
            print(f"Your score is {score}")
        elif choice1[3] == choice2[3]:
            print(f"That's correct!, {choice1[0]} has {choice1[3]}M followers and {choice2[0]} has {choice2[3]}M followers.")
        else:
            print(f"That's incorrect!, {choice1[0]} has {choice1[3]}M followers and {choice2[0]} has {choice2[3]}M followers.")
            global chances
            chances -= 1
            print(f"You have {chances} lives left.")
            if chances == 0:
                play_again = 'n'
            else:
                play_again = 'y'
        if play_again == 'y' and chances > 0:
            play_game()
        else:
            print(f"Thanks for playing! Your score was {score} points.")
            game_over = True
    play_game()
