import math
import geopy.distance
import numpy as np
import matplotlib.pyplot as plt

import magnetic_func.magnetic_func as mag_func

def main():
    # fileName = 'Neo vbipMap.txt'
    # fileName = '美麗華 vbipMap.txt'
    fileName = 'vbipMap_1_3.txt'
    # mag_func.one_map_visualize(fileName)

    fileNameList = []
    fileNameList.append('vbipMap_1_1.txt')
    fileNameList.append('vbipMap_1_2.txt')
    fileNameList.append('vbipMap_1_3.txt')
    fileNameList.append('vbipMap_2_1.txt')
    fileNameList.append('vbipMap_2_2.txt')
    fileNameList.append('vbipMap_2_3.txt')
    
    mag_func.multi_map_visualize(fileNameList)
    
    
if __name__ == "__main__":
    main()