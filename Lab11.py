import os
import matplotlib.pyplot as plt

def find_id(name):
    file = open("../data/assignments.txt")
    lines = file.readlines()
    lines = [l.strip() for l in lines]
    for i in range(len(lines)):
        if lines[i] == name:
            return int(lines[i+1])
    return 0

def weight(id):
    assignments = open("../data/assignments.txt").readlines()
    assignments = [a.strip() for a in assignments]
    for i in range(len(assignments)):
        if assignments[i] == str(id):
            return (int(assignments[i + 1]))/100

    return 0

def calc_grade(id):
    #loop through each file in submissions folder, find one that matches the student
    #ID, if it does add the grade listed * assignment weight to the sum
    #grade is percentage + weight / 100. final grade is sum of these
    sum = 0
    for submission in os.listdir("../data/submissions"):
        with open(os.path.join("../data/submissions", submission)) as file:
            #getting a list with int values of stud ID, assign. ID, and score as a %
            sublist = file.readline().strip().split("|")
            sublist = [int(s) for s in sublist]
            if sublist[0] == id:
                sum += sublist[2] * weight(sublist[1])
    return sum / 10

def calc_stats(id):
    min = 10000
    max = 0
    sum = 0
    count = 0
    for submission in os.listdir("../data/submissions"):
        with open(os.path.join("../data/submissions", submission)) as file:
            # getting a list with int values of stud ID, assign. ID, and score as a %
            sublist = file.readline().strip().split("|")
            sublist = [int(s) for s in sublist]
            sum += sublist[2]
            count += 1
            if sublist[1] == id:
                if sublist[2] < min:
                    min = sublist[2]
                if sublist[2] > max:
                    max = sublist[2]
    return [min, max, sum/count]

def list_scores(name):
    scores = []
    id = find_id(name)
    for submission in os.listdir("../data/submissions"):
        with open(os.path.join("../data/submissions", submission)) as file:
            # getting a list with int values of stud ID, assign. ID, and score as a %
            sublist = file.readline().strip().split("|")
            sublist = [int(s) for s in sublist]
            if sublist[1] == id:
                scores.append(sublist[2])
    return scores


def main():
    print("1. Student Grade\n2. Assignment statistics\n3. Assignment graph")

    file = open("../data/students.txt")
    names = file.read().split("\n")
    #making all the lists
    student_ids = [int(n[0:3])for n in names]
    names = [n[3:len(n)] for n in names]
    students = {}
    for i in range(len(names)):
        students[names[i]] = student_ids[i]

    file2 = open("../data/assignments.txt")
    assignments = file2.read().split("\n")
    assignments = [assignments[a] for a in range(0,len(assignments),3)]

    option = int(input("Enter your selection: "))

    if option == 1:
        name = input("What is the student's name: ")
        if name not in students.keys():
            print("Student not found")
        else:
            print("Working on it..")
            print(students[name])
            print(f"{calc_grade(students[name]):.0f}%")

    elif option == 2:
        assignment = input("What is the assignment name: ")
        if assignment not in assignments:
            print("Assignment not found")
        else:
            assignment_id = find_id(assignment)
            min_val = calc_stats(assignment_id)[0]
            avg_val = calc_stats(assignment_id)[2]
            max_val = calc_stats(assignment_id)[1]


            print(f"Min: {min_val:.0f}%")
            print(f"Avg: {avg_val:.0f}%")
            print(f"Max: {max_val:.0f}%")

    elif option == 3:
        assignment_h = input("What is the assignment name: ")
        if assignment_h not in assignments:
            print("Assignment not found")
        else:
            scores = list_scores(assignment_h)
            plt.hist(scores, bins = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            plt.show()

    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()