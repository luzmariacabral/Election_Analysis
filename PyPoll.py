import csv
import os

# Assign a variable load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    #print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.
    #for row in file_reader:
      #print(row)
# Close the file.
#election_data.close()

#Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:
#write three counties to the file. 
    #txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")



#Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
#Write some data to the file.
#outfile.write("Hello World")

#Close the file
#txt_file.close()

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.