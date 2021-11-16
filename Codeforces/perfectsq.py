def main() -> None:
    for test in range(int(input())):
        a, b = map(int, input().split())
        ans = min(max(2 * a, b), max(2 * b, a))
        print(ans ** 2)
 
 
if __name__ == '__main__':
    main()