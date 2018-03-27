import matplotlib.pyplot as plt
import csv

# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Computer Usage (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.
plt.figure("Public Library Usage", tight_layout=True, figsize=(9, 7), facecolor="lightblue")

with open("files/Libraries_-_2017_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
month_names = data.pop(0)
month_names = month_names[1:]
print(month_names)
library_names = [x[0] for x in data]
print(library_names)
print(data)
visit_num_list = []
jan_vists = [int(x[1]) for x in data]
visit_num_list.append(sum(jan_vists))
feb_vists = [int(x[2]) for x in data]
visit_num_list.append(sum(feb_vists))
mar_vists = [int(x[3]) for x in data]
visit_num_list.append(sum(mar_vists))
apr_vists = [int(x[4]) for x in data]
visit_num_list.append(sum(apr_vists))
may_vists = [int(x[5]) for x in data]
visit_num_list.append(sum(may_vists))
jun_vists = [int(x[6]) for x in data]
visit_num_list.append(sum(jun_vists))
jul_vists = [int(x[7]) for x in data]
visit_num_list.append(sum(jul_vists))
aug_vists = [int(x[8]) for x in data]
visit_num_list.append(sum(aug_vists))
sep_vists = [int(x[9]) for x in data]
visit_num_list.append(sum(sep_vists))
oct_vists = [int(x[10]) for x in data]
visit_num_list.append(sum(oct_vists))
nov_vists = [int(x[11]) for x in data]
visit_num_list.append(sum(nov_vists))
dec_vists = [int(x[12]) for x in data]
visit_num_list.append(sum(dec_vists))
print(visit_num_list)

plt.bar([x for x in range(12)], visit_num_list, color='lightblue')
plt.title("Chicago Library Usage - 2017")
plt.ylabel("Number of Visitors")
plt.xticks([x for x in range(12)], month_names, rotation=45, fontsize=8)


# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.
plt.figure("Public Transportation Usage", tight_layout=True, figsize=(9, 7), facecolor="lightblue")

with open("files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)
label_list = data.pop(0)
year_list = [int(x[0]) for x in data]
year_numbers = [x for x in range(len(year_list))]
# print(year_numbers)
# print(year_list)
bus_list = [int(x[1]) for x in data]
# print(bus_list)
paratransit_list = [int(x[2]) for x in data]
rail_list = [int(x[3]) for x in data]
# print(rail_list)
totals_list = [int(x[4]) for x in data]
print(rail_list)

plt.plot(year_numbers, bus_list, label="Bus Travel")
plt.plot(year_numbers, paratransit_list, label="Paratransit Travel")
plt.plot(year_numbers, rail_list, label="Railway Travel")
plt.plot(year_numbers, totals_list, label="Travel Totals")
plt.ylabel("Number of Uses (in Hundreds of Millions)")
plt.xticks(year_numbers, year_list, rotation=90)
plt.legend(bbox_to_anchor=(.95, .3), loc="upper right")

plt.show()
