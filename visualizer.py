import matplotlib.pyplot as plt
import pandas as pd

# Function to generate a pie chart for monthly spending

def generate_spending_pie_chart(data):
    # Data should be a dictionary with categories as keys and spending as values
    categories = data.keys()
    spending = data.values()

    plt.figure(figsize=(8, 8))
    plt.pie(spending, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Monthly Spending Pie Chart')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.show()

# Function to generate summary statistics

def generate_summary_statistics(data):
    # Data is assumed to be a dictionary with categories as keys and spending as values
    total_spending = sum(data.values())
    average_spending = total_spending / len(data)

    print('Total Spending:', total_spending)
    print('Average Spending:', average_spending)
    for category, amount in data.items():
        print(f'{category}: {amount}')