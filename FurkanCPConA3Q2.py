'''

Essential unit: P.Con.
Assignment: A3
Question: Q#2
Name: Furkan Canturk
Pseudoname: FC
Date:
Teacher&Class: ICS3UI-01 for Ms. Harris
Modification:
Question:
Acknowledgements:
Sample Run:

'''


def insertionSort(alist):
     for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

    while position > 0 and alist[position - 1] > currentvalue:
        alist[position] = alist[position - 1]
        position = position - 1

            alist[position] = currentvalue

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)




def bubbleSort(alist):
     for passnum in range(len(nlist) - 1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i + 1]:
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)



def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
            return qsort([x for x in arr[1:] if x < arr[0]]) + \
                   [arr[0]] + \
                   qsort([x for x in arr[1:] if x >= arr[0]])

