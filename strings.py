# strings

print("hello world")
print('hello world\n')

print("let's code")
print('He said,"Come here."\n')

print('''bla bla bla
	bla bla '
	 '"" \n
	bla bla bla
	be be eb''')

print('hello ' "world!")
print("C:\nowhere\n") # want to print -> C:\nowhere

# raw strings : backslash character are not recognised here

print(r'C:\nowhere')
print(r"C:\nowhere""\\") # you cant use backslash(\) at the end
print(r'''C:\nowhere''')

print(repr('C:\nowhere'))
