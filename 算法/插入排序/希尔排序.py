def shell_Sort(arr):
   target=len(arr)//2
   while target>0:
       for j in range(target,len(arr)):
           i=j
           while i>0 and arr[i]<arr[i-target]:
               arr[i],arr[i-target]=arr[i-target],arr[i]
               i-=target
       target//=2


if __name__ == '__main__':
    arr = [9, 8, 7, 0, 6,5, 1, 4, 3, 2]
    shell_Sort(arr)
    print(arr)

