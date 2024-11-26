from collections import namedtuple

def calculate_avg(student_list_data):
    total_marks = 0
    
    for student_data in student_list_data:
        total_marks += int(student_data.MARKS)
    return total_marks/len(student_list_data)

if __name__ == "__main__":

    num_of_students = int(input())
    column_name = input().split()
    dicted = {column_name[0]: 0 , column_name[1]: 1
              , column_name[2] : 2, column_name[3]: 3}
    student_data = namedtuple("student_data", column_name)

    student_list_data = list()
    

    for i in range(num_of_students):
        student_info = [data for data in input().split(' ') if data.strip() != '']
        
        student_entry = student_data(ID = student_info[dicted["ID"]],
                                     MARKS = student_info[dicted["MARKS"]],
                                     NAME = student_info[dicted["NAME"]],
                                     CLASS = student_info[dicted["CLASS"]])
        student_list_data.append(student_entry)

    print(round(calculate_avg(student_list_data), 2))



# ez approach
'''
if __name__ == "__main__":
    
    num_of_students = int(input())

    column_name = input().split()
    index_of_interst = column_name.index('MARKS')

    total_marks_scored = 0
    
    for i in range(num_of_students):
        data = [data for data in input().split(' ') if data.strip() != '']
        total_marks_scored += int(data[index_of_interst])

    print(round(total_marks_scored/num_of_students, 2))
'''