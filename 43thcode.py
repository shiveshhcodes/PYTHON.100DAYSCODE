# f  = open("43thcode.txt" , "a")
# f.write("this is going to be my first comment on python and i don't know what to write so i am just writing anything lol.")
# f.close()
# f.write("\nthis is going to be my second line of comment on python and i don't know what to write so i am just writing anything lol.")
# f.close()

# here we will discover , what syntaxs to use to not put a file on closed!!

with open('43thcode.txt' , 'r') as f:
    # f.write('this is going to be my first line of code')
    # f.write('\nthis is going to be my second line of code')
    # f.write('\nthis is going to be my third line of code')
 result = f.read()
print(result)

# f = open('44thcode.txt' , 'r')
# lines = f.read()
# print(lines)
# f.close()
# with open('infinityy.txt' , 'a') as f:
#          f.write(f'day 0 of fun coding\n')
         
# while True:
#     for i in range (0 ,124):
#         extra_day = {i+1}
#         with open('infinity.txt' , 'a') as f:
#          f.write(f'day {extra_day} of fun coding\n')
#         if extra_day == 101:
#          break
        
        

