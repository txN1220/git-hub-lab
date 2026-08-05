def bubble_sort(a):
    n=len(a)
    for p in range(n - 1):
        swaped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaped = True
        if not swaped:
            break
if __name__ == "__main__":
    test_data = ([4,2,5,6,1,3])
    print("排序前的資料;", test_data)
    bubble_sort(test_data)
    print("排序後的正確資料", test_data)

