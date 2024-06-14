import os
import csv

# connecting path to the text file given
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# creating list and a counter variable to be used to save our data from the file
date = []
netTotal = 0
date_dict = {}
average_calc_total = []

# read through the file
with open(budget_data_csv, 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # removing the header of the file and storing it in a variable
    header = next(csv_reader)
    
    for row in csv_reader:
        
        # Add the dates to a list
        date.append(row[0])
        
        # Total up profit/losses
        netTotal += int(row[1])
        
        # dictionary with date as key and profit/losses as value
        date_dict[row[0]] = int(row[1])
    
    # set total amount of months equal to the number of indexes in date list
    total_months = len(date)
    
    # initiating variables to count and add up values in a loop
    increase_total = 0
    current_total = 0
    decrease_total = 0
    
    # loop to calculate greatest increase in profits and greatest decrease in profits
    for i in range(len(date)-1):
        
        # find the change in profit/losses between the next month and the current month
        current_total = date_dict[date[i+1]] - date_dict[date[i]]
        
        # Create a list of the changes in profit/losses between each month
        average_calc_total.append(current_total)
        
        # saves the greatest value of increase in profits
        if current_total > increase_total:
            
            increase_total = current_total
            increase_current_date = date[i+1]
        
        # saves the greatest decrease in value in profits
        elif current_total < decrease_total:
            
            decrease_total = current_total
            decrease_current_date = date[i+1]
    
    # adding up the total of the changes between each month
    total = 0
    for i in average_calc_total:
        total += i
    
    # averaging the changes by the total number of changes
    # rounding the value to two decimal places
    average = round(total/len(average_calc_total),2)
    
print("Financial Analysis")
print('-----------------------------')
print(f"Total Months: {total_months}")
print(f'Total: ${str(netTotal)}')
print(f'Average Change: ${str(average)}')
print(f'Greatest Increase in Profits: {increase_current_date} (${str(increase_total)})')
print(f'Greatest Decrease in Profits: {decrease_current_date} (${str(decrease_total)})')

# make a new textfile and connecting a path to it
output_file = os.path.join('analysis', 'results.csv')

# open the textfile and write into it
with open(output_file, 'w') as csvfile:
    
    csv_writer = csv.writer(csvfile, delimiter=',')
    
    csv_writer.writerow(['Financial Analysis'])
    csv_writer.writerow(['------------------------------------'])
    csv_writer.writerow([f"Total Months: {total_months}"])
    csv_writer.writerow([f'Total: ${str(netTotal)}'])
    csv_writer.writerow([f'Average Change: ${str(average)}'])
    csv_writer.writerow([f'Greatest Increase in Profits: {increase_current_date} (${str(increase_total)})'])
    csv_writer.writerow([f'Greatest Decrease in Profits: {decrease_current_date} (${str(decrease_total)})'])