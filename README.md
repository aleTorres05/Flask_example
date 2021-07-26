# FLASK BLUEPRINT TASK
Flask Blueprint "Find distance"

## Sub Topic Headings H2
important external libraries to be installed

````
pip install Flask
````

````
pip install haversine
````
which is used to obtain the latitude and longitude of a certain location 
````
pip install loguru
````
Which is used to add the response to a .log file 

The above libraries are need in order to run the program 

## Usage

Below is another example of displaying
````python
import csv

with open("sample.csv","r") as csvinput: # read input csv file
    reader = csv.reader(csvinput) # create a reader
    for row in reader:
        print(row[0])
````