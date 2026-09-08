import random

durations = [random.randint(1, 10) for i in range(50)]

print("Track Durations:", durations)

time_limit = 60

memo = {}

def max_tracks(index, remaining_time):
    if index >= len(durations) or remaining_time <= 0:
        return 0

    if (index, remaining_time) in memo:
        return memo[(index, remaining_time)]

    skip = max_tracks(index + 1, remaining_time)

    take = 0
    if durations[index] <= remaining_time:
        take = 1 + max_tracks(index + 2, remaining_time - durations[index])

    memo[(index, remaining_time)] = max(take, skip)

    return memo[(index, remaining_time)]


result = max_tracks(0, time_limit)

print("Time Limit:", time_limit, "minutes")
print("Maximum Non-Adjacent Tracks:", result)