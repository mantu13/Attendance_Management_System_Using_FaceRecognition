import os
import csv

# Step 1: Create the directory if it doesn't exist
directory = 'StudentDetails'
if not os.path.exists(directory):
    os.makedirs(directory)

# Step 2: Create or open the CSV file
file_path = os.path.join(directory, 'StudentDetails.csv')

# Open the file in append mode
with open(file_path, 'a+', newline='') as csvFile:
    # Create a CSV writer object
    csvWriter = csv.writer(csvFile)

    # Optional: Write a header if the file is empty
    csvFile.seek(0)  # Move to the beginning of the file
    if csvFile.read(1) == '':  # Check if the file is empty
        csvWriter.writerow([' roll', 'name', 'image'])  # Example header

    # You can now write data to the CgeSV file
    # Example: csvWriter.writerow(['John Doe', 20, 'A'])