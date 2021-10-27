def dotProduct(a,b):
	return a.x * b.x + a.y * b.y

def dfs(graph, currentNode, visited):
	visited.append(currentNode)
	for v in graph[currentNode]:
		if not(v in visited):
			dfs(graph,v,visited)
	return visited

def quicksort(myList,start,end):
	if (start < end):
		pivotVal = myList[end]
		i = start - 1
		for j in range(start,end+1):
			if myList[j] <= pivotVal:
				i += 1
				myList[i],myList[j] = myList[j],myList[i]          
		split = i
		quicksort(myList,start,split-1)
		quicksort(myList,split+1,end)
		return myList


def bubbleSort(numbers):
	sortedFlag = False
	while sortedFlag == False:
		sortedFlag = True
		for i in range(len(numbers)-1):
			if numbers[i] > numbers[i+1]:
				numbers[i+1],numbers[i] = numbers[i],numbers[i+1]
				sortedFlag = False
	return numbers

def binarySearch(arr,start,end,target):
	if (start > end):
		return False
	mid = (start+end)//2
	if arr[mid] == target:
		return True
	elif arr[mid] > target:
		return binarySearch(arr,start,mid-1,target)
	else:
		return binarySearch(arr,mid+1,end,target)
