# Data-Python
Developing console application from a local .csv file

# CSV Reader Script
Introduction
This Python script reads data from a CSV (Comma-Separated Values) file and prints the content to the console. It's designed to work with any standard CSV file.

# Requirements
Python 3.x

# Installation
No additional installation is required. Just clone this repository or download the script.

# Usage
Save this script in your Text Editor using Python from your terminal:

    #!/bin/bash

    #Define the path to your CSV file
    csv_file="data.csv" 

    #Check if the file exists
    if [[ -f "$csv_file" ]]; then
      echo "Reading from $csv_file:"
      echo ""

    #Read and print the contents of the file line by line
    while IFS= read -r line
    do
           echo "$line"
        done < "$csv_file"
    else
        echo "Error: File '$csv_file' not found."
      fi

Name and save file .sh

Run the command `chmod +x read_csv.sh` to make the script executable. 


`./yourscriptfile.sh`
Replace 'yourscriptfile' in the script with the name of your .sh file.

# CSV File Format
The script expects a standard CSV file with comma-separated values. Example format:

Name,Age,City
- Alice,30,New York
- Bob,25,Los Angeles

Example
Given a CSV file with the following content:

Name,Age,City
- Alice,30,New York
- Bob,25,Los Angeles


The output will be:

Name, Age, City
Alice, 30, New York
Bob, 25, Los Angeles

