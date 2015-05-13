import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt

# parse_raw_donut_data
#
# Extracts data from raw Outlook messages (saved in text format) and writes
# the data to a formatted CSV
#
# Arguments:
# infiles : list object of input text files, named by category
#   Example: ["cake.txt", "donuts.txt", "cookies.txt", etc...]
# outfile : CSV text file to write values to
def parse_raw_donut_data(infiles, outfile):
    with open(outfile, 'w') as fout:
        for infile in infiles:
            # Grab the name of this category from the file
            category = infile[0:infile.find(".")]
            with open(infile, 'r') as fin:
                for line in fin:
                    # scan for header information
                    if line[0:5] == "From:":
                        # Grab the sender and formatted time of each message
                        sender = line[6:]
                        date = dt.datetime.strptime(next(fin)[6:], "%A, %B %d, %Y %I:%M %p\n")
                        # Append to the output CSV
                        fout.write(dt.datetime.strftime(date, "%c") + "," + category + ',' + sender)


# read_in_donut_data
#
# Reads in formatted donut data from a file
#
# Arguments:
# infile: file containing CSV of formatted donut data
#
# Returns:
# List containing donut data in the format:
#   [[datetime, category, sender],
#    [datetime, category, sender],
#    [datetime, category, sender],
#    ... ]
def read_in_donut_data(infile):
    data = []
    with open(infile, 'r') as fin:
        for line in fin:
            event = line.split(',')
            date = dt.datetime.strptime(event[0], "%c")
            category = event[1]
            sender = event[2][0:-1]
            data.append([date, category, sender])
    return data


        

        
        
