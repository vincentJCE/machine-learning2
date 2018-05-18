n = 10
X = list(range(n))
Y = [1, 1, 1,  -1, -1, -1,  1, 1, 1,  -1]

import math
def weak_classifier(X, Y, D):
    min_error = 10000
    index = 0
    is_positive = True
    #is_positve=True,在split左边被分类为-1，右边被分类为1
    #is_positive=False, 在split左边被分类为1， 右边被分类为-1
    for split in range(n+1):
        
        sum = 0
        for i in range(split):
            if Y[i] == 1:
                sum += D[i]
        for i in range(split, n):
            if Y[i] == -1:
                sum += D[i]
        
        if sum < min_error:
            index = split
            min_error = sum
            is_positive = True
            

 

        sum = 0
        for i in range(split):
            if Y[i] == -1:
                sum += D[i]
        for i in range(split, n):
            if Y[i] == 1:
                sum += D[i]

        if sum < min_error:
            index = split
            min_error = sum
            is_positive = False
            

    Y_hat = list(range(n))
    if is_positive:
        for i in range(index):
            Y_hat[i] = -1
        for i in range(index, n):
            Y_hat[i] = 1

    else:
        for i in range(index):
            Y_hat[i] = 1
        for i in range(index, n):
            Y_hat[i] = -1
            
    return (Y_hat, min_error)

def main():
    D = [1/n] * n
    H = [0] * n
    M = 3
    for m in range(M):
        Y_hat, error = weak_classifier(X, Y, D)
        if error == 0:
            print('find a perfect classifier and break')
            break
        alpha = 0.5*math.log((1-error)/error)
        print('alpha', alpha)
        for i in range(n):
            H[i] += alpha*Y_hat[i]
        Z = 0
        for i in range(n):
            D[i] *= math.e**(-alpha*Y[i]*Y_hat[i])
            Z += D[i]
        for i in range(n):
            D[i] /= Z
            
    print('Real label:  ', Y)
    print('Prediction:  ', H)
        
main()