from graphrenderingwindow import *
from math import inf
from random import randint
import re
#This graph represents the frequency of one letter appearing with another letter in the possible wordle answers.
#Two nodes share an edge for each time their letters appear in a word together.
#The letter of a node is determined by its place in the array, A = 0, B = 1, etc.
wordleGraph = [[1208,627,673,811,1529,314,623,615,958,146,590,1246,821,1122,777,734,44,1552,2445,1088,591,275,389,93,570,203],
[627,196,113,177,571,58,109,82,332,32,113,258,153,191,510,35,5,367,600,194,315,19,50,17,220,40],
[673,113,162,189,589,69,63,317,453,11,188,287,156,229,601,159,3,389,659,265,288,43,48,21,200,29],
[811,177,189,274,1330,103,153,152,577,34,140,344,186,359,689,173,9,506,794,224,368,87,162,51,301,47],
[1529,571,589,1330,1628,383,540,518,1053,118,520,1227,758,1054,1078,715,23,1801,2668,1139,553,421,448,214,622,216],
[314,58,69,103,383,216,69,54,261,12,53,202,53,103,248,28,9,246,457,170,203,13,45,18,130,23],
[623,109,63,153,540,69,184,124,354,26,52,270,131,336,467,118,3,359,570,162,276,35,53,4,227,24],
[615,82,317,152,518,54,124,84,333,21,122,240,163,182,461,142,4,252,679,342,232,34,123,12,169,27],
[958,332,453,577,1053,261,354,333,294,67,382,769,494,779,537,421,39,847,1531,734,274,214,175,91,242,141],
[146,32,11,34,118,12,26,21,67,4,29,42,28,53,96,25,2,41,120,27,70,9,11,1,29,2],
[590,113,188,140,520,53,52,122,382,29,106,203,95,251,408,136,3,299,780,161,229,18,74,2,206,20],
[1246,258,287,344,1227,202,270,240,769,42,203,386,300,284,860,335,5,374,1284,398,488,139,166,54,398,49],
[821,153,156,186,758,53,131,163,494,28,95,300,186,222,554,159,5,365,805,233,362,28,55,38,243,47],
[1122,191,229,359,1054,103,336,182,779,53,251,284,222,288,794,229,17,416,1018,451,427,90,178,39,332,64],
[777,510,601,689,1078,248,467,461,537,96,408,860,554,794,896,590,15,967,1874,806,375,132,284,74,489,154],
[734,35,159,173,715,28,118,142,421,25,136,335,159,229,590,236,6,396,883,299,318,29,73,19,316,34],
[44,5,3,9,23,9,3,4,39,2,3,5,5,17,15,6,2,11,32,16,70,0,2,0,6,1],
[1552,367,389,506,1801,246,359,252,847,41,299,374,365,416,967,396,11,376,1416,635,587,138,166,46,413,71],
[2445,600,659,794,2668,457,570,679,1531,120,780,1284,805,1018,1874,883,32,1416,1376,1395,1132,210,493,88,564,111],
[1088,194,265,224,1139,170,162,342,734,27,161,398,233,451,806,299,16,635,1395,414,456,55,168,37,343,52],
[591,315,288,368,553,203,276,232,274,70,229,488,362,427,375,318,70,587,1132,456,134,50,37,30,253,58],
[275,19,43,87,421,13,35,34,214,9,18,139,28,90,132,29,0,138,210,55,50,32,20,9,57,7],
[389,50,48,162,448,45,53,123,175,11,74,166,55,178,284,73,2,166,493,168,37,20,20,10,107,19],
[93,17,21,51,214,18,4,12,91,1,2,54,38,39,74,19,0,46,88,37,30,9,10,2,32,2],
[570,220,200,301,622,130,227,169,242,29,206,398,243,332,489,316,6,413,564,343,253,57,107,32,70,57],
[203,40,29,47,216,23,24,27,141,2,20,49,47,64,154,34,1,71,111,52,58,7,19,2,57,78]]
labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#We want to compute a minimal spanning tree and analyze clustering behaviour for the graph.



#Helper method for isPath. This takes a list of nodes and confirms whether we've visited the current v1 efore, breaking loops.
def _isPath(visitedNodes, adjMatrix, v1, v2) :
    if v1 == v2 :
        return True
    #Testing for each edge of the vertex v1
    for i in range(len(adjMatrix[v1])) :
        if adjMatrix[v1][i] > 0 and visitedNodes.count(i) == 0:
            if _isPath(list(visitedNodes + [i]),adjMatrix, i, v2):
                return True
    return False

#Helper Method, returns True if a path exists between the two verticies. Needs to be passed two indices indicating the vertices' places in the given adjacency matrix
#Uses a depth-first search.
#This method does NOT detect the presense of a loop. It treats two equal indices as a trivial path. 
def isPath(adjMatrix, v1, v2):
    #Path consisting of one vertex
    if v1 == v2 :
        return True
    #Testing for each edge of the vertex v1
    for i in range(len(adjMatrix[v1])) :
        if adjMatrix[v1][i] > 0 :
             if _isPath([v1],adjMatrix, i, v2):
                 return True
    return False

#Start with a minimal spanning tree.
#Kruskal's Algorithm
def minimalspanningtree(graph) :
    graphCopy = []
    #Having the graph in a one dimensional array makes for easier searching.
    for vertex in graph:
        graphCopy = graphCopy + vertex
    #Eliminating empty edges
    i = 0
    while i < len(graphCopy) :
       if graphCopy[i] == 0 :
           graphCopy[i] = inf
       i+=1
    #Initialize an empty list of edges. All values initially 0.
    #They don't need to be infinite because we get the minimum value from the graphCopy and add it without comparing to the stored values in the tree.
    minimalTree = [[0] * len(graph) for i in range(len(graph))]

    i=0
    while i < len(graphCopy) :
        lowest = min(graphCopy)
        index = graphCopy.index(lowest)
        #print(lowest)
        #Here we check and see if the edge connects two trees. If there's no path between the endpoints of a potential edge then we can connect it.
        if not isPath(minimalTree, int(index/len(graph)), int(index%len(graph))) :
            minimalTree[int(index/len(graph))][int(index%len(graph))] = lowest
            minimalTree[int(index%len(graph))][int(index/len(graph))] = lowest
        #Either way, we never want to deal with this edge again. 
        graphCopy[index] = inf
        i+=1

    return minimalTree
    #Bugtesting Methods
def getRandomSimpleGraph(graphsize, probability) :
    graph = [[0] * graphsize for i in range(graphsize)]
    for i in range(graphsize) :
        for j in range(graphsize) :
            if randint(0,100) < probability :
                graph[i][j] = 1
        graph[i][i] = 0
    return graph
def getRandomWeightedGraph(graphsize,probability,minWeight,maxWeight) :
    graph = [[0] * graphsize for i in range(graphsize)]
    for i in range(graphsize) :
        for j in range(graphsize) :
            if randint(0,100) < probability :
                graph[i][j] = randint(minWeight,maxWeight)
        graph[i][i] = 0
    return graph

graphfile = open("guessesgraph.txt","r")
wordleGraph = [[0] * 26*5 for i in range(26*5)]
for line in wordleGraph :
    nextline = graphfile.readline().split(",")
    for cell in range(len(line)) :
        line[cell] = int(re.sub("[\[,\] ]","",nextline[cell]))

window = GraphWindow()
window.drawLevelledLabelledGraph(wordleGraph, 26,labels)
window0 = GraphWindow()
window0.drawLevelledLabelledGraph(minimalspanningtree(wordleGraph), 26, labels)


