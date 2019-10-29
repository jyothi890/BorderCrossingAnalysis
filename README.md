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
