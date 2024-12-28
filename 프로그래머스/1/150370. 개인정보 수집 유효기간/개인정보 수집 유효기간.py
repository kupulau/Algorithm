def solution(today, terms, privacies):
    answer = []
    for i, v in enumerate(privacies):
        date, type = v.split(' ')
        duration = int([x[2:] for x in terms if x[0]==type][0])
        d_yr, d_month = duration//12, duration%12
        date_yr, date_month, date_day = date.split('.')
        date_yr = int(date_yr)+d_yr
        date_month = int(date_month)+d_month
        if date_month > 12:
            date_yr += 1
            date_month -= 12
            
        # format
        if date_month < 10:
            date_month = '0{}'.format(date_month)
        
        doom = '{}.{}.{}'.format(date_yr, date_month, date_day)
        if doom <= today:
            answer.append(i+1)
               
    return answer