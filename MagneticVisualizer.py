import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

import magnetic_func.magnetic_func as mag_func

def main():
    # fileName = 'Neo vbipMap.txt'
    # fileName = '美麗華 vbipMap.txt'
    # fileName = 'vbipMap_1_3.txt'
    # fileName = 'map/att_2_2 vbipMap 拷貝.txt'
    # mag_func.one_map_visualize(fileName)

    fileNameList = []
    fileNameList.append('map/att_1_1 vbipMap 拷貝.txt')
    fileNameList.append('map/att_2_2 vbipMap 拷貝.txt')
    fileNameList.append('map/att_2_3 vbipMap 拷貝.txt')
    fileNameList.append('map/att_3_2 vbipMap 拷貝.txt')
    fileNameList.append('map/att_3_3 vbipMap 拷貝.txt')
    
    # mag_func.multi_map_visualize(fileNameList)
    # mag_func.multi_map_difference_visualize(fileNameList)
    mag_func.multi_map_difference_curve_visualize(fileNameList)
    
if __name__ == "__main__":
    main()