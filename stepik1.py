from pprint import pprint


from pprint import pprint
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006',
               'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
                 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]
print(pprint(result))
d = [{'S001': {'Camila Rodriguez': 93}}, {'S002': {'Juan Cruz': 93}}, {'S003': {'Dan Richards': 93}}, {'S004': {'Sam Boyle': 93}}, {'S005': {'Batista Cesare': 
93}}, {'S006': {'Francesco Totti': 93}}, {'S007': {'Khalid Hussain': 93}}, {'S008': {'Ethan Hawke': 93}}, {'S009': {'David Bowman': 93}}, {'S010': {'James Milner': 93}}, {'S011': {'Michael Owen': 93}}, {'S012': {'Gary Oldman': 93}}, {'S013': {'Tom Hardy': 93}}]

result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]
