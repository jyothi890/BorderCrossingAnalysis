# Insight Data Engineering Coding Challenge
# Table of Contents
1. Problem
2. Input
3. Output
4. Approach
5. Run Instructions
6. Tests

# Problem

The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

For this challenge, we want to you to calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. We also want to know the running monthly average of total number of crossings for that type of crossing and border.

# Input

For this challenge, you will be given an input file, Border_Crossing_Entry_Data.csv, that will reside in the top-most input directory of your repository.

For the purposes of this challenge, you'll want to pay attention to the following fields:

- Border: Designates what border was crossed
- Date: Timestamp indicating month and year of crossing
- Measure: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
- Value: Number of crossings

# Output

Using the input file, you must write a program to

- Sum the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
- Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of Border and Measure, or means of crossing.

Your program must write the requested output data to a file named report.csv in the top-most output directory of your repository.
Each line of the report.csv file contains these fields in this order:
- Border: Designates what border was crossed
- Date: Timestamp indicating month and year of crossing
- Measure: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
- Value: Sum of  number of crossings of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month
- Average: Running monthly average of total crossings for that combination of Border and Measure, or means of crossing.

The lines should be sorted in descending order by

- Date
- Value (or number of crossings)
- Measure
- Border

# Approach

My approach to this problem is understand date in the input file, read the file row by row to sum and save the values in dictionary, sort dictionary and write date to output file.

Version #1

Spontaneously I felt that data could be easily handled when captured in dictionary. At first, as part of rapid prototyping, I read through the contents of file and saved the data in the dictionary. I used nested dictionary as it perfectly suited the problem. A saperate utility function is defined to parse the  date in each row to retrieve year and month. To obtain total number of crossings by month  the dicitonary is designed such that the othermost key is border, followed by measure,year and month as inner keys and sum of number of crossings as dictionary value.

But I realizied that I could not calculate runnning monthly average with this design of nested dicitonary since data cannot be ordered by year and month across borders and measures. So I re-designed the nested dictionary.

Version #2

The latest nested dictionary consists of year as outermost key followed by month,measure and border as inner keys. For calculating running monthly average this dictionary is sorted by year and month. For each combination of border and measure (sorted by year and month) a supporting dicitonary is used in parallel to hold cumulative sum of no of crossings upto that month. This supporting dicitonary holds cumulative sum and no of months visited so far. For each value of sum of no_of_crossings in nested dicitonary , a row is added to list for combination of year, month, measure, border, value(sum of no_of_crossings for that month) and running month average(calculated by using cumulative sum).

I found that no of crossings for few measures in a month are 0. These months are not considered in our calculation.
