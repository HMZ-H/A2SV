# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

def main():
    n = int(input()) 
    arr = list(map(int, input().split()))
    
    ex = [False, False]  
    for num in arr:
        ex[num % 2] = True
    
    if ex[0] and ex[1]:
        arr.sort()
    
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
