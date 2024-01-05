print(
    "Welcome to Streak-Counter! This is a simple streak counter."
)
streaks = {}
while True:
    print("Type 'new' to make a new streak or 'add' to increase streak: ")
    choice = str(input())
    if choice.lower() == "new":
        new_streak = str(input("What will be the name of this streak?"))
        new_streak_days = int(input("How long is this streak currently?"))
        streaks[new_streak] = new_streak_days
        print("New streak added.")
    elif choice.lower() == "add":
        print("Current streaks are: ")
        for streak in streaks.keys():
            print(streak)
        

