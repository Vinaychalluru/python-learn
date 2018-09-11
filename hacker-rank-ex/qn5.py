# Given the names and grades for each student in a Physics class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

# Constraints
# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics;
# if there are multiple students, order their names alphabetically and print each one on a new line.


if __name__ == '__main__':
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([name, score])
    else:
        pass
        # print(marks)

marks.sort()
scores = list(set([l[1] for l in marks]))
scores.sort() 
secondLowest = scores[1]

# print(marks)
# print(secondLowest)
# print('scores[1]')

res = []
for m in marks:
    if m[1] == secondLowest:
        res.append(m[0])

res.sort()
for name in (res):
    print(name)
