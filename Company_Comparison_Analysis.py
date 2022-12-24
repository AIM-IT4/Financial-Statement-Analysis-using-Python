import pandas as pd

# Load financial data for three comparable companies
data = {'Company': ['Company A', 'Company B', 'Company C'],
        'Revenue': [100, 120, 90],
        'Expenses': [80, 90, 70],
        'Equity': [50, 60, 40],
        'Stock Price': [10, 12, 9],
        'Earnings per Share': [2, 2.4, 1.8]}
df = pd.DataFrame(data)

# Calculate financial ratios and valuation metrics
df['Profit Margin'] = (df['Revenue'] - df['Expenses']) / df['Revenue']
df['ROE'] = (df['Revenue'] - df['Expenses']) / df['Equity']
df['P/E Ratio'] = df['Stock Price'] / df['Earnings per Share']
df['EV/EBITDA'] = (df['Stock Price'] * df['Equity']) / (df['Revenue'] - df['Expenses'])

# Print the results
print(df)
