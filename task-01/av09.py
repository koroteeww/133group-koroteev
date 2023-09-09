from datetime import datetime,timedelta
now = datetime.now()
averageman = 90.7
averagewoman = 67.5
bday = datetime(1988,11,29)
notice_interval = timedelta(days = averageman*365)
avdeath = bday + notice_interval
print(avdeath)
print("you remain to live="+str(avdeath-now))