import matplotlib.pyplot as plt
import csv
import numpy as np

'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya\

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.  
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)
'''
plt.figure("Energy Efficiency of Schools", tight_layout=True, figsize=(11, 7.2), facecolor="lightgreen")

with open("files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

school_data = []
for i in range(len(data)):
    if data[i][6] == "K-12 School":
        school_data.append(data[i])
headers = school_data.pop(0)
school_data = [x for x in school_data if x[21] != '']
new_data = []

for school in school_data:
    try:
        float(school[21])
        new_data.append(school)
    except:
        # print(school[21])
        pass

school_data = new_data[:]
school_data.sort(key=lambda x: float(x[21]))
print(school_data)

ghg_data = []
sqrft_data = []
ghg_intesity_data = []
for i in range(len(school_data)):
    try:
        emissions = (float(school_data[i][20]))
        ghg_data.append(emissions)
        sqr_footage = (float(school_data[i][7]))
        sqrft_data.append(sqr_footage)
        ghg_intensity = (float(school_data[i][21]))
        ghg_intesity_data.append(ghg_intensity)
    except:
        print(data[i][2], "has no data")

plt.scatter(sqrft_data, ghg_data, s=2, color="lightgreen")
plt.xlabel("Square Footage")
plt.ylabel("Greenhouse Gas Emissions (In Tons C02)")
plt.title("Greenhouse Gas Efficiency in Chicago Schools")

for i in range(len(school_data)):
    if i < 5 or i > (len(school_data) - 6) or school_data[i][2] == "Francis W Parker School":
        plt.annotate(school_data[i][2] + ": GHG Intensity = " + school_data[i][21], xy=(sqrft_data[i], ghg_data[i]))  # text, xy = (x, y)
        print(school_data[i][2])

m, b = np.polyfit(sqrft_data, ghg_data, 1)
x = [0, 1600000]
y = [m * point + b for point in x]
plt.plot(x, y, color="green")

plt.show()

'''
Challenge (for fun):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''