##### EFI ONLINE_ORDERING_ORDER_APPROVER Parser ####

#### Input Parameters ####
# 1--> pattern
# 2--> input directory path
# 3--> Output directory path
##########################
import sys
import os
import glob

# making global output file variable
output = ''

def processor(files_list, input_directory, output_directory):

        global output

        for file in files_list:
                #open input, output files
                data = open(input_directory + '/' + file, 'r')
                output = open(output_directory + '/' + file, 'w')
                header = data.readline()
                header = header.strip('\n')
                header = header.split(',')

                #write header to output file
                output.write(','.join(header))
                output.write('\n')

                #iterate over each row in data
                for row in data:
                    if (row.count(',') == 5):
                        output.write(row)
                    else:
                        #print(row)
                        fields = row.split(',')
                        fields[3:-2] = [' '.join(fields[3:-2])]
                        output.write(','.join(fields))
                        output.write('\n')

                output.close()
                data.close()


def main():

        length = len(sys.argv)
        pattr=sys.argv[1]
        input_directory = sys.argv[2]
        output_directory = sys.argv[3]
        files_list = glob.glob(input_directory + '/' + pattr)

        files_list = [ file.split('/')[-1] for file in files_list ]

        processor(files_list, input_directory, output_directory)

if __name__ == "__main__":
    main()

