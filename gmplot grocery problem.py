from gmplot import *
import csv

# Grocery Plot Problems
# In 2013, an interesting dataset was released for Chicago which identified a number of food deserts.
# In many areas of the city, there were no suitable grocery stores with adequate produce, meats, refrigerated, and frozen food sections
# Many areas were only served by corner stores and convenience stores.
# Using gmplot and the chicago grocery csv, which contains updated grocery store data, 
# create a map with the following characteristics.
# - Map is centered on Chicago at a zoom level that shows all stores (5pts)
# - All adequate grocery stores are plotted (could be scatterplot, circles, or markers) (use the one looks best to you) (10pts)
#   Inadequate grocery stores are NOT plotted (you decide what inadequate means)
# - Shows a heatmap which helps to visualize the greatest concentration of adequate stores. (10pts) 
#   Your heatmap should be optimized for the city level view.  Tweak the radius and maxIntensity to adjust blob.
apikey = "AIzaSyAOJfeSJJr64yL2UPNwf9C8TDe3UE9qnEA"
mymap = GoogleMapPlotter(41.876190, -87.629686, 11, apikey=apikey)

with open("files/Map_of_Grocery_Stores_-_2013.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)

index = -1
while index < len(data) - 1:
    index += 1
    if "WALGREEN" in data[index][0].upper() or "LIQUOR" in data[index][0].upper() or "SAVE-A_LOT" in data[index][0].upper() or "SEVEN ELEVEN" in data[index][0].upper() or "DOLLAR" in data[index][0].upper() or "DRUG" in data[index][0].upper() or "CONVENIENCE" in data[index][0].upper():
        data.pop(index)

for i in range(len(data)): print(data[i][0].upper())
lats = []
longs = []
for i in range(len(data)):
    lats.append(float(data[i][-3]))
    longs.append(float(data[i][-2]))

mymap.heatmap(lats, longs, maxIntensity=3, radius=22, dissipating=True)
mymap.scatter(lats, longs, color="green", marker=False, size=100)

mymap.draw("mymap.html")

# Challenges:  
# Instead of a heatmap, make each store a circle with varying size based on square footage of the store.  
# Filter out all liquor stores, drug stores, and convenience stores.
# Place markers or other indicators where you still see inadequate food access.
