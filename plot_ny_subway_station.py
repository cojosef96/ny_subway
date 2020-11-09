import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

MAP_BOUNDRIES = (-74.0273, -73.8776, 40.6937, 40.8580)
# MAP_BOUNDRIES = (34.4910, 34.5072, 31.5857, 31.5963) # zoomed
# BBox = ((df.longitude.min(),   df.longitude.max(),      
        #  df.latitude.min(), df.latitude.max())



if __name__ == "__main__":

        # ruh_m = plt.imread('map_zoom.png') # zoom
        ruh_m = plt.imread('map_ny.png')
        df = pd.read_csv('StationEntrances.csv')

        lat = np.array(df['Station_Latitude'])
        lon = np.array(df['Station_Longitude'])

        fig, ax = plt.subplots(figsize = (5,7))
        ax.imshow(ruh_m, zorder=0, extent = MAP_BOUNDRIES, aspect= 'equal')
        ax.scatter(lon, lat, zorder=1, alpha= 1, c='b', s=10)
        ax.set_title('Plotting Spatial Data on Riyadh Map')
        ax.set_xlim(MAP_BOUNDRIES[0],MAP_BOUNDRIES[1])
        ax.set_ylim(MAP_BOUNDRIES[2],MAP_BOUNDRIES[3])
        plt.show()

        

