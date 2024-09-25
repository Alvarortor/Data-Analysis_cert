import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(df.columns)


#Preclean data
def data_clean(df, column = 'value'):
    #Get value cutoff for each of the ranges
    low = df[column].quantile(0.025)
    up = df[column].quantile(0.975)
    
    # Remove values outside range
    df_clean = df[(df[column] > low) & (df[column] < up)]
    
    return df_clean

def data_avg(df):

    
    return df

#Part 1
def draw_line_plot(df):
    fig = plot.subplots(figsize=(12, 4))
    fig = plot.plot('date', 'value',color = 'r', data = df)
    
    plot.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plot.xlabel('Dates')
    plot.ylabel('Page Views')


    #Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot(df):

    
    #
    df_bar = df.copy()
    # grouping and organizing the df parts
    df_bar_group = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar_group = df_bar_group.unstack(level='month')
   

    # Draw bar plot
    fig = df_bar_group.plot.bar(figsize=(7,7)).figure
    plot.xlabel('Years');
    plot.ylabel('Average Page Views');
    plot.legend(title='Months');

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace= True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, axes = plot.subplots(1, 2, figsize=(10,4))

    #Subplot for yearly page views, left plot ax=axes[0]
    ax1 = sns.boxplot(data= df_box, x = "year", y = "value", ax=axes[0], palette="Set1")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")

    #subplot for monthly page views, right plot ax=axes[1]
    ax2 = sns.boxplot(data=df_box, x="month", y="value", ax=axes[1], order=months, palette="Set1")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


df = data_clean(df)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month_name()







#draw_line_plot(df)
#draw_bar_plot(df)
draw_box_plot()
plot.show()