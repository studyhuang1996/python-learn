from math import log
import operator
'''
计算熵: 
param 数据集 二维数组 
returnt 熵 
'''
def calcShannontEnt(dataSet):
    numEntries = len(dataSet)
    labCounts={}
    for featVec in dataSet:
        currentLabel = featVec[-1]   #拿到分类目标值，yes
        if currentLabel not in labCounts.keys():
            labCounts[currentLabel] =0
        labCounts[currentLabel] += 1  #记录每个类别出现的次数
    shannonEnt = 0.0
    for key in labCounts:
        prob = float(labCounts[key])/numEntries
       # print('当前分类：%s ,所得熵值：%s' %(key,-prob * log(prob,2)))
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

'''
创建数据集: 
param {type} 
return {type} 
'''
def createDataSet():
    dataSet = [
        [1,1,'yes'],
        [1,1,'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no']
    ]
    labels =  ['no surfacing','flippers']
    return dataSet,labels
#调用计算熵
myDat,labels = createDataSet()
#print(calcShannontEnt(myDat))

'''
description: 
param dataSet 待划分的数据集
param axis 划分数据集的特征
param value 需要返回的特征的值
return {type} 
'''
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

#print(splitDataSet(myDat,0,0))

'''
选择最好的划分数据的特征: 
param {type} 
return {type} 
'''
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) -1
    baseEntropy = calcShannontEnt(dataSet)
    bestInfoGain = 0.0; bestFeature =-1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannontEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

print(chooseBestFeatureToSplit(myDat))

'''
投票表决决定叶子节点的分类: 
param {type} 
return {type} 
'''
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reversed=True)
    return sortedClassCount[0][0]
    

'''
创建树: 
param 数据集和标签列表
return {type} 
'''
def createTree(dataSet,labels):
    classList= [example[-1] for example in dataSet]
    if(classList.count(classList[0]) == len(classList)):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeature]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeature])
    featValues= [example[bestFeature] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeature,value),subLabels)
    return myTree


print(createTree(myDat,labels))