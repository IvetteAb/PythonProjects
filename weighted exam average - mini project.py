# weighted exam score average

# enter how many exams you've done, hence the int (i.e. integer)
# python prints the quote in the terminal & you can enter your no of exams (in the terminal)
number_of_exams = int(input("Enter number of exams: "))
print(number_of_exams)

# enter how many credits these exams cover - 120
# python prints the quote in the terminal & you can enter your credits (in the terminal)
total_credits = int(input("Enter how many credits these exams cover: "))

# add up % for each exam using 'for' loops
# python will start off w/ 0, but when you add exams & credits it'll adjust i.e. add up % from each exam
# some ppl use 'i' as it's general - here we used 'exam'
# this is looped from L18 & L19, so it'll keep adding onto the previous average then it'll print your av
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits     # % for that specific exam
print("Your average is", average)
