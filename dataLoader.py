import sys
import pandas as pd
import numpy as np

#---Converting the dataset from csv to txt------------------------------------#
def csvToTxt(csvfile):
    df = pd.read_excel(csvfile, index_col=None)
    size = len(df)

    data = np.array([
        (df['Local_Name'][i] + "," +
        df['English_Name'][i].lower()) 
    for i in range(size)
    if (u'\u0949' not in df['Local_Name'][i] 
    and u'\u0945' not in df['Local_Name'][i]
    and u'\u0946' not in df['Local_Name'][i]
    and u'\u094a' not in df['Local_Name'][i])])

    print("Size of dataset:",len(data))
    print("One entry in dataset:", data[0])

    with open('dataset.txt', 'w', encoding='utf-8') as d:
        [d.write(dt.split(",")[0] + " " + dt.split(",")[1] + "\n") for dt in data]
    return data
#-----------------------------------------------------------------------------#

#---Splitting data into Train/Test--------------------------------------------#
def splitData(data,trainSize = 80):

    size = len(data)
    splitSize = int(size * trainSize / 100)

    np.random.shuffle(data)
    print("Data splitted into: Train:",trainSize,  " Test:", 100-trainSize)

    trainData = data[:splitSize]
    testData = data[splitSize:]

    trainSize = len(trainData)
    testSize = len(testData)

    valSize = int(trainSize * 15 / 100)

    valData = trainData[:valSize]
    trainData = trainData[valSize:]

    trainSize = len(trainData)
    valSize = len(valData)

    print("Size of training data:",trainSize)
    print("Size of validation data:", valSize)
    print("Size of test data:",testSize)

    return trainData, valData, testData
#-----------------------------------------------------------------------------#

#--------Splits a txt file into train/test------------------------------------#
def splitTxt(filename, trainSize=80):

    f = open(filename, 'r', encoding='utf-8')

    data = [[d.split(" ")[0], d.split(" ")[1]] for d in f.readlines()]

    size = len(data)
    splitSize = int(size * trainSize / 100)

    np.random.shuffle(data)
    print("Data splitted into: Train:",trainSize,  " Test:", 100-trainSize)

    trainData = data[:splitSize]
    testData = data[splitSize:]

    trainSize = len(trainData)
    testSize = len(testData)

    valSize = int(trainSize * 15 / 100)

    valData = trainData[:valSize]
    trainData = trainData[valSize:]

    trainSize = len(trainData)
    valSize = len(valData)

    print("Size of training data:",trainSize)
    print("Size of validation data:", valSize)
    print("Size of test data:",testSize)

    with open("train.txt", 'w', encoding='utf-8') as train:
        for d in trainData:
            train.write(d[0] + " " + d[1])

    with open("test.txt", 'w', encoding='utf-8') as test:
        for d in testData:
            test.write(d[0] + " " + d[1])

    with open("val.txt", 'w', encoding='utf-8') as val:
        for d in valData:
            val.write(d[0] + " " + d[1])

#-----------------------------------------------------------------------------#

#-------------Loads data from a txt file--------------------------------------#
def loadTxt(filename):

    f = open(filename, 'r', encoding='utf-8')

    data = np.array([
        (d.split(" ")[0] + "," + d.split(" ")[1].strip("\n"))
        for d in f 
    ])

    print("Size of dataset:",len(data))
    print("One entry in dataset:", data[0])

    return data
#-----------------------------------------------------------------------------#



