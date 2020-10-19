# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(new_record)
census = np.concatenate((data, new_record), axis = 0)
print(census)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print(data)
print(type(data))
age = np.array(census[:,0])
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)

race_0 = census[census[:,2]==0]


race_1 = census[census[:,2]==1]


race_2 = census[census[:,2]==2]


race_3 = census[census[:,2]==3]


race_4 = census[census[:,2]==4]


len_0 = len(race_0)
print(len_0)

len_1 = len(race_1)
print(len_1)

len_2 = len(race_2)
print(len_2)

len_3 = len(race_3)
print(len_3)

len_4 = len(race_4)
print(len_4)
a=[len_0,len_1,len_2,len_3,len_4]
minority_race = a.index(min(a))
print(minority_race)


senior_citizens = census[census[:,0]>60]


working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)


high = census[census[:,1]>10]


low = census[census[:,1]<=10]


avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)





