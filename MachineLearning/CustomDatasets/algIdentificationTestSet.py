def sort(numbers):
	sortedFlag = False
	while sortedFlag == False:
		sortedFlag = True
		for i in range(len(numbers)-1):
			if numbers[i] > numbers[i+1]:
				temp = numbers[i+1]
				numbers[i+1] = numbers[i]
				numbers[i] = temp
				sortedFlag = False
	return numbers

def computeDotP(x,y):
	return x.i * y.i + x.j * y.j

def binS(l,s,e,targ):
	if (s > e):
		return False
	mid = (s+e)//2
	if l[mid] == targ:
		return True
	elif l[mid] > targ:
		return binS(l,s,mid-1,targ)
	else:
		return binS(l,mid+1,e,targ)

def trav(graph, currentNode, vis):
	vis.append(currentNode)
	for v in graph[currentNode]:
		if not(v in vis):
			trav(graph,v,vis)
	return vis

def dfs(graph, currentNode, visited):
	visited.append(currentNode)
	for v in graph[currentNode]:
		if not(v in visited):
			dfs(graph,v,visited)
	return visited

def linearS(listOfVals,searchFor):
	for val in listOfVals:
		if val == searchFor:
			return True
	return False
