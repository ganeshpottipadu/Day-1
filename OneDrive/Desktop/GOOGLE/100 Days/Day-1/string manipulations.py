# Joining two strings with + 
first_name = "Ganesh"
last_name = "Pottipadu"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Finding the lenght of string
text = "Python Programming"
print("Length of text:", len(text))

# changing the case 
msg = "hello python learners"
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())
print("Title Case:", msg.title())

# Indexing & Slicing 
word = "Python"
print("First character:", word[0])    # P
print("Last character:", word[-1])    # n
print("First three letters:", word[:3])  # Pyt
print("Last three letters:", word[-3:])  # hon


# Splitting & Joining
fruits = "apple,banana,orange"
fruit_list = fruits.split(",")
print("After split:", fruit_list)
joined = " - ".join(fruit_list)
print("After join:", joined)














