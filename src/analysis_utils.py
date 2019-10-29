from datetime import datetime  
from collections import defaultdict


def time_of_bordercrossing(datum):
    """
    Takes as input a dictionary containing info about a single boarder crossing (datum) and
    and returns the year and month of the year during which the border was crossed.
    
    """

    try:
         border_crossing_date = datetime.strptime(datum['Date'],
            '%m/%d/%Y %H:%M:%S %p')

         month = int(border_crossing_date.strftime('%-m'))
         year = int(border_crossing_date.strftime('%Y'))
         return (year, month)
    except ValueError as ve:  
         print(ve) 
