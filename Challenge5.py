import pandas as pd
import matplotlib.pyplot as plot
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')





def draw_plot(df):
    # Read data from file
    df = df.copy()

    # Create scatter plot
    fig = plot.subplots(figsize=(12, 4))
    fig = plot.scatter('Year', 'CSIRO Adjusted Sea Level',color = 'r', data = df)
    


   
    #Save image and return fig (don't change this part)
    #fig.savefig('line_plot.png')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x = pd.Series([i for i in range(1880,2051)])
    y = res.intercept + res.slope * x
    plot.plot(x , y , '-', label= "1880-2050 expected")
    leg = plot.legend(loc = 'lower center')
    
    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(2000,2051)])
    y = res.intercept + res.slope * x
    plot.plot(x , y , '-', label= "2000-2050 expected")
    leg = plot.legend(loc = 'lower center')

    # Add labels and title
    plot.title("Rise in Sea Level")
    plot.xlabel('Year')
    plot.ylabel('Sea Level (inches)')
    
    plot.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plot.savefig('sea_level_plot.png')
    return plot.gca()
    
    
draw_plot(df)