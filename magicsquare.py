def computeCost(mat1, mat2):
    """
    Do an element-wise subtraction of values mat1[i,j] - mat2[i,j]
    """
    cost_ = 0
    #print('mat1->',mat1)
    #print('mat2->',mat2)

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            cost_ += abs(mat1[i][j] - mat2[i][j])
            #print('cost now is ',cost_)

    #print(cost_)

    return cost_


def formingMagicSquare(s):
    """
    Input: 3x3 array, may have duplicate numbers
    Output: magic square with total equal 15 in any rows, columns, and diagonally adjacent cells
    3x3 Magic Square - model
    816
    357
    492

    we can do 8 directional variant configurations

    """

    magicN = 15     # mandatory
    configs = {'1':[[8,1,6],[3,5,7],[4,9,2]],
               '2':[[4,3,8],[9,5,1],[2,7,6]],
               '3':[[2,9,4],[7,5,3],[6,1,8]],
               '4':[[6,7,2],[1,5,9],[8,3,4]],
               '5':[[6,1,8],[7,5,3],[2,9,4]],
               '6':[[8,3,4],[1,5,9],[6,7,2]],
               '7':[[4,9,2],[3,5,7],[8,1,6]],
               '8':[[2,7,6],[9,5,1],[4,3,8]]}
    costs = []

    #print(configs)

    for cfgkey in configs:
        cost = computeCost(s, configs[cfgkey])
        costs.append(cost)
        #print(cfgkey, configs[cfgkey], ' --> ', cost)

    return min(costs)

if __name__ == "__main__":
    input_ = [[2,7,5],[9,5,1],[4,3,8]]
    #print(input_)
    print(formingMagicSquare(input_))
