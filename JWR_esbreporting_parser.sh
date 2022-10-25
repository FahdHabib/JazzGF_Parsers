#-------------------------------------------------------------------------
############################################################################
# There will be four input parameters which will be pased to the parser, they are mentioned as below 
##  $1 = inputDirectoryPath
##  $2 = outputDirectoryPath
##  $3 = logsDirectoryPath
##  $4 = sourceFilePattern
##  $5 = GCFR Buss Date


##  IF parser executed successfully then it must return 0 return code otherwise parser should return non zero return code
##  Also Parsing script Should validate whether required numbers of paramaeters are passed to the parser

# ---------------------------------------------------------------------------------------------------
# ERROR CODES & EXPLAINATION
# EXIT 0: Parser executed successfully...
# EXIT 1:  No of Parameters passed are less then the required...
# EXIT 2: Parser Failed...

# ---------------------------------------------------------------------------------------------------

############################################################################





echo "Call JWR ESB Reporting Logs Parser"

 
 #### # Parameters Validation - Doing initial Check for Parameters count ####

if [ "$#" -ne 5 ]; then

    echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Error : The number of parameters passed is not equal to the expected value.\n"

    echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Exiting : Error State 1"
    
    exit 1
fi


fileName=$(ls -td -- $1/$4 | head -n 1)


originalFileName="$(basename $fileName)"

echo $1
echo $2
echo $3
echo $4
echo $5

iconv -f UTF-8 -t ASCII//TRANSLIT "$fileName" > $2/ASCII_output.csv
sed -i 's/\"//g' $2/ASCII_output.csv

rc1=$?

echo "Logging" >>$3/logs.txt
mv $2/ASCII_output.csv $2/$originalFileName
rc=$?
if [ $rc1 -ne 0 ]
then
		echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Error : Parser Failed\n"
		echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Exiting : Error State 2"
		exit 2
else
    echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Parser executed successfully\n"

    echo -e `date "+%Y-%m-%d_%H%M%S"` '|' "Exiting  with return code 0"

	exit 0
fi
