X, Y = map(int, input().split())
Z = (Y*100)//X 

left = 1
right = X
answer = X     # (자연수) 승률이 바뀌기 위해 플레이해야 할 게임의 최소 횟수

if Z >= 99:
	print(-1)
else:
	while left <= right:
		mid = int((left + right)/2)
		new_z = int((Y+mid)/(X+mid)*100)
		if new_z > Z:
			answer = mid
			right = mid -1
		else:
			left = mid + 1
	print(answer)