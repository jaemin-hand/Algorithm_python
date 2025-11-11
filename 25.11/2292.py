import sys
sys.stdin = open('input.txt','r')

N = int(input())

if(N == 1):
    print(1)
else:
    # 변수 초기화
    count = 1
    max_room = 1

    while N > max_room:
        # 다음 겹층으로 이동
        
        # max_room에 6의 배수를 더해 다음 겹의 최댓값으로 갱신
        max_room = max_room + (6 * count)
        count += 1
    print(count)