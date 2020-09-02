class Solution:
    def selectionsort(self, array):
        if array == null or array is empty:
            return array
        for i in range(len(array) -1 ):
            glo = i
            for j in range(i+1, len(array)):
                if array[j] < array[glo]:
                    glo = j
        temp = array[i]
        array[i] = array[glo]
        array[glo] = temp
