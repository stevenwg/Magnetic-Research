import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

def magnectic_read(fileName):
    fr = open(fileName, 'r')
    latitude_list = []
    longitude_list = []
    MagX_list = []
    MagY_list = []
    MagZ_list = []
    line = fr.readline()
    while line:
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
    fr.close()
    GPS_data = np.column_stack((latitude_list, longitude_list))
    Mag_data = np.column_stack((MagX_list, MagY_list, MagZ_list))
    return [GPS_data, Mag_data]


def GPStoKM(GPS_data):
    distance = []
    latitude = GPS_data[0, 0]
    longitude = GPS_data[0, 1]
    for idx in range(len(GPS_data)):
        latitude_new = GPS_data[idx, 0]
        longitude_new = GPS_data[idx, 1]
        coords_1 = (latitude_new,longitude_new)
        coords_2 = (latitude, longitude)
        result = geopy.distance.distance(coords_1, coords_2).km
        distance.append(result)
        latitude = latitude_new
        longitude = longitude_new
    distance.remove(0) # remove the first distance
    return np.array(distance)


def one_map_visualize(fileName):
    GPS_data, Mag_data = magnectic_read(fileName)
    # print(GPStoKM(GPS_data)*1000)
    Mag_data_max = Mag_data.max(axis=0)
    Mag_data_min = Mag_data.min(axis=0)
    Mag_color_list = (Mag_data - Mag_data_min) / (Mag_data_max - Mag_data_min)
    plt.figure(1)
    for idx in range(len(GPS_data)):
        ax = plt.subplot(221)
        ax.set_title("MagX")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,0], Mag_color_list[idx,0], Mag_color_list[idx,0])), markersize = 2)
        ax.grid(True)
        # ax.set_xlim([25.030, 25.052])
        ax = plt.subplot(222)
        ax.set_title("MagY")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,1], Mag_color_list[idx,1], Mag_color_list[idx,1])), markersize = 2)
        ax.grid(True)
        # ax.set_xlim([25.030, 25.052])
        ax = plt.subplot(223)
        ax.set_title("MagZ")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,2], Mag_color_list[idx,2], Mag_color_list[idx,2])), markersize = 2)
        ax.grid(True)
        # ax.set_xlim([25.030, 25.052])
        ax = plt.subplot(224)
        ax.set_title("Mag")
        ax.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple(Mag_color_list[idx,:]), markersize = 2)
        ax.grid(True)
        # ax.set_xlim([25.030, 25.052])
        # l = plt.plot(GPS_data[idx,0], GPS_data[idx,1], 'o', color = tuple((Mag_color_list[idx,0], 0, Mag_color_list[idx,2])), markersize = 5)
    ax.plot(GPS_data[1000,0], GPS_data[1000,1], 'o', color = (0,0,0), markersize = 5)
    plt.show()
    return


def multi_map_visualize(fileName_list):
    GPS_data_list = []
    Mag_data_list = []
    Mag_data_max_all = []
    Mag_data_min_all = []
    plt.figure(1)
    for idx in range(len(fileName_list)):
        GPS_data, Mag_data = magnectic_read(fileName_list[idx])
        GPS_data_list.append(GPS_data)
        Mag_data_list.append(Mag_data)

        Mag_data_max = Mag_data.max(axis=0)
        Mag_data_min = Mag_data.min(axis=0)
    #     Mag_data_max_all = np.hstack((Mag_data_max_all, Mag_data_max))
    #     Mag_data_min_all = np.hstack((Mag_data_min_all, Mag_data_min))
    #     print('fileName: ' + fileName_list[idx] + ', Mag_data_max: ' + str(Mag_data_max) + ', Mag_data_min: ' + str(Mag_data_min))
        Mag_color_list = (Mag_data - Mag_data_min) / (Mag_data_max - Mag_data_min)
        # ax = plt.subplot(int(str(1)+str(len(fileName_list))+str(idx+1)))
        ax = plt.subplot(int(str(len(fileName_list))+str(1)+str(idx+1)))
        ax.set_title(fileName_list[idx])
        for dot_idx in range(len(GPS_data)):
            if (dot_idx > (len(GPS_data)-300)):
                ax.plot(GPS_data[dot_idx,0], GPS_data[dot_idx,1], 
                'o', color = tuple((Mag_color_list[dot_idx,0], Mag_color_list[dot_idx,1], Mag_color_list[dot_idx,2])), markersize = 5)
        ax.grid(True)
        # 
        # ax.set_xlim([25.030, 25.052])
        # ax.set_ylim([-121.557, -121.5545])

        ax.set_xlim([25.081, 25.0822])
        ax.set_ylim([-121.5553, -121.5557])
    
    # print('Mag_data_max_all: ' + str(Mag_data_max_all) + ', Mag_data_min_all: ' + str(Mag_data_min_all))
    plt.show()
    return

def multi_map_difference_visualize(fileName_list):
    GPS_data_diff_list = []
    Mag_data_diff_list = []
    Mag_data_max_all = []
    Mag_data_min_all = []
    plt.figure(1)
    for idx in range(len(fileName_list)):
        GPS_data, Mag_data = magnectic_read(fileName_list[idx])
        # Calculate difference values of map
        GPS_data_diff = np.delete(GPS_data, 0, 0)
        Mag_data_diff = Mag_data[1:,:] - Mag_data[0:-1]
        GPS_data_diff_list.append(GPS_data_diff)
        Mag_data_diff_list.append(Mag_data_diff)

    Mag_data_diff_max = np.concatenate(Mag_data_diff_list, axis=0).max(axis=0)
    Mag_data_diff_min = np.concatenate(Mag_data_diff_list, axis=0).min(axis=0)
    
    for idx in range(len(fileName_list)):
        Mag_color_diff_list = (Mag_data_diff_list[idx] - Mag_data_diff_min) / (Mag_data_diff_max - Mag_data_diff_min)
        ax = plt.subplot(int(str(len(fileName_list))+str(1)+str(idx+1)))
        ax.set_title(fileName_list[idx])
        for dot_idx in range(len(GPS_data_diff_list[idx])):
            if (dot_idx > (len(GPS_data_diff_list[idx])-300)):
                ax.plot(GPS_data_diff_list[idx][dot_idx,0], GPS_data_diff_list[idx][dot_idx,1], 
                'o', color = tuple((Mag_color_diff_list[dot_idx,0], Mag_color_diff_list[dot_idx,0], Mag_color_diff_list[dot_idx,0])), markersize = 5)
                ax.grid(True)
                ax.set_xlim([25.0811, 25.0821])
                ax.set_ylim([-121.5553, -121.5557])
    
    # print('Mag_data_max_all: ' + str(Mag_data_max_all) + ', Mag_data_min_all: ' + str(Mag_data_min_all))
    plt.show()
    return