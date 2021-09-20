def Simple_insertion_Sort(arr):
    if len(arr)<=1:
        return arr
    else:
        for i in range(len(arr)):
            j=i
            target = arr[i]
            while j>0 and target<arr[j-1]:
                arr[j]=arr[j-1]
                j-=1
            arr[j] = target
        return arr


if __name__ == '__main__':
    arr = [9, 8, 7, 0, 6, 5, 1, 4, 3, 2]
    Simple_insertion_Sort(arr)
    print(arr)