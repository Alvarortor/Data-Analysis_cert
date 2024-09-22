#Learn how to plot data on python

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import seaborn as sns


#Import dataset and make into df

df = pd.read_csv('medical_examination.csv')
#print(df.index)
#print(df.columns)
#Get headers


#Add overweigh column into dataset and populate based on BMI
kg = df.loc[:,["weight"]]
m = df.loc[:,["height"]].div(100)
m2 = round(np.square(m),2)

df['met_sqr'] = m2

df['BMI'] = df['weight'].div(df['met_sqr'], axis= 0) #Divide weight by heigt for each row

df['overweight'] = np.where(df['BMI'] > 25, 1,0)

#Normalize data 0 is always good, 1 is always bad
#Invert these for cholesterol and glucose; i.e. turn 1 into 0 and 0 into 1

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)






#make barplots
def cat_plot():
    df_cat = pd.melt(df,id_vars=['cardio'], value_vars =['cholesterol', 'gluc', 'smoke', 'active', 'overweight'])
    #Group and split by cardio with counts visible
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    
    df_cat = df_cat.rename(columns={0: 'total'})
    
    plot = sns.catplot(x = "variable", y= "total", hue = 'value', col ='cardio',kind = 'bar', data = df_cat)  
    fig = plot.fig
    fig.savefig('catplot.png')
    return fig

 

#Make second plot ( a heatmap! here)
def h_map():
#Clean up data errors
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975)) ]
#FInd correlation   
    crltn= df_heat.corr()

#Upper triangle
    mask = np.triu(np.ones_like(crltn, dtype=bool))
    
#Make fig
    fig, ax = plot.subplots(figsize=(9, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(crltn, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig   


cat_plot()
plot.show()

h_map()
plot.show()
