# 1. Import the data
import pandas as pd

df = pd.read_csv("medical_examination.csv")

# 2. Create the overweight column
df['BMI'] = df['weight'] / (df['height']/100)**2
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw a Categorical Plot
def draw_cat_plot():
    # Draw the catplot
    # Replace None with the correct code
    pass

# 5. Create a DataFrame for the cat plot
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# 6. Group and reformat the data in df_cat
df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

# 7. Convert the data into long format and create a chart
import seaborn as sns

def draw_cat_plot():
    # Draw the catplot
    # Replace None with the correct code
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    return fig

# 8. Draw the Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) &
        (df['ap_lo'] <= df['ap_hi'])
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = ...

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Plot the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})

    return fig
