
import pandas as pd
import numpy as np
import csv


def CsvProcess(csvPath):
    dataArray = pd.read_csv(csvPath)
    dataArray = np.array(dataArray)
    pageTotal = dataArray[len(dataArray)-1][1]
    print(pageTotal)

    dataList=[]
    for i in range(0,len(dataArray) ):
        df1 = dataArray[i]





if __name__ == "__main__":
    csvPathArray = [
        "./CFApdf/2019 CFA Curriculum Level I Volume 1.csv",
        "./CFApdf/2019 CFA Curriculum Level I Volume 2.csv",
        "./CFApdf/2019 CFA Curriculum Level I Volume 3.csv",
        "./CFApdf/CFA Program Curriculum Level I Vol 4.csv",
        "./CFApdf/CFA Program Curriculum Level I Vol 5.csv",
        "./CFApdf/CFA Program Curriculum Level I Vol 6.csv"
    ]

    CsvProcess( csvPathArray[0] )
