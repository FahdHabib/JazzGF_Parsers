##### EFI Scratch Card Tracking Parser ####

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
                
                
                #update header with new column
                header.insert(3,"SC_VALUE")
                
                #write header to output file
                output.write(','.join(header))
                output.write('\n')
              
                #iterate over each row in data
                for row in data:
                        row = row.strip('\n')
                        row = row.split(',')
                        # check if QUANTITY is 1
                        if row[4] == '1':
                            #adding start_range value to sc value column
                            row.insert(3, row[1])
                            #write row to output file
                            output.write(','.join(row))
                            output.write('\n')
                        # check if QUANTITY is greater than 1
                        elif row[4] > '1':
                            #if QUANTITY is greater than 1, then add new rows with their respective sc values    
                            for i in range(int(row[4])):
                                new_row = row[:]
                                #adding start_range+i value to sc value column
                                new_row.insert(3, str(int(row[1])+i))
                                
                                #write row to output file
                                output.write(','.join(new_row))
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
