"""
Module that validates the flight school's records.

This is the primary module that does all of the work. It loads the files, loops through
the lessons, and searches for any takeoffs that violate insurance requirements.

Technically, we could have put many of these functions in __main__.py.  That is the
main module of this application anyway.  However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: Federico Sacasa
Date: June 12th, 2022
"""
import utils
import tests
import os.path
import violations


def discover_violations(directory,output):
    """
    Searches the dataset directory for any flight lessons the violation regulations.
    
    This function will call list_weather_violations() to get the list of weather violations.
    If list_endorsment_violations (optional) is completed, it will call that too, as
    well as list_inspection_violations.  It will concatenate all of these 2d lists
    into a single 2d list of violations (so a flight may be listed more than once for
    each of the three types of violations).
    
    If the parameter output is not None, it will create the CSV file with name output
    and write the 2d list of violations to this file.  This CSV file should have the
    following header:
    
        STUDENT,AIRPLANE,INSTRUCTOR,TAKEOFF,LANDING,FILED,AREA,REASON
    
    Regardless of whether output is None, this function will print out the number of
    violations, as follows:
    
        '23 violations found.'
    
    If no violations are found, it will say
    
        'No violations found.'
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', 'teachers.csv', 'lessons.csv',
    'fleet.csv', and 'repairs.csv'.
    
    Parameter output: The CSV file to store the results
    Precondition: output is None or a string that is a valid file name
    """
                      # Implement this function
    header = ['STUDENT','AIRPLANE','INSTRUCTOR','TAKEOFF','LANDING','FILED', 'AREA','REASON']
    res1 = [header]
    result = violations.list_weather_violations(directory)
    tot = len(result)
    for r in range(tot):
        res1.append(result[r])
    if output != None:
        utils.write_csv(res1,output)
    if tot == 0:
        print('No violations found.')
    elif tot == 1:
        print('1 violation found.')
    else:
        print(str(tot)+' violations found.')


def execute(args):
    """
    Executes the application or prints an error message if executed incorrectly.
    
    The arguments to the application (EXCLUDING the application name) are provided to
    the list args. This list should contain either 1 or 2 elements.  If there is one
    element, it should be the name of the data set folder or the value '--test'.  If
    there are two elements, the first should be the data set folder and the second
    should be the name of a CSV file (for output of the results).
    
    If the user calls this script incorrectly (with the wrong number of arguments), this
    function prints:
    
        Usage: python auditor dataset [output.csv]
    
    This function does not do much error checking beyond counting the number of arguments.
    
    Parameter args: The command line arguments for the application (minus the application name)
    Precondition: args is a list of strings
    """
                      # Implement this function
    invalid = len(args) == 0 or len(args) > 2
    dataset = None
    output  = None
    if not invalid and '--test' in args:
       invalid = len(args) == 2
    elif not invalid:
       dataset = args[0]
       if len(args) == 2:
           output = args[1]
  
    if invalid:
       print('Usage: python auditor dataset [output.csv]')
    elif dataset is None:
       tests.test_all()
    else:
       discover_violations(dataset,output)
       pass
