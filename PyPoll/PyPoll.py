import os, csv

# Files to load and output
file_load = os.path.join("Resources", "election_data.csv")
file_output = os.path.join("analysis", "election_analysis.txt")

# Empty counters
total_votes = 0
candidates_list = []
candidate_votes = {}
winning_count = 0
winning_candidate = ""

# Read the csv and convert it to a list of dictionaries
with open(file_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates_list:

            # Add it to list of candidates in the running
            candidates_list.append(candidate_name)

            # Start tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to text file
with open(file_output, "w") as txt_file:

    # Print the final vote count to terminal
    print(f"Total Votes: {total_votes}")

    # Save the final vote count to the text file
    txt_file.write(f"Total votes: {total_votes}\n")

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage to terminal
        voter_output = f"{candidate}: {vote_percentage:.2f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate to terminal
    print(f"Winner: {winning_candidate}")

    # Save the winning candidate's name to the text file
    txt_file.write(f"Winner: {winning_candidate}")
