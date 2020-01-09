import math

(N, Y) = map(int, (input().split()))

count = 0

#All_cases = math.factorial(N+2)/(math.factorial(N)*math.factorial(2))
#print(All_cases)

for x in range(N):
    for y in range(N):
        for z in range(N):
            if x + y + z == N and 10000*x + 5000*y + 1000*z == Y:
                print(x, y, z)
                break

            else:
                count += 1

        else:
            continue
        break
    else:
        continue
    break

#print(count)

if count == N**3:
    print(-1,-1,-1)