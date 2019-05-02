import os, csv

# Files to load and output
file_load = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("analysis", "budget_analysis.txt")


months_total = 0
net_changes_list = []
month_of_change = []
total_net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]


# Read the csv and convert it into a list of dictionaries
with open(file_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    # Extract first row to avoid appending to net_changes_list
    first_row = next(reader)
    months_total = months_total + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Total Votes
        months_total = months_total + 1
        total_net = total_net + int(row[1])

        # Net Change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_changes_list = net_changes_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Greatest Increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Greatest Decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average net change
net_monthly_avg = sum(net_changes_list) / len(net_changes_list)

# Summary
summary = (
    f"Total Months: {months_total}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print summary in terminal
print(summary)

# Export results to text file
with open(file_output, "w") as txt_file:
    txt_file.write(summary)
