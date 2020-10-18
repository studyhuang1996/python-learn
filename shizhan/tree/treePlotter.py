
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

createPlot()
    

