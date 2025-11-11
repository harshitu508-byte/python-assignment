'''
Name-> Harshit Upadhayay
Date-> 08-11-2025
Project-> Daily Calorie Tracker
'''
def main():
    print("Simple Daily Calorie Tracker\n")
#get number of meals
    n = input("How many meals will you enter?: ")
    if not n.isdigit():
        print("Please enter a whole number for number of meals. Exiting.")
        return
    n = int(n)

    meals = []
    calories = []
#input meal names and calories
    for i in range(1, n + 1):
        name = input(f"Name of meal {i}: ")
        if name == "":
            name = f"Meal {i}"
        cal = input(f"Calories for '{name}': ")
        try:
            cal_val = float(cal)
            if cal_val < 0:
                print("Negative value not allowed. Setting calories to 0 for this meal.")
                cal_val = 0.0
        except:
            print("Invalid calorie input. Setting calories to 0 for this meal.")
            cal_val = 0.0

        meals.append(name)
        calories.append(cal_val)

#input daily calorie limit
    limit_in = input("\nEnter your daily calorie limit: ")
    try:
        daily_limit = float(limit_in)
        if daily_limit < 0:
            print("Negative limit not allowed. Using 0.")
            daily_limit = 0
    except:
        print("Invalid limit input. Using 0.")
        daily_limit = 0
        
#calculate total and average calories
    total = sum(calories)
    if len(calories) > 0:
        avg = total / len(calories)
    else:
        avg = 0

    print("\nDAILY SUMMARY")
    for m, c in zip(meals, calories):
        print(f"{m}: {c:.1f} kcal")
    print(f"Total calories: {total:.1f} kcal")
    print(f"Average per meal: {avg:.1f} kcal")
    print(f"Daily limit: {daily_limit:.1f} kcal")

    if total > daily_limit:
        print("WARNING: You exceeded your daily calorie limit!")
    else:
        print("You are within your daily calorie limit. Good job!")
#run the program
if _name_ == "_main_":
    main()
