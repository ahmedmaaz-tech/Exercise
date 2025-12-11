student_name = str("Ali Khan")
student_age = int(16)
student_grade = str("10th")
student_gpa = float(3.8)
# print(student_name, "is", student_age, "years old and currently in", student_grade, "grade with a GPA of", student_gpa,".")
print(f"{student_name} is {student_age} years old and currently in {student_grade} grade with a GPA of {student_gpa}.")

# Output: Ali Khan is 16 years old and currently in 10th grade with a GPA of 3.8.

customer_name = str ("Ayesha")
coffee_price = float (2.5)
sandwich_price = float (4.0)
cake_price = float (3.0)

# print("Customer Name:", customer_name , "Coffee:$", coffee_price , "Sandwich:$", sandwich_price ,"Cake:$", cake_price)
print(f"Customer Name: {customer_name} Coffee: ${coffee_price} Sandwich: ${sandwich_price} Cake: ${cake_price}")
print(f"Total Bill: ${coffee_price + sandwich_price + cake_price}")
print(f"Thank you for visiting our café, {customer_name}!")

#Output:
# Customer Name: Ayesha Coffee: $2.5 Sandwich: $4.0 Cake: $3.0
# Total Bill: $9.5
# Thank you for visiting our café, Ayesha!