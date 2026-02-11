matrix = []

def calculateAverageStudents(matrix):
    for i in range(3):
        sum = 0
        for j in range(3):
            sum+=int(matrix[i][j])
        print("Average of Student "+ str(i+1) + " is " + str((sum/3)))

#input
for i in range(3):
    studentScores = []
    for j in range(3):
        studentScores.append(input("Enter Score: "))
        matrix.append(studentScores)
print(matrix[0][0])

calculateAverageStudents(matrix)
