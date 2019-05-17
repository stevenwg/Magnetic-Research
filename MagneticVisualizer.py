import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

import magnetic_func.magnetic_func as mag_func

def main():

# ---------------- GPStoKM ----------------
    # fileName = 'vbipMap.txt'
    # GPS_data, Mag_data = mag_func.magnectic_read(fileName)
    # KM_data = mag_func.GPStoKM(GPS_data)*1000
    # fo = open("test.txt", "w")
    # for i in range(len(KM_data)):
    #     fo.write(str(KM_data[i]) + "\n")
    # fo.close()

# ---------------- One Map ----------------
    # fileName = 'Neo vbipMap.txt'
    # fileName = '美麗華 vbipMap.txt'
    # fileName = 'vbipMap_1_3.txt'
    # fileName = 'map/att_2_2 vbipMap 拷貝.txt'
    fileName = 'map/vbipMap2 MRT.txt'
    mag_func.one_map_visualize(fileName)

# ---------------- Multi Map ----------------
    # fileNameList = []
    # fileNameList.append('map/att_1_1 vbipMap 拷貝.txt')
    # fileNameList.append('map/att_2_2 vbipMap 拷貝.txt')
    # fileNameList.append('map/att_2_3 vbipMap 拷貝.txt')
    # fileNameList.append('map/att_3_2 vbipMap 拷貝.txt')
    # fileNameList.append('map/att_3_3 vbipMap 拷貝.txt')
    
    # # mag_func.multi_map_visualize(fileNameList)
    # # mag_func.multi_map_difference_visualize(fileNameList)
    # mag_func.multi_map_difference_curve_visualize(fileNameList)
    
if __name__ == "__main__":
    main()