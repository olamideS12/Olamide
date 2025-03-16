fruit=["banana","apple","orange","kiwi","grape"]
print(fruit)

fruit.remove("orange")
print(fruit)
 
fruit.sort()
print(fruit)

fruit.pop()
print(fruit)

fruit.reverse()
print(fruit)

fruit.append("carrot")
print(fruit)

fruit.clear()
print(fruit)

page1 = {
    "index": "254",
    "page no": "19000",
    "title": "freinds that will stay forever"
    }

print(page1["index"])
print(page1.get("page no"))

page1["page no"]="34567"
print(page1["page no"])

page1["chapter"]= 34
print(page1["chapter"])

page1.pop("index")
print(page1)
