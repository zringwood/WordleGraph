#This Class is used to draw graphs to a window.
#It is noninteractive and draws the graphs by laying out each node in a circle.
from graphics import *
from math import pi, sqrt, sin, cos, inf, floor
#TODO delete this it's only here for testing
import random
labels = "abcdefghijklmnopqrstuvwxyz"
class GraphWindow(GraphWin):
    def __init__(self):
        super().__init__("Graph Display", 600,600,False)
        #Center of the canvas treated as 0,0
        self.setCoords(-250, -250, 250, 250)
        #Graphs are drawn in a circle, this is the distance to the midpoint.
        self.radius = 200.0
      
    #Returns a point object with cartesian versions of the given polar coords
    def convertToCartesian(self,radius,theta) :
        return Point(radius * cos(theta), radius * sin(theta))
    #Draws a graph with the nodes labelled according to the given list.
    #Needs the average weight of the graph's edges. 
    def drawLabelledWeightedGraph(self, graph, labels,avgWeight) :
        #Center of the canvas treated as 0,0
        self.setCoords(-250, -250, 250, 250)
        index = 0
        for vertex in graph :
            #Calling this a couple times so we save it here
            currVertexCenter = self.convertToCartesian(self.radius,2*pi/len(graph)*index) 
            edgeIndex = 0
            for edge in vertex :
                if edge>0 :
                    endpoint = self.convertToCartesian(self.radius,2*pi/len(graph)*edgeIndex)
                    edgeGraphic = Line(currVertexCenter,endpoint)
                    #determines whether or not we need a loop
                    if endpoint.getX() == currVertexCenter.getX() and endpoint.getY() == currVertexCenter.getY() :
                        edgeGraphic = Circle(self.convertToCartesian(self.radius + 15,2*pi/len(graph)*index) ,20)
                    #Divides the value by the average to get propotional widths
                    if edge != inf :
                        edgeGraphic.setWidth((int)(edge/avgWeight))
                        edgeGraphic.draw(self)
                        
                    
                    
                edgeIndex += 1
            index+=1
        #We draw the vertices and edges seperately so that the edges are always below the vertices.
        index = 0
        for vertex in graph:
            currVertexCenter = self.convertToCartesian(self.radius,2*pi/len(graph)*index) 
            vertexCircle = Circle(currVertexCenter,10)
            vertexCircle.setFill("white")
            vertexCircle.draw(self)
            if len(labels) > 0 :
                label = Text(currVertexCenter,labels[index])
                label.setFill("black")
                label.draw(self)
            index+=1
    def drawWeightedGraph(self,graph,avgWeight):
        self.drawLabelledWeightedGraph(graph,[],avgWeight)
    #Draws a graph with the nodes labelled according to the given list.
    def drawLabelledGraph(self, graph, labels) :
        self.drawLabelledWeightedGraph(graph,labels,1)
    #Draws a graph such that each node is laid out on a circle
    def drawGraph(self, graph):
        self.drawLabelledGraph(graph,[])
    #Draws a graph such that each set of given length is drawn on a seperate horizontal portion of the screen
    #Doesn't support loops
    def drawLevelledLabelledGraph(self,graph,levellength,labels):
        #Need the lower left of the window to be 0, 0
        self.setCoords(0, 0, 600, 600)
        numLevels = len(graph)/levellength
        levelSeparation = self.height/numLevels
        for i in range(len(graph)):
            currVertexCenter = Point(10 + (self.width/levellength)*(i%levellength),levelSeparation/2 + levelSeparation*floor(i/levellength))
            for j in range(len(graph[i])): 
                #Draw the edges
                endpoint = Point(10 + (self.width/levellength)*(j%levellength),levelSeparation/2 + levelSeparation*floor(j/levellength))
                edgeGraphic = Line(currVertexCenter,endpoint)
                edgeGraphic.setWidth(1)
                edgeGraphic.draw(self)
            #Draw the vertex
            vertexCircle = Circle(currVertexCenter,10)
            vertexCircle.setFill("white")
            vertexCircle.draw(self)
            #draws labels if applicable
            if len(labels) > 0 :
                label = Text(currVertexCenter,labels[i])
                label.setFill("black")
                label.draw(self)
    #Draws a graph such that each set of given length is drawn on a seperate horizontal portion of the screen
    #Doesn't support loops
    def drawLevelledGraph(self,graph,levellength):
        self.drawLevelledLabelledGraph(graph,levellength,[])
    
            
        
#TODO: temp code for testing remember to delete
def makeRandomGraph(size):
    graph = []
    count = 0
    while count < size :
        node = []
        count2 = 0
        while count2 < size :
            edge = random.randint(1,10)
            if random.random() > 1 :
                edge = 0
                
            node.append(edge)
            
            count2+=1
        graph.append(node)
        count+=1
    return graph

