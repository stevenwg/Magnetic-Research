import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

def main():
    f = open('Neo vbipMap.txt', 'r')

    # fw = open('GPStoKM_result.txt', 'w')

    latitude_list = []
    longitude_list = []

    line = f.readline()
    idx = 0
    for word in line.split():
        if idx == 2:
            latitude = float(word)
            latitude_list.append(latitude)
        elif idx == 5:
            longitude = float(word)
            longitude_list.append(longitude*(-1))
        idx += 1

    line = f.readline()
    while line:
        idx = 0
        for word in line.split():
            if idx == 2:
                latitude_new = float(word)
                latitude_list.append(latitude_new)
            elif idx == 5:
                longitude_new = float(word)
                longitude_list.append(longitude_new*(-1))
            idx += 1
        
        coords_1 = (latitude_new,longitude_new)
        coords_2 = (latitude, longitude)
        # KM -> M
        result = geopy.distance.distance(coords_1, coords_2).km*1000
        print(result)
        # fw.write(str(result)+'\n')

        latitude = latitude_new
        longitude = longitude_new
        line = f.readline()

    f.close()
    # fw.close()

    l = plt.plot(latitude_list, longitude_list, 'ro')
    plt.setp(l, markersize = 1)
    l = plt.plot(latitude_list[274], longitude_list[274], 'bo')
    # plt.setp(l, markersize = 1)
    # plt.setp(l, markerfacecolor='C0')

    plt.show()

if __name__ == "__main__":
    main()