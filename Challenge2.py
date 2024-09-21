

#Imports
import pandas as pd


#Get dataset and load into system
df = pd.read_csv('adult.data.csv')
#print(df.to_string())

#Reference to columns
#print(df.columns)

#Get total size
total = (df[df.columns[0]].count())

#Look at demographic data

#How many people in each race?
rce = df['race'].value_counts()
rce = rce.to_string().lstrip()
print("1. Number of individuals of each race:","\n", rce)

#Average age of men

    #Steps: Find men, average age, round
men = (df[df["sex"] == 'Male'])
avg_age = men.loc[:,'age'].mean()
print("2. Average male age (yr):", round(avg_age,1))


#Percent of people with bachelors
    #Remove extra data
degrees = df.loc[:,['education']]

    #Count if degree is bachelors
B_deg = degrees[degrees['education']== 'Bachelors'].count()


#Percent with bachelors over total, rounded to 1 decimal
perc = round(((B_deg/total) * 100),1)
perc = (perc.to_string()[-4:][::]) #Convert to string to remove leading education
print("3. Percent of indiv. with Bacherlor's degree:", perc,"%")



#Percent of people with advanced degree and make more than 50K #Bach and up
#remove extra data
all_degpay = (df.loc[:,["education", "salary","education-num"]])

#Filter education code to higher than bachelors first
h_deg = all_degpay.loc[all_degpay['education-num'] >= 13]

#Then string filter salary
h_pay = h_deg.loc[h_deg['salary'].str.contains('>50K')]

#Count indivs
h_degpay = h_pay.count()

#Operations for percents
h_degpay_perc = round(((h_degpay/total) * 100),1)
h_degpay_perc = (h_degpay_perc.to_string()[-4:][::])
print("4. Percent of indiv. with at least Bachelor's degree making >50K:", h_degpay_perc,"%")



#Percent of people without advanced degree and make more than 50k
l_deg = all_degpay.loc[all_degpay['education-num'] < 13]
l_pay = l_deg.loc[l_deg['salary'].str.contains('<=50K')]
l_degpay = l_pay.count()
l_degpay_perc = round(((l_degpay/total) * 100),1)
l_degpay_perc = (l_degpay_perc.to_string()[-4:][::])
print("5. Percent of indiv. without at least Bachelor's degree making >50K:", l_degpay_perc,"%")
    
#What min number of hours people work each week
all_hourpay = (df.loc[:,["hours-per-week", "salary"]])
minhour = all_hourpay.min(axis = 0)['hours-per-week']
print("6. Minimum hours worked per week: ",minhour) #must be nice


#WHat percent of people work min hours and make more than 50k
h_pay = all_hourpay[all_hourpay['salary'].str.contains('>50K')]
minhour1 = h_pay.min(axis = 0)['hours-per-week']
min_hour_perc = round(((minhour1/total) * 100),1)
print("7. Percent of indiv. working minimal(",minhour,")hours/week while still earning >50k: ",min_hour_perc)
#I think this one should be given some rounding freedom

#What country has highest percent of people earning >50k, return percent

all_placepay = (df.loc[:,["native-country", "salary"]])
h_pay = all_placepay[all_hourpay['salary'].str.contains('>50K')]
h_cpay = h_pay['native-country'].value_counts()

max_country_pay = (h_cpay.iloc[:1])
country_pay = max_country_pay.to_string()
x = country_pay.split()
max_country = x[0]
pay_people = x[1]
pp = pd.to_numeric(pay_people)

h_pay_country = round(((pp/total) * 100),1)

print("8. The",max_country,"has the highest percentage of people:(",h_pay_country,") earning >50k")

#What is most popular ocupation for peeps earning >50k in india 

all_placejobpay = (df.loc[:,["native-country", "occupation", 'salary']])
in_job = all_placejobpay[all_placejobpay['native-country'] == 'India']
h_pay = in_job.loc[in_job['salary'].str.contains('>50K')]
pop_occ = h_pay['occupation'].value_counts()
max_pop = (pop_occ.iloc[:1])
max_pop = max_pop.to_string()
x = max_pop.split()
job = x[0]
num = x[1]
num = pd.to_numeric(num)
print("9. The most popular occupation in India is that pays >50K is:", job)