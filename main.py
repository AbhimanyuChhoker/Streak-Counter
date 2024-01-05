print(
    "Welcome to Streak-Counter! This is a simple streak counter."
)
streaks = {}
streaks_keys = list(streaks.keys())
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
        for streak in streaks_keys:
            print(streak)
        streak_to_be_increased = str(input("Choose a streak to be increased: "))
        if streak_to_be_increased.lower() in map(str.lower, streaks_keys):
            print(f"{streak_to_be_increased} will be increased.")
            streaks[streak_to_be_increased]
        

