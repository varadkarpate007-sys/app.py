import random

expenses = [random.randint(0, 1000) for i in range(30)]

print("Daily Expenses:")
print(expenses)

week1 = expenses[0:7]
week4 = expenses[21:28]

print("\nWeek 1 Expenses:", week1)
print("Week 4 Expenses:", week4)

week1_total = sum(week1)
week1_average = week1_total / len(week1)

week4_total = sum(week4)
week4_average = week4_total / len(week4)

print("\nWeek 1 Total:", week1_total)
print("Week 1 Average:", week1_average)

print("\nWeek 4 Total:", week4_total)
print("Week 4 Average:", week4_average)

no_spend_days = []

for i in range(len(expenses)):
    if expenses[i] == 0:
        no_spend_days.append(i + 1)

print("\nNo-spend Days:", no_spend_days)

current_streak = 0
max_streak = 0

for expense in expenses:
    if expense == 0:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0

print("Longest No-spend Streak:", max_streak, "days")