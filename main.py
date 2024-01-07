import json
print("Welcome to Streak-Counter! This is a simple streak counter.")
streaks = {}

with open('streaks.json') as json_file:
    streaks = json.load(json_file)

def autocorrect_case(input_string, correct_strings):
    lowercase_input_string = input_string.lower()
    for correct_string in correct_strings:
        if lowercase_input_string == correct_string.lower():
            return correct_string
        else:
            return input_string


while True:
    choice = str(input("Type 'new' to make a new streak or 'add' to increase streak or 'exit' to exit: "))
    if choice.lower() == "new":
        new_streak = str(input("What will be the name of this streak?"))
        new_streak_days = int(input("How long is this streak currently?"))
        streaks[new_streak] = new_streak_days
        streaks_keys = list(streaks.keys())
        print("New streak added.")
    elif choice.lower() == "add":
        print("Current streaks are: ")
        for streak in streaks_keys:
            print(streak)
        streak_to_be_increased = str(input("Choose a streak to be increased: "))
        if streak_to_be_increased.lower() in map(str.lower, streaks_keys):
            print(f"{streak_to_be_increased} will be increased.")
            streak_to_be_increased = autocorrect_case(streak_to_be_increased, streaks_keys)
            streaks[streak_to_be_increased] += 1
        else:
            print("Wrong streak provided. Please try again.")
    elif choice.lower() == "exit":
        print("Exiting...")
        print(streaks)
        with open("streaks.json", "w") as outfile: 
            json.dump(streaks, outfile)
        break