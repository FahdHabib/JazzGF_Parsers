##### MFS Pre Processor ####

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
		if(os.path.getsize(input_directory + '/' + file) > 0):
			data = open(input_directory + '/' + file, 'r')
			output = open(output_directory + '/' + file, 'w')
			for row in data:
				outdata = row.strip('\n')
				outdata = outdata.split(',')
				if len(outdata) > 84:
					outdata = outdata[:85]
					output.write(','.join(outdata))
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

