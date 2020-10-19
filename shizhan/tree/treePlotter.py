'''
Author: your name
Date: 2020-10-18 15:23:56
LastEditTime: 2020-10-19 23:45:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python/shizhan/tree/treePlotter.py
'''

import matplotlib.pyplot as pyplot

#定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
allow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeTyoe):
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',
                            xytext=centerPt,textcoords='axes fraction',
                            va="center",ha="center",bbox=nodeTyoe,arrowprops=allow_args)


def createPlot():
    fig = pyplot.figure(1,facecolor='white')
    fig.clf()
    createPlot.ax1 = pyplot.subplot(111,frameon=False)
    plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('叶节点',(0.8,0.1),(0.3,0.5),leafNode)
    pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS'] #解决中文乱码
    pyplot.show()

# createPlot()
    

'''
获取叶子节点的数目: 
param {type} 
return {type} 
'''
def getNumLeafs(myTree):
    numLeafs=0
    #得到根节点
    firstStr = list(myTree.keys())[0]
    #子节点集
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        #如果子集是字典类型，则还有子节点
        if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs +=1
    return numLeafs

def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth = 1+ getTreeDepth(secondDict[key])
        else:
            thisDepth =1
        if thisDepth > maxDepth : maxDepth = thisDepth
    return maxDepth


mydata = {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

# getNumLeafs(mydata)
# print(getTreeDepth(mydata))

def plotMidText(currentPr,parentPt,txtStr):
    xMid =(parentPt[0]-currentPr[0])/2.0 + currentPr[0]
    yMid =(parentPt[1]-currentPr[1])/2.0 + currentPr[1]
    createPlot.ax1.text(xMid,yMid,txtStr)

'''
description: 
param {type} 
return {type} 
'''
def plotTree(myTree,parentPt,nodeTxt):
    numLeafs =getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0+float(numLeafs))/2.0/plotTree.totalW, 1.00)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff -1.0/plotTree.totalW
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff =  plotTree.yOff + 1.0/ plotTree.totalD

def createPlotTree(inTree):
    fig = pyplot.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = pyplot.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;plotTree.vOff =5
    plotTree(inTree,(0.5,1.0),'')
    pyplot.rcParams['font.sans-serif'] = ['Arial Unicode MS'] #解决中文乱码
    pyplot.show()    


createPlotTree(mydata)