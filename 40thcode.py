import os
# if not os.path.exists("100dayscodetrial"):
#     os.mkdir("100dayscodetrial")
    
# for i in range (1 , 3):
#     with open(f"100dayscodetrial/{i+1}.py" , "w") as tested:
#         pass

cwd = os.getcwd()
# print(f"Current working directory: {cwd}") 

newdir = os.listdir(cwd)
# newdir_ls = list(newdir)
# print(newdir_ls)
# index = 0
# print(f"current working directory is {cwd}")
# newdir_ls.sort()
# newdir_ls.reverse()
for index , item in enumerate(newdir):
    print(f"{index}. {item}")
