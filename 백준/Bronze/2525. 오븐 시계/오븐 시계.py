def oven_timer(hour, min, duration):
    dur_hour, dur_min = duration//60, duration%60
    res_hour = hour + dur_hour
    res_min = min + dur_min
    
    if res_min >= 60:
        res_min = res_min - 60
        res_hour += 1
    
    if res_hour >= 24:
        res_hour -= 24

    return str(res_hour)+ ' '+ str(res_min)

hour, min = map(int, input().split())
duration = int(input())

print(oven_timer(hour, min, duration))