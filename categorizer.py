def categorize_spending(amount, category):
    if category == 'Food':
        return f'Amount spent on Food: ${amount}'
    elif category == 'Travel':
        return f'Amount spent on Travel: ${amount}'
    elif category == 'Shopping':
        return f'Amount spent on Shopping: ${amount}'
    elif category == 'Entertainment':
        return f'Amount spent on Entertainment: ${amount}'
    elif category == 'Utilities':
        return f'Amount spent on Utilities: ${amount}'
    else:
        return f'Amount spent in Other category: ${amount}'

# Example usage:
print(categorize_spending(50, 'Food'))
print(categorize_spending(100, 'Travel'))
print(categorize_spending(25.99, 'Shopping'))
print(categorize_spending(75.50, 'Entertainment'))
print(categorize_spending(45, 'Utilities'))
print(categorize_spending(20, 'Other'))