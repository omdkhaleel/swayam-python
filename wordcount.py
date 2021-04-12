def wordcount():
	w=input("Enter your word: ")
	c=input("Which letter you want to count: ")
	count=0
	for char in w:
		if char == c:
			count=count+1
	print(count)
