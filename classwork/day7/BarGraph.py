import pylab as plt
DayofWeekofCall = [1,2,3]
DispatchesOnThisWeek=[60,54,30]
LABELS=["MONDAY","TUESDAY","WEDNESDAY"]
plt.bar(DayofWeekofCall,DispatchesOnThisWeek,align='center')
plt.xticks(DayofWeekofCall,LABELS,Rotation='45')
plt.show()
