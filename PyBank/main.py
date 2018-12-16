import os
import csv
import pandas as pd

csvpath = os.path.join("resources/budget_data.csv")

with open(csvpath,'r',newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    total_months = 0
    total_amt = 0
    previous_month = 0
    differences = []
    dates = []
    for row in csv_reader:
        if not total_months == 0:
            differences.append(int(row["Profit/Losses"])-previous_month)
        total_months += 1
        total_amt += int(row["Profit/Losses"])
        previous_month = int(row["Profit/Losses"])
        dates.append(row["Date"])

    #Calculate average change
    average_change = sum(differences)/len(differences)

    #Assign variables for the greatest increases
    greatest_increase_amt = max(differences)
    max_index = differences.index(greatest_increase_amt)
    greatest_increase_date = dates[max_index + 1]

    #Assign variables for greatest decreases
    greatest_decrease_amt = min(differences)
    dec_index = differences.index(greatest_decrease_amt)
    greatest_decrease_date = dates[dec_index + 1]

    ## things that work:
    print(f'''
    Financial Analysis:
    Total months: {total_months}
    Net Profit/Loss: {total_amt}
    Average change: {average_change}
    Greatest increase (month, amount): {greatest_increase_date} (${greatest_increase_amt})
    Greatest decrease (month, amount): {greatest_decrease_date} (${greatest_decrease_amt})
    ''', file=open("financial_summary.txt", "a"))



