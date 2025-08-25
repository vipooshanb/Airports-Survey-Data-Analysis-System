"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: 
 4. Date: 
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name - set by the var 'selected_data_file' into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)


"""
EDIT THE CODE BELOW TO COMPLETE YOUR SUBMISSION
"""
selected_data_file="CDG2021.csv" #hard coded csv name to be replaced with a dynamically created filename
load_csv(selected_data_file) #calls the function "load_csv" sending the variable 'selected_data_file" as a parameter


#-----------------------------------------------------------------------------------------------------------------
#Some Example code queries to be replaced with those required by the brief - compare these outputs to the CSV file

first_row = data_list[0] #asign the list from the first row of the CSV to the var 'first_row'
second_item_in_secrow = data_list[1][1] #asign the second item (the flight number) from the second row of the CSV to a variable
third_item_in_thirdrow = data_list[2][2] #asign the third item (sheduled departure time) from the third row of the CSV to a variable

#PRINT THE OuTPUT TO SCREEN
print (f"The current file name is {selected_data_file}")
print ("")
print (f"First row of data_list is data_list[0] -> {first_row}")
print ("")
print (f"Second item of the second row is data_list[1][1] -> {second_item_in_secrow}")
print ("")
print (f"Third item of the third row is data_list[2][2] -> {third_item_in_thirdrow}")








