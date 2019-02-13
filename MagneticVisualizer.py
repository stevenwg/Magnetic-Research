import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

def main():
    fr = open('Neo vbipMap.txt', 'r')
    # fr = open('美麗華 vbipMap.txt', 'r')

    latitude_list = []
    longitude_list = []
    MagX_list = []
    MagY_list = []
    MagZ_list = []

    line = fr.readline()
    idx = 0
    for word in line.split():
        if idx == 2:
            latitude = float(word)
            latitude_list.append(latitude)
        elif idx == 5:
            longitude = float(word)
            longitude_list.append(longitude*(-1))
        elif idx == 8:
            MagX = float(word)
            MagX_list.append(MagX)
        elif idx == 11:
            MagY = float(word)
            MagY_list.append(MagY)
        elif idx == 14:
            MagZ = float(word)
            MagZ_list.append(MagZ)
        idx += 1

    line = fr.readline()
    while line:
        idx = 0
        for word in line.split():
            if idx == 2:
                latitude_new = float(word)
                latitude_list.append(latitude_new)
            elif idx == 5:
                longitude_new = float(word)
                longitude_list.append(longitude_new*(-1))
            elif idx == 8:
                MagX = float(word)
                MagX_list.append(MagX)
            elif idx == 11:
                MagY = float(word)
                MagY_list.append(MagY)
            elif idx == 14:
                MagZ = float(word)
                MagZ_list.append(MagZ)
            idx += 1
        
        coords_1 = (latitude_new,longitude_new)
        coords_2 = (latitude, longitude)
        result = geopy.distance.distance(coords_1, coords_2).km*1000
        # print(result)
        line = fr.readline()

    fr.close()

    GPS_data = np.column_stack((latitude_list, longitude_list))
    
    Mag_data = np.column_stack((MagX_list, MagY_list, MagZ_list))
    
    Mag_data_max = Mag_data.max(axis=0)
    Mag_data_min = Mag_data.min(axis=0)

    Mag_color_list = (Mag_data - Mag_data_min) / (Mag_data_max - Mag_data_min)

    plt.figure(1)
    for idx in range(len(GPS_data)):
        ax = plt.subplot(221)
        ax.set_title("MagX")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,0], Mag_color_list[idx,0], Mag_color_list[idx,0])), markersize = 5)
        ax = plt.subplot(222)
        ax.set_title("MagY")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,1], Mag_color_list[idx,1], Mag_color_list[idx,1])), markersize = 5)
        ax = plt.subplot(223)
        ax.set_title("MagZ")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,2], Mag_color_list[idx,2], Mag_color_list[idx,2])), markersize = 5)
        ax = plt.subplot(224)
        ax.set_title("Mag")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple(Mag_color_list[idx,:]), markersize = 5)
        # l = plt.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,0], 0, Mag_color_list[idx,2])), markersize = 5)
    plt.show()

if __name__ == "__main__":
    main()