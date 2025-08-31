

# numbers = [40, 40, 10, 10, 21, 21, 100,100, 400,400, 15, 15]

# def second_lowest_number():
#         numbers.sort()
#         z = numbers[0]
#         for i in numbers:
#                 if i > z:
#                     print(i)
#                     print(z)
#                     break
# second_lowest_number()

# second_smallest = sorted(set(numbers))[1]
# print([i for i in numbers if i == second_smallest])
# print(second_smallest)

if __name__ == '__main__':
    student_number = int(input("Enter the number of student: "))
    if not (2 <= student_number <= 5):
        print("Student number constaint must be between 2 and 5")
        
    else:
        records = []
        for _ in range(student_number):
                name = input("Enter student name: ")
                score = float(input("Enter student score: "))
                records.append(list([name,score]))
        scores = sorted(set(record[1] for record in records))
        if len(scores) > 1:
            second_smallest_score = scores[1]
            second_smallest_students = [record[0] for record in records if record[1] == second_smallest_score]
            second_smallest_students.sort()
            for student in second_smallest_students:
                    print(student)

        else:
                print("Not enough uniques scores to determine the second smallest.")
        
        

"""
Get input for no of student,
create a constraint if input n is less than or equal to 5 but greater than or equal to 2 
Multiply input no by 2,
declare variables name, score,
create a list record to append each input name and score to a list,
sort the scores in descending order
create a variable for the second smallest score within the list of list
sort the name of the second smallest variable list
print out the names of the second smallest variable 
print again.
"""   