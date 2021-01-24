
import os
import csv

# specify output file path
output_txt = os.path.join('Analysis', 'summary.txt')

# specify input file path
budget_data = os.path.join('Resources', 'budget_data.csv')

# define variables and give initial values
mo_count = 0
net_PL = 0
first_mo_PL = 0
last_mo_PL = 0
current_mo_PL = 0
next_mo_PL = 0
max_profit = 0
max_profit_mo = ""
min_profit = 0
min_profit_mo = ""

# open and read the CSV
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    #read the header row
    csv_header = next(csv_file)
    
    # loop through csv file
    for row in csv_reader:

        # get the first month
        if mo_count == 0:
            first_mo_PL = float(row[1])

        # sum month total and net Profit/Loss
        mo_count += 1
        net_PL += float(row[1])

        # max and min Profit (i.e. max Loss)
        next_mo_PL = float(row[1])        
        difference = next_mo_PL - current_mo_PL
        current_mo_PL = float(row[1])
        
        if difference > max_profit:
            max_profit = difference
            max_profit_mo = row[0]
        if difference < min_profit:
            min_profit = difference
            min_profit_mo = row[0]

# calculate total difference in P/L
last_mo_PL = float(row[1])  
total_difference = last_mo_PL - first_mo_PL

# get average change
average_difference = (total_difference) / (mo_count - 1)

# Print Results
print('Financial Analysis')
print('-------------------')
print('\n')
print(f'Total Months: {mo_count}')
print(f'Total: ${round(net_PL,0)}')
print(f'Average Change: ${round(average_difference,2)}')
print(f'Greatest Profit Increase: {max_profit_mo}: ${max_profit}')
print(f'Greatest Profit Decrease: {min_profit_mo}: ${min_profit}')

# write to txt file
with open(output_txt, 'w') as writer:
    writer.write('Financial Analysis')
    writer.write('\n')
    writer.write('-------------------')
    writer.write('\n')
    writer.write(f'Total Months: {mo_count}')
    writer.write('\n')
    writer.write(f'Total: ${round(net_PL,0)}')
    writer.write('\n')
    writer.write(f'Average Change: ${round(average_difference,2)}')
    writer.write('\n')
    writer.write(f'Greatest Profit Increase: {max_profit_mo}: ${max_profit}')
    writer.write('\n')
    writer.write(f'Greatest Profit Decrease: {min_profit_mo}: ${min_profit}')