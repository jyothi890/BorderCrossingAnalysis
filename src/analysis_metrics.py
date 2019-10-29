import csv  
import collections
from math import ceil
import analysis_utils


def total_crossings_monthly_by_measure(in_file):
    """
    This function takes full data from the specified input file and returns a nested  
    dictionary that holds total number of crossing for each type of measure(type of crossing)
    against a border for that month.
    
    """

    # set up a dictionary to hold the values for the cleaned and trimmed
    # data point

    bordercrossing = collections.defaultdict(lambda : \
            collections.defaultdict(lambda : \
            collections.defaultdict(lambda : \
            collections.defaultdict(int))))
    try:
        with open(in_file, 'r') as f_in:

            # set up csv DictReader object ##

            trip_reader = csv.DictReader(f_in)

            # collect data from and process each row

            for row in trip_reader:

            # set variables to data points

                border = row['Border']
                measure = row['Measure']
                # call date utility fuction to extract year and month
                (year, month) = \
                    analysis_utils.time_of_bordercrossing(row)
                crossings = int(row['Value'])

                # sum up the crossings based on measure and border

                if crossings > 0:
                    bordercrossing[year][month][measure][border] += \
                        crossings
    except IOError:
        sys.stderr.write('Unable to open the log file' + '\n')
    except Exception as e:
        print (e)
        raise Exception('Unhandled' + '\n')
    return bordercrossing


def calculate_running_monthly_average(in_file):
    """
    This function takes full data from the specified input file
    and returns a list of running monthly average for the combinations of year,month,measure and border.
    The list has data as : [year,month,measure,border,sum_of_crossings(for that month),running monthly average]
    """

    # List to hold Running Monthly Average of total crossings

    bordercrossing_rma = list()

    # Tuple to hold cumulative sum and count of months

    sumupto = collections.namedtuple('sumupto', 'sum_so_far, months')

    # Dictionary to hold each measure's cumulative sum upto the month visited and number of months

    cumulative_total = collections.defaultdict(lambda : \
            collections.defaultdict(tuple))

    # Collect data from and process each row

    for (year, months) in \
        sorted(total_crossings_monthly_by_measure(in_file).items()):
        for (month, measures) in sorted(months.items()):
            for (measure, borders) in measures.items():
                for (border, value) in borders.items():
                    
                    # for new combination border and measure cumulative total is no of crossings from 
                    # the first month and running monthly average is 0.
                    if not cumulative_total[border][measure]:
                        cumulative_total[border][measure] = \
                            sumupto(sum_so_far=value, months=1)
                        bordercrossing_rma.append((
                            year,
                            month,
                            measure,
                            border,
                            value,
                            0,
                            ))
                    else:
                        # for existing combination border running monthly average is calculated
                        # based on cumulative total recorded till current month.
                        average = \
                            int(ceil(cumulative_total[border][measure][0]
                                / cumulative_total[border][measure][1]))
                        bordercrossing_rma.append((
                            year,
                            month,
                            measure,
                            border,
                            value,
                            average,
                            ))
                        # The current month no of crossing is added to cumulative total for
                        # futur calculations of running monthly average for that border and measure
                        cumulative_total[border][measure] = \
                            sumupto(sum_so_far=cumulative_total[border][measure][0]
                                    + value,
                                    months=cumulative_total[border][measure][1]
                                    + 1)

    return bordercrossing_rma
