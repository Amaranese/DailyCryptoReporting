# ======================== Python dependencies
import os
import random
import pandas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from pylab import figure, axes, pie, title, show
import datetime
from datetime import timedelta


"""

THIS JOB READS FROM REPORTS FOLDER, EXTRACTS DATA, PRODUCES GRAPHS SAVES AS PNG TO FOLLOWING ../../../murchie85.github.io/images/crypto/gbp/

"""

# ========================  Create Array of market names from available files 

directory = "reports/"
#initialize iterators
availableMarkets = []
availableMarketsFile = []
metricArray = []
metricRow = []
coinmetricRow = []



for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        #print(os.path.join(directory, filename))
        marketName = filename[:-14]
        availableMarketsFile.append(filename)
        availableMarkets.append(marketName)
        continue
    else:
        continue

# ======================== Create populated Markets matrix


for j in range(0, len(availableMarkets)): # Iterate through files
    with open("reports/" + str(availableMarketsFile[j]), 'rU') as f:
        metricRow = []
        for line in f: # Iterate through rows
            line = line[:-1]
            words = line.split(",")
            #print(words)
            marketArray = np.asarray(words)
            metricRow.append(marketArray)
        coinmetricRow.append(np.asarray(metricRow))



# ========================  Iterate through matrix Save and Produce Graphs 


for y in range (0, len(coinmetricRow)):
    rates = []
    dates = []
    for x in range(0, len(coinmetricRow[y])):
        rates.append(float(coinmetricRow[y][x][2][1:]))
        toDatetime = datetime.datetime.strptime(coinmetricRow[y][x][0][:-3], "%Y-%m-%d %H:%M")
        dates.append(toDatetime)


    plt.clf() # clear cache
    color = ["blue","red","green","black","orange"]
    print(rates)
    fig, ax = plt.subplots()
    ax.plot(dates,rates, color=random.choice(color))
    fig.autofmt_xdate()
    myFmt = DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(myFmt)
    plt.title(str(coinmetricRow[y][0][1]) + " to £GBP", fontsize=20)
    plt.ylabel("pounds GBP")  
    
    
    
    
    plt.savefig("../../../murchie85.github.io/images/crypto/gbp/" + str(coinmetricRow[y][0][1]) + "-report.png", bbox_inches="tight")



    

