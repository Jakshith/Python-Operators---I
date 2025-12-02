print("Enter Marks obtained in 4 subjects: ")
maths = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = maths+english+science+hindi
print("sum of all the 4 subjects: ", sum)

perc = (sum/400)*100

print (end="Precentage Mark = ")
print (perc)