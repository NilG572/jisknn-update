import pandas as pd


def knn(sortedEuclideanDistance, sortedRemark, k):
    passCounter, supplementaryCounter = 0, 0
    passLength, supplementaryLength = 0.0, 0.0

    for i in range(0, k):
        if (sortedRemark[i] == 0):
            supplementaryCounter += 1
            supplementaryLength += sortedEuclideanDistance[i]
        else:
            passCounter += 1
            passLength += sortedEuclideanDistance[i]
    if (passCounter > supplementaryCounter):
        print("For k =" + str(k) + " you may pass")
        return 1
    elif (passCounter < supplementaryCounter):
        print("For k =" + str(k) + " you may get supplementary")
        return -1
    elif (passCounter == supplementaryCounter):
        if (passLength < supplementaryLength):
            print("For k =" + str(k) + " you may pass because " + str(passLength) + " < " + str(supplementaryLength))
            return 1
        elif (passLength > supplementaryLength):
            print("For k =" + str(k) + " you may get supplementary because " + str(supplementaryLength) + " < " + str(
                passLength))
            return -1
        elif (passLength == supplementaryLength):
            print("For k =" + str(k) + " you may pass or may get supplementary")
            return 0


def will_pass(firstsemMarks, secondsemMarks):
    """

    :param firstsemMarks: write first sem marks (integer)
    :param secondsemMarks: write second sem marks (integer)
    :return: weather the has passed or not


    """
    url = "result.csv"
    result = pd.read_csv(url)

    first = result['FIRST']
    second = result['SECOND']
    remarks = result['REMARKS']

    print(" Enter the marks to be tested----")
    firstSemMarks = firstsemMarks
    secondSemMarks = secondsemMarks

    upperBoundOfK = 7
    print(" Upper bound of k is " + str(upperBoundOfK))

    passMarks = 40
    print(" Pass marks is " + str(passMarks))
    print(" Number of previous data instances is " + str(len(first)))

    euclideanDistance = []
    euDisRemark = {}
    print("\nFIRST\tSECOND\tREMARKS\tEUCLIDIAN DISTANCE")
    for i in range(0, len(first)):
        euclideanDistance.append(pow(pow(first[i] - firstSemMarks, 2) + pow(second[i] - secondSemMarks, 2), 0.5))
        euDisRemark[euclideanDistance[i]] = remarks[i]
        print(" " + str(first[i]) + "\t  " + str(second[i]) + "\t   " + str(remarks[i]) + "\t" + str(
            euclideanDistance[i]))

    sortedEuclideanDistance = (sorted(euDisRemark))
    sortedRemark = []
    for i in sorted(euDisRemark):
        sortedRemark.append(euDisRemark[i])

    print("\nAfter sorting ---\nREMARKS\tEUCLIDIAN DISTANCE")
    for i in range(0, upperBoundOfK):
        print("   " + str(sortedRemark[i]) + "\t" + str(sortedEuclideanDistance[i]))

    total = 0
    print(" ")
    for k in range(1, upperBoundOfK + 1):
        result = knn(sortedEuclideanDistance, sortedRemark, k)
        total += result
    if total < 0:
        return "you may get supplementary.  YOU SHOULD STUDY HARD!!📚"
    elif total > 0:
        return "You may pass.  KEEP IT UP!!👍"
    else:
        return "You may pass or may get supplementary.  FOCUS ON YOUR STUDIES!!🎯"

if __name__ == '__main__':
   print( will_pass(5,7))
