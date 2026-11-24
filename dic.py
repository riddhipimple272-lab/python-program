customer_info={"cust_id":1234,"name":"raj","city":"pune"}
print(customer_info)

employee_id={"emp_name":"ram","emp_salary":20000,"emp_city":"punr"}
for k in enumerate (employee_id):
    print(k)


customer_info={"cust_id":1234,"name":"siddhi","city":"nanded"} 
for r in (customer_info):
   print(r)  

student={"stu_name":"raj","stu_id":3456,"stu_city":"nagpur"}
print(student.get)


student.get("age")
print(student.get("course"))

student={"name":"riddhi","age":22}
print(student.get("city","nanded"))



mobile={"price":2000,"model":"moto"}
print(mobile.copy)

student = {
     "name": "Siddhi",
     "age": 22,
    "course": "Python"
 }

print(student.get("name"))
print(student.get("age"))
print(student.get("course"))



student = {
    "name": "Siddhi",
    "age": 22,
    "course": "Python"}
new_student = student.copy()
print(new_student)


student = {"name": "rahul", "age": 22}
new_student = student.copy()
new_student ["age"] = 23
print(student)
print(new_student)



a={1,2,3}
b={3,4,5}
union_set=a.union(b)
print(union_set)

union_set=a|b
print(union_set)


a={1,2,3}
b={3,4,2}
intersection_set=a.intersection(b)
print(intersection_set)

intersection_set=a & b
print(intersection_set)


a={1,2,5,7,6,3}
b={3,4,2}
difference_set=a.difference(b)
print(difference_set)

difference_set=a-b
print(difference_set)



a={1,2,3}
b={3,4,5}
s_diff=a.symmetric_difference(b)
print(s_diff)

s_diff=a^b
print(s_diff)

