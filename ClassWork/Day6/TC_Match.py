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