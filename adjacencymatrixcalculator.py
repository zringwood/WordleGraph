#Writes an adjacency matrix for the following graph:
#Each Vertex represents a letter of the alphabet in a particular place in a wordle guess
#Verticies share an edge IFF the letters they represent are in the same word.
legalguesses = open("wordlelegalguesses.txt", "r")

graph = [[0] * (26*5) for i in range(26*5)]

#For every legal guess in the file, we want to add one edge for letter in the word
nextword = legalguesses.readline()
while nextword != "" :
    for i in range(len(nextword)-1):
        for j in range(len(nextword)-1):
            if i != j : 
                graph[ord(nextword[i]) - ord('a') + i*26][ord(nextword[j]) - ord('a') + j*26] += 1
    nextword = legalguesses.readline()
#Writes the graph to a string
graphstring = "["
for vertex in graph :
    graphstring += "{},\n".format(vertex)
#There's an extra comma on the end of the string, this cuts it off
graphstring = graphstring[:len(graphstring)-2]
graphstring += "]"
guessesgraph = open("guessesgraph.txt","w")
guessesgraph.write(graphstring)
guessesgraph.close()

