import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

if __name__ == "__main__":
    file_path = 'datagym.csv'  # Change this to the path of your CSV file
    read_csv(file_path)