from prettytable import PrettyTable

# Initialize the table with column names
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Add rows
myTable.add_row(["Leanord", "X", "B", "91.2 %"])
myTable.add_row(["Penny", "X", "C", "63.5 %"])
myTable.add_row(["Howard", "X", "A", "90.23 %"])
myTable.add_row(["Bernadette", "X", "D", "92.7 %"])
myTable.add_row(["Sheldon", "X", "A", "98.2 %"])
myTable.add_row(["Raj", "X", "B", "88.1 %"])
myTable.add_row(["Amy", "X", "B", "95.0 %"])

print(myTable)

from tabulate import tabulate

# Data
mydata = [
    ["Nikhil", "Delhi"],
    ["Ravi", "Kanpur"],
    ["Manish", "Ahmedabad"],
    ["Prince", "Bangalore"]
]

# Header
head = ["Name", "City"]

# Display table
print(tabulate(mydata, headers=head, tablefmt="grid"))

input('press any key to exit .....')
