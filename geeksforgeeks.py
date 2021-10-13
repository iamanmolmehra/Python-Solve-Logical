##################    BASIC PROGRAMS    ###################





# # Factorial #
# inp = int(input('Enter a number \n'))

# t = 1

# for i in range(1,inp+1) :
#     t = t * i

# print(t)






# # Armstrong #
# inp = int(input('Enter a number \n'))

# su = 0
# neq = inp

# while neq > 0 :
#     dig = neq % 10
#     su = su + dig**3
#     neq = neq // 10

# if (su == inp) :
#     print('is an armstrong number')
# else :
#     print('is not an armstrong number')






# # Printing all Prime numbers in an Interval #
# lower = int(input('Enter a number \n'))
# upper = int(input('Enter another number \n'))

# for i in range(lower, upper+1) :
#     if (i>1) :
#         for j in range(2,i) :
#             if (i%j == 0) :
#                 break
#         else : 
#             print(i)






# # Prime numbers from 1 to 100 #
# for i in range(2,101) :
#     for j in range(2,i) :
#         if (i%j == 0) :
#             break
#     else :
#         print(i)





# #  For checking whether a number is Prime or not #
# f = int(input('Enter a number \n'))

# for i in range(2,f) :
#     if (f%i == 0) :
#         print(f,'is not a prime number')
#         break
# else : 
#     print(f,'is a prime number')






# # For n-th Fibonacci number # 
# n = int(input('Enter the number of elements in Fibonacci Series : '))

# fibonacciSeries = [0,1]

# if n<0 : 
#     print('Incorrect Input')
# elif n<=2 : 
#     fibonacciSeries[n-1]
# else :
#     for i in range(2, n) :
#         g = fibonacciSeries[i-1] + fibonacciSeries[i-2]
#         fibonacciSeries.append(g)

# print(fibonacciSeries)







# For cheking Fibonacci number #
# num1 = 0
# num2 = 1
# num3=0
# user = int(input("Enter Num: "))
# while num3<user+1:
#     print(num3)
#     if num3==user:
#         print("Moj kar di...")
#         break
#     num1 = num2
#     num2=num3
#     num3 = num1+num2
# else:
#     print("Moj nahi ki...")






# # For n\’th multiple of a number in Fibonacci Series #
# k = int(input("Enter the Num: "))
# n = int(input("Enter the multiple: "))
# n1,n2,i = 0,1,1
# while n != 0 :
#     n3 = n2+n1
#     n1 = n2 
#     n2 = n3
#     if (n2%k == 0):
#         n-=1
#     i+=1
# print(i)







# # ASCII Value of a character #
# c = 'g'
# print("The ASCII value of '" + c + "' is", ord(c))






# # Sum of squares of first n natural numbers #
# n = int(input('Enter a number \n'))
# sum = 0
# for i in range(1, n+1) :
#     p = i**2
#     sum = sum + p
# print(sum)






# # For cube sum of first n natural numbers #
# n = int(input('Enter a number \n'))
# sum = 0
# for i in range(1, n+1) :
#     p = i**3
#     sum = sum + p
# print(sum)






####################    ARRAY PROGRAMS    ###################





# # Program to find sum of array #
# n = input("Enter the elements of list seperately : ").split()
# sum = 0

# for i in n :
#     sum = sum + int(i)
# print(sum)






# # To find largest element in an array #
# n = input("Enter the elements of list seperately : ").split(" ")
# max = float(n[0])
# for i in range(0,len(n)) :
#     if float(n[i])>max :
#         max = float(n[i])

# print(max)





# # For array rotation #
# arr = input("Enter the elements of list seperately : ").split(" ")
# arr = list(map(lambda x: int(x), arr))
# # print(arr)
# # arr = list(filter(lambda x: x<=10, arr))
# # print(arr)
# n = int(input("Enter the rotation : "))
# for i in range(0, n):
#     first = arr[0]
#     for j in range(0, len(arr)-1) :
#         arr[j] = arr[j+1]
#     arr[len(arr)-1] = first

# print()
# for i in range(0, len(arr)) :
#     print(arr[i])







# To Split the array and add the first part to the end #
# arr = input("Enter the elements of list seperately : ").split(" ")
# arr = list(map(lambda x: int(x), arr))
# n = int(input("Enter the rotation : "))
# for i in range(0, n):
#     first = arr[0]
#     for j in range(0, len(arr)-1) :
#         arr[j] = arr[j+1]
#     arr[len(arr)-1] = first

# print()
# for i in range(0, len(arr)) :
#     print(arr[i])






# Find remainder of array multiplication divided by n #
arr = input('Enter the elements of the array').split(' ')
arr = list(map(lambda x: int(x), arr))
n = input("Enter the number of the multiplication:")

for i in range(0, len(arr)) :
    arr[]
