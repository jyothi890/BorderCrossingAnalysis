import sys
import os
import analysis_metrics
import datetime
import time
import csv


def report(in_file, out_file):
    """
    This function takes full data from the specified input file
    and writes the condensed data to a specified output file. This is
    a wrapper method that calls utility and metric functions to clean and
    aggregate the data.
    """

    try:
        with open(out_file, 'w') as f_out:

        # csv DictWriter object - writer requires column names for the
        # first row as the "fieldnames" argument

            out_colnames = ['Border', 'Date', 'Measure', 'Value',
                            'Average']
            trip_writer = csv.DictWriter(f_out, fieldnames=out_colnames)
            trip_writer.writeheader()

        # collect data from and process each row
        # A list of running monthly average of total crossings for the combination
        # of border and measure is returned.This list is sorted in descending order of
        # year,month,value,measure and border.

            for row in \
                sorted(analysis_metrics.calculate_running_monthly_average(in_file),
                       key=lambda x: (x[0], x[1], x[4], x[2], x[3]),
                       reverse=True):
                new_point = {}
                new_point['Border'] = row[3]
                new_point['Date'] = datetime.datetime(
                    row[0],
                    row[1],
                    1,
                    0,
                    0,
                    0,
                    ).strftime('%m/%d/%Y %I:%M:%S %p')
                new_point['Measure'] = row[2]
                new_point['Value'] = row[4]
                new_point['Average'] = row[5]
                trip_writer.writerow(new_point)
    except IOError as e:
        print(e)
        sys.stderr.write('Unable to open the log file' + '\n')
    except Exception as e:
        print(e)
        raise Exception('Unhandled'+'\n')


def main():
    """
    This code logic parses command-line for correct inputs and subsequently calls functions to process
    data and generate report.
    """

    args = sys.argv[1:]
    usage = 'usage: <input_file> <output_file> '
    if not args:
        print (usage)
        sys.exit(1)

    # Check parameter

    if not os.path.isfile(args[0]):
        print (usage)
        print ('Provide a valid input filepath')
        sys.exit(1)
    else:
        input_filename = args[0]
    if len(args) == 1:
        print (usage)
        print ('Provide an output filename')
        sys.exit(1)
    if not os.path.isdir("/".join(args[1].split('/')[:-1])):
        print (usage)
        print ('Provide a valid output filepath')
        sys.exit(1)
    else:
        output_filename = args[1]
    try:
        print ('Start of Log  : ' \
            + datetime.datetime.fromtimestamp(time.time() + 24
                * 3600).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        report(input_filename, output_filename)
        print ('Output file : ' + args[1] + ' is created at path ' \
            + os.path.dirname(os.path.realpath(output_filename)))
    except Exception as e:
        sys.stderr.write('Error is ' + e.args[0] + '\n')
    finally:
        print ('End of Log  : ' \
            + datetime.datetime.fromtimestamp(time.time() + 24
                * 3600).strftime('%Y-%m-%d %H:%M:%S') + '\n')


if __name__ == '__main__':
    main()
