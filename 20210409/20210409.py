def solution(priorities, location):
    chkVal = [0, -1]
    nowVal = priorities[location]
    higherNum = 0
    sameCnt = 0
    maxVal = max(priorities)
    maxValLoc = -1
    maxLocation = 0
    setStart = True
    for i in range(len(priorities)):
        if setStart and maxVal == priorities[i] :
            maxLocation = i
            setStart = False
        if setStart == False and chkVal[0] > priorities[i] and priorities[location] < chkVal[0] :
            chkVal = [priorities[i], i]
            if i < location :
                maxValLoc = 0
            elif i > location :
                maxValLoc = 1

        if priorities[location] < priorities[i]:
            higherNum += 1
    if chkVal[1] == -1 :
        for i in priorities[maxLocation::] :
            if i == priorities[location] :
                sameCnt +=1
        sameCnt += 1
        if location != 0 :
            for i in priorities[0:location] :
                if i == priorities[location] :
                    sameCnt +=1
        return sameCnt + higherNum
    else :
        if maxValLoc == 0:
            for i in range(len(priorities)) :
                if i > location and i < chkVal[1]:
                    continue
                if i == priorities[location] :
                    sameCnt +=1
            return sameCnt+ higherNum
        elif maxValLoc == 1 :
            for i in priorities[chkVal[1]:location] :
                if i == priorities[location] :
                    sameCnt +=1
            return sameCnt + higherNum
    return 1

print(solution([1, 1, 9, 1, 1, 1], 0))