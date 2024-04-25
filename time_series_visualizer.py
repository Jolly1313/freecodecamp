import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the data
def import_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    return df

# 2. Clean the data
def clean_data(df):
    # Filter out days when page views were in the top 2.5% or bottom 2.5% of the dataset
    bottom_thresh = df['value'].quantile(0.025)
    top_thresh = df['value'].quantile(0.975)
    df_cleaned = df[(df['value'] >= bottom_thresh) & (df['value'] <= top_thresh)]
    return df_cleaned

# 3. Draw a line plot
def draw_line_plot(df):
    # Create a line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('line_plot.png')
    
    return fig

# 4. Draw a bar plot
def draw_bar_plot(df):
    # Create a new DataFrame for monthly average page views
    df_bar = df.groupby([df.index.year, df.index.month]).mean().unstack()

    # Create a bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_abbr[i] for i in range(1, 13)])
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('bar_plot.png')
    
    return fig

# 5. Draw box plots
def draw_box_plot(df):
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Create box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    sns.boxplot(x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1]).set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('box_plot.png')
    
    return fig
