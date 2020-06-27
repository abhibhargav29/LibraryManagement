from itertools import combinations

def maxPairs(skillLevel, minDiff):
    list_pairs = combinations(skillLevel,2)

    cnt=0
    done=[]
    for pair in list_pairs:
        if(pair[0] not in done and pair[1] not in done):
            if(abs(pair[0]-pair[1])>=minDiff):
                cnt+=1
                done.append(pair[0])
                done.append(pair[1])

    return cnt


skillLevel_count = int(input().strip())
skillLevel = []

for i in range(skillLevel_count):
    skillLevel_item = int(input())
    skillLevel.append(skillLevel_item)

minDiff = int(input().strip())

result = maxPairs(skillLevel, minDiff)
print(result)
