def bubble_sort(arr):
    if len(arr)<1:
        return arr
    else:
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

if __name__ == '__main__':
    arr = [9, 8, 7, 0, 6, 5, 1, 4, 3, 2]
    bubble_sort(arr)
    print('冒泡：',arr)
