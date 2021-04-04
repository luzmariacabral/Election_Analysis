import csv
import os

# Assign a variable load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    #print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add ti the total vote count.
        total_votes +=1

        # Print the candidate name from each row.
        candidate_name = row[2]
        #Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)
        # If the candidate does not match any axisting candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #  Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through the counts.
        #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
            #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Determine winning vote count and candidate[]
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage - vote_percentage
            # 3. Set the winning_candidate equa to the candidate's name.
            winning_candidate = candidate_name
    # To do: print out each candidate's name, vote count, and percentage of votes to termina.
        print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

    # To do: print out the winning candidate, vote count and percentage to terminal.
# Print the candidate vote dictionary
#print(candidate_results)




#Print the candidate list
#print(candidate_options)
      #print(row)
#3. Print the total votes.
#print(total_votes)

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