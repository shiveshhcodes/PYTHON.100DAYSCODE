# # lets create a KBC game in python!!

# questions = [
#     {
#         "question": "what is the capital of india" ,
#         "options": ["A. Delhi" , "B. Mumbai "],
#         "Correct Answer": "A",
#         "amount":"1000"
#     } ,
#     {
#         "question": "what is the capital of MP" ,
#         "options": ["A. Bhopal" , "B. Indore "],
#         "Correct Answer": "A",
#         "amount":"2000"
#     } ,
#     {
#         "question": "what is the capital of J&K" ,
#         "options": ["A. Delhi" , "B. Sri Nagar "],
#         "Correct Answer": "B",
#         "amount":"5000"
#     } , 
#     {
#         "question": "what is the capital of Maharastra" ,
#         "options": ["A. Nashik" , "B. Mumbai "],
#         "Correct Answer": "B",
#         "amount":"10000"
#     }
# ]

# total_amount=0

# for a in questions:
#  print(a["question"])
#  for option in a["options"]:
#   print(option) 


# user_answer = input("Enter Your Answer A/B : ").upper()

# # lets check is the user answer is correct or not.

# if user_answer == a["correct"]:
#     total_amount += a["amount"]
#     print("Congratulations , you just won" , a["amount"])
# else:
#      print("this is wrong answer , the correct answer was" , a["correct"])
#         break

# print()
# print("Game over , Total prize:" , total_amount)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai"],
        "Correct Answer": "A",
        "amount": 1000
    },
    {
        "question": "What is the capital of MP?",
        "options": ["A. Bhopal", "B. Indore"],
        "Correct Answer": "A",
        "amount": 2000
    },
    {
        "question": "What is the capital of J&K?",
        "options": ["A. Delhi", "B. Sri Nagar"],
        "Correct Answer": "B",
        "amount": 5000
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["A. Nashik", "B. Mumbai"],
        "Correct Answer": "B",
        "amount": 10000
    }
]

total_amount = 0

for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    user_answer = input("Enter Your Answer (A/B): ").upper()
    
    if user_answer == question["Correct Answer"]:
        total_amount += question["amount"]
        print("Congratulations, you just won", question["amount"])
    else:
        print("This is the wrong answer, the correct answer was", question["Correct Answer"])
        break

print()
print("Game over. Total prizee:", total_amount)
