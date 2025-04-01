def solution(S):
    days = {
        'Sun': [0] * 24 * 60,
        'Mon': [0] * 24 * 60,
        'Tue': [0] * 24 * 60,
        'Wed': [0] * 24 * 60,
        'Thu': [0] * 24 * 60,
        'Fri': [0] * 24 * 60,
        'Sat': [0] * 24 * 60
    }

    sc = S.split()
    for idx in range(0, len(sc), 2):
        day, times = sc[idx], sc[idx+1]
        start, end = times.split('-')
        start_hour, start_minute = start.split(':')
        end_hour, end_minute = end.split(':')
        start_point, end_point = int(start_hour) * 60 + int(start_minute), int(end_hour) * 60 + int(end_minute)
        days[day][start_point:end_point] = [1] * (end_point - start_point)

    max_free = 0
    max_free_start_day, max_free_start_index = 'Sun', 0
    max_free_end_day, max_free_end_index = 'Sun', 0
    temp_start_day, temp_start_index = 'Sun', 0

    count = 0
    for day in days:
        for i, point in enumerate(days[day]):
            if point == 0:
                if count == 0:
                    temp_start_day, temp_start_index = day, i
                count += 1
            else:
                if count >= max_free:
                    max_free = count
                    max_free_end_day, max_free_end_index = day, i
                    max_free_start_day, max_free_start_index = temp_start_day, temp_start_index
                count = 0

    print("Max free time:\t", f"{max_free // 60:02d}h {max_free % 60:02d}m ({max_free} minutes)")
    print("Schedule: \t", f"{max_free_start_day} {max_free_start_index // 60:02d}:{max_free_start_index % 60:02d} - {max_free_end_day} {max_free_end_index // 60:02d}:{max_free_end_index % 60:02d}")


# 找出最長的空閒時間
# 假設週日為每週的第一天，且不考慮週六到隔週日的情況
schedule = (
    "Sun 01:00-04:00 Sun 10:00-20:00 "
    "Mon 01:00-13:00 Mon 15:00-21:00 "
    "Tue 03:30-18:15 Tue 19:00-20:00 "
    "Wed 04:25-15:14 Wed 16:14-22:40 "
    "Thu 00:00-23:59 "
    "Fri 05:00-10:00 Fri 16:30-23:50 "
    "Sat 10:00-24:00 Sat 02:00-06:00"
)

solution(schedule)
