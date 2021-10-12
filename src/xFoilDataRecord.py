from csv import writer
import os

DIR = "C:\\Users\\Akira\\Desktop\\Code\\XFoilAutomation\\delft2_polars"
#"C:\\Users\\Akira\\Desktop\\Code\\XFoilAutomation\\delft_polars"
#"C:\\Users\\Akira\\Desktop\\Code\\XFoilAutomation\\uiuc_polars"
#"C:\\Users\\Akira\\Desktop\\Code\\XFoilAutomation\\uiuc2_polars"

#Getting data from text file
for dir in DIR:
    for f in os.listdir(dir):
        dataFile = open(f, 'r')
        lines = dataFile.readlines()
        with open('all_data.csv', 'a') as file:
            writer_object = writer(file)
            for l in lines[12:]:
                d = l.split()
                writer_object.writerow(d)
            file.close()


#Must manually insert Cl/Cd, delete empty rows and add Reynold's number and Mach number