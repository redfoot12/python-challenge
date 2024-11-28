import os
import csv

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
monthly_difference = []
average_change = 0
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    csvreader = csv.reader(financial_data)

    # Skip the header row
    header = next(csvreader)
         
    firstRow = next(csvreader)

    total_months = total_months + 1

    total_net += float(firstRow[1])
    
    # set up last month
    priorMonth = float(firstRow[1])
       
    for row in csvreader:
      total_months = total_months + 1
       
      total_net += float(row[1])

      # calculate the next change
      netChange = float(row[1]) - priorMonth
      # add to the list of monthly changes
       # Extract first row to avoid appending to netChange list
      monthly_difference.append(netChange)

      # Add the first month that a change occurred
      months.append(row[0])

      priorMonth = float(row[1])

# Calculate the average net change across the months
average_change = sum(monthly_difference) / len(monthly_difference)

# Calculate the greatest increase in profits (month and amount)
greatest_increase = [months[0], monthly_difference[0]]
# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = [months[0], monthly_difference[0]]



# loop to calculate the index of the greatest and least monthly change
for m in range(len(monthly_difference)):
    if(monthly_difference[m] > greatest_increase[1]):
      greatest_increase[1] = monthly_difference[m]
      greatest_increase[0] = months[m]

    if(monthly_difference[m] < greatest_decrease[1]):
      greatest_decrease[1] = monthly_difference[m]
      greatest_decrease[0] = months[m]

# Generate the output summary
output = ( 
  f"\nFinancial Analysis\n"
  f"\n"
  f"------------------------------------------\n"
  f"\nTotal Months = {total_months:}"
  f"\n"
  f"\nTotal = ${total_net:}\n"
  f"\nAverage Change: ${average_change:.2f}\n"
  f"\nGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:.0f})\n"
  f"\nGreatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:.0f})\n"
  )
# Print the output
print(output)




# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    