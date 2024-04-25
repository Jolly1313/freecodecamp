import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
def import_data():
    df = pd.read_csv("epa-sea-level.csv")
    return df

# 2. Create a scatter plot
def create_scatter_plot(df):
    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level')
    
    # 3. Get the slope and y-intercept of the line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create arrays for the line plot
    x_values = df['Year']
    y_values = slope * x_values + intercept
    
    # 4. Plot the line of best fit
    plt.plot(x_values, y_values, color='red', label='Line of Best Fit')
    
    # 5. Plot a new line of best fit from year 2000 to the most recent year
    recent_years = df[df['Year'] >= 2000]['Year']
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years, df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x_values_recent = list(range(2000, 2051))
    y_values_recent = slope_recent * x_values_recent + intercept_recent
    plt.plot(x_values_recent, y_values_recent, color='green', label='Recent Line of Best Fit')
    
    # 6. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add legend
    plt.legend()
    
    # Save the plot
    plt.savefig('sea_level_plot.png')
    
    # Show plot
    plt.show()
    
# Main function to execute
if __name__ == "__main__":
    df = import_data()
    create_scatter_plot(df)
