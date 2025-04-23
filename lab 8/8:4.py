s = {"Aaron", "Arpit", "Aryan", "Aaditya","Bhavya", "Batman", "Bershka", "Bortoleto"}
A = set()
B = set()

for i in s:
    if i.startswith("A"):
        A.add(i)
    elif i.startswith("B"):
        B.add(i)

print(f"s = {s}")
print(f"A = {A}")
print(f"B = {B}")
