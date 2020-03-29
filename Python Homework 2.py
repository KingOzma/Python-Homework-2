#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x[0] == 's':
        print(x)
	
#Use range() to print all the even numbers from 0 to 100
x = range(0,101)
for n in x:
    if n % 2 == 0:
        print(n)
		
		
#st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x) % 2 == 0:
        print(x)
		
#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(0,101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0: 
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

#Use a List Comprehension to create a list of the first letters of every word in the string below:
		
st = 'Create a list of the first letters of every word in this string'
for x in st.split():
        print(x[0])
		
[x[0] for x in st.split()]
		
		