import calendar
import datetime
CollectDay = "2020-06-11"
print(CollectDay[0:8]+str(calendar.monthrange(int(CollectDay[0:4]), int(CollectDay[5:7]))[1]))
collectdays_list = []
for i in range(calendar.monthrange(int(CollectDay[0:4]), int(CollectDay[5:7]))[1] + 1)[1:]:
    collectdays_list.append(CollectDay[0:8] + ("0" + str(i) if i < 10 else str(i)))
print(collectdays_list)
for i in collectdays_list:
    if datetime.datetime.strptime(i, '%Y-%m-%d') <= (datetime.datetime.now() - datetime.timedelta(days=1)):
        print(i)

