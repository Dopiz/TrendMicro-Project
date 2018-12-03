import re

def solution(S):
    
    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    clock = re.split('\s', S)
    m = {day[i]: [] for i in range(0, len(day))}
    max_time = {day[i]: 0 for i in range(0, len(day))}
    tail_time = {day[i]: 0 for i in range(0, len(day))}

    for i in range(0, len(clock), 2):
        m[clock[i]].append(clock[i + 1])
        m[clock[i]].sort()
    
    for key in m.keys():
        time = m[key]
        end_h = 0
        end_m = 0
        for i in range(0, len(time)):

            hh = (int(time[i][:2]) - end_h) * 60
            mm = (int(time[i][3:5]) - end_m)
            end_h = (int(time[i][6:8]))
            end_m = (int(time[i][9:]))
            max_time[key] = max(max_time[key], hh + mm)

            if i == len(time) - 1:
                hh = (int(24 - end_h)) * 60
                mm = (int(0 - end_m))
                tail_time[key] = hh + mm
                max_time[key] = max(max_time[key], tail_time[key])
                print(hh, mm, tail_time[key])
            
            if i == 0 and key != 'Sun':
                max_time[key] = max(max_time[key], max_time[key] + tail_time[day[(day.index(key) + 6) % 7]])
        
                
    # Mon_first_time = int(m['Mon'][0][:2]) * 60
    # max_time['Mon'] = max(max_time['Mon'], Mon_first_time + tail_time['Sun'])

    print(max_time)

    return max(max_time.values())


# 找出最長的空閒時間

# A = 'Sun 10:00-20:00 Fri 05:00-10:00 Fri 16:30-23:50 Sat 10:00-24:00 Sun 01:00-04:00 Sat 02:00-06:00 Tue 03:30-18:15 Tue 19:00-20:00 Wed 04:25-15:14 Wed 15:14-22:40 Thu 00:00-23:59 Mon 05:00-13:00 Mon 15:00-21:00'
# A = 'Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu 01:00-20:00\nFri 01:00-23:00\nSat 01:00-23:00\nSun 01:00-21:00' 
# print(solution(A))