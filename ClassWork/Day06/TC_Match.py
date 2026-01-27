# Match Function
import re
text ="python is powerful"
result = re.match("python",text)
if result:
    print("Match Found")

else:
    print("Not Match")


# another example
import re
text ="python is powerful"
result = re.match("java",text)
if result:
    print("Match Found")

else:
    print("Not Match")


# Search Function
searchresult=re.search("python",text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())


email="admin@gmail.com"
if re.match(r"[a-zA-z]+@",email):
    print("Valid Start")

# Full Match to check full match or not
result2=(re.fullmatch(r"/d{10}","1234567890"))
print(result2)


# Find All
print(re.findall(r"\d+","price 50 and 100 and 20"))

# Find Iter
for n in re.finditer(r"\d+","A1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())


# Special Sequence

print(re.search(r"/d+","Age is 25"))


# MetaClass
print(re.search(r"^a.*c$","abnkkkkkknnc"))


print(re.search(r"/w+(?=@)","test@gmail.com"))



print(re.search("python", "Python", re.I))


text4="one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))