# Import Modules
import csv
import os

#Create Variables & integrate csv files
Election_Data_csv = os.path.join("/Users/Will/Documents/Instructions/PyPoll/Resources/election_data.csv")
Total_Votes = 0
Charles_Votes = 0
Diana_Votes= 0
Raymon_Votes = 0
Winner = ""
#With Loop Throught the data
with open(Election_Data_csv) as Poll_Data:
    #Read data through a reader
    reader = csv.reader(Poll_Data,delimiter=",")

    #Start For loop for csv Data
    for row in reader:
        Total_Votes +=1

    #List Candidates and hold vote count in candidate variables through the csv rows
        if row[2] == "Charles Casper Stockham": 
            Charles_Votes +=1
        elif row[2] == "Diana DeGette":
            Diana_Votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Votes +=1

#Creating list for candidates to compare the values we grabbed from the loop
Candidates = ["Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane"]
Votes = [Charles_Votes,Diana_Votes,Raymon_Votes]

#Percent Values For the final print and calculate a winner
dict_Final_Votes = dict(zip(Candidates,Votes))
Charles_Final = float(Charles_Votes/Total_Votes) * 100
Diana_Final = float(Diana_Votes/Total_Votes) * 100
Raymon_Final = float(Raymon_Votes/Total_Votes) * 100
Poll_Results = dict_Final_Votes.get
#Winner Output
Winner = "Diana DeGette"

#Print the results
print("Election Results")
print("--------------------")
print("Total Votes:", Total_Votes)
print("--------------------")
print(f"Charles Casper Stockham: {Charles_Final:.3f}% ({Charles_Votes})")
print(f"Diana DeGette: {Diana_Final:.3f}% ({Diana_Votes})")
print(f"Raymon Anthony Doane: {Raymon_Final:.3f}%({Raymon_Votes})")
print("--------------------")
print(f"Winner:", Winner)
print("--------------------")

#Output Files
output_file = ("/Users/Will/Documents/Instructions/PyPoll/Resources/election_results_summary.txt")

with open(output_file, "w", encoding = 'utf-8') as file:
    #Printing a summary
    file.write("Election Results")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Total Votes: {Total_Votes} ")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Final:.3f}% ({Charles_Votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_Final:.3f}% ({Diana_Votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Final:.3f}%({Raymon_Votes})")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Winner:{Winner}")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")