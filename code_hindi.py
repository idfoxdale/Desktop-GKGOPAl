import pandas as pd
h_dataset = pd.read_csv('hindi_dataset.tsv', sep='\t')
print(h_dataset.head())


""" print(h_dataset.shape)
print(h_dataset.columns)
print(h_dataset.describe())
print(h_dataset.info())
print(h_dataset.isnull().sum())
print(h_dataset.isnull().sum()/h_dataset.shape[0]) """

""" 
# Simple Way to Read TSV Files in Python using csv
# importing csv library
import csv

# open .tsv file
with open("hindi_dataset.tsv") as file:
	
	# Passing the TSV file to
	# reader() function
	# with tab delimiter
	# This function will
	# read data from file
	tsv_file = csv.reader(file, delimiter="\t")
	
	# printing data line by line
	for line in tsv_file:
		print(line)
 """