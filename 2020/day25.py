import concurrent.futures
import time

def transform(subjectNumber,loopSize):
    value = 1
    for _ in range(loopSize):
        value *= subjectNumber
        value = value % 20201227
    
    return value,loopSize

def getLoopSize(publicKeys,subjectNumber,maxLoopSize):

    answer = {}

    value = 1
    for loopSize in range(maxLoopSize):
        value *= subjectNumber
        value = value % 20201227

        if value in publicKeys:
            if value not in answer:
                answer[value] = loopSize+1
        
        if len(answer) == len(publicKeys):
            break
    
    return answer


if __name__ == '__main__':

    t0 = time.time()

    publicKey1 = 5764801
    publicKey2 = 17807724

    publicKey1 = 3248366
    publicKey2 = 4738476

    # maxLoopSize = 1000

    # for subjectNumber in range(7,8):
    
    #     loopSize1,_ = getLoopSize([publicKey1],subjectNumber,maxLoopSize)
    #     if loopSize1 == None:
    #         continue
    #     else:
    #         print('loopSize1: ',loopSize1)
        
    #     loopSize2,_ = getLoopSize([publicKey2],subjectNumber,maxLoopSize)
    #     if loopSize2 == None:
    #         continue
    #     else:
    #         print("loopSize2:",loopSize2)

    #     encryptionKey1,_ = transform(publicKey1,loopSize2)
    #     encryptionKey2,_ = transform(publicKey2,loopSize1)

    #     if encryptionKey1 == encryptionKey1:
    #         print(subjectNumber,loopSize1,loopSize2,encryptionKey1,encryptionKey2)
    #         break

    # maxLoopSize = 1000000000
    # maxSubjectNumber = 10000
    # publicKeys = [publicKey1,publicKey2]
    # manualSubjectNumbers = [
    #     699,
    #     916,
    #     1318,
    #     1972,
    #     3113,
    #     3632,
    #     4080,
    #     4618,
    #     4716,
    #     5266,
    #     5639,
    #     5817,
    #     6471,
    #     6590,
    #     7027,
    #     7124,
    #     7817,
    #     8813
    #     ]
    # for subjectNumber in range(7,8): #manualSubjectNumbers: #range(1,maxSubjectNumber+1):
    #     loopSize = getLoopSize(publicKeys,subjectNumber,maxLoopSize)

    #     if loopSize:
    #         print(loopSize,subjectNumber)

    #     if len(loopSize) == len(publicKeys):
    #         print(loopSize,subjectNumber)
    #         break
    #     if subjectNumber%10000 == 0:
    #         print(subjectNumber)
    # print(loopSize,subjectNumber)
    # print(time.time() - t0)

    encryptionKey1,_ = transform(3248366,17111924)
    encryptionKey2,_ = transform(4738476,13330548)
    print(encryptionKey1)
    print(encryptionKey2)

    # 2168386 too low