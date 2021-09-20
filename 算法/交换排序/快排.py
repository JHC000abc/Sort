def quick_sort(arr,start,end):
    if start>end:
        return
    else:
        left=start
        right=end
        target=arr[left]
        while left<right:
            while left<right and arr[right]>=target:
                right-=1
            arr[left]=arr[right]
            while left<right and arr[left]<target:
                left+=1
            arr[right]=arr[left]
        arr[left]=target

        quick_sort(arr,start,left-1)
        quick_sort(arr,left+1,end)

if __name__ == '__main__':
    arr=[9,8,7,0,6,5,1,4,3,2]
    quick_sort(arr,0,len(arr)-1)
    print('快排：',arr)