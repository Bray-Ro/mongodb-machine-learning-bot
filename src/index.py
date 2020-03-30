import pymongo
# SETUP DATABASE
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db"]
questions = db["questions"]
def ask():
    question = input("Hello, I am Data you can ask me anything: ")
    check = questions.count_documents({"question": question})
    if check == 0:
        answer = input("I do not know the answer to that yet, please tell me: ")
        questions.insert_one({"question": question, "answer": answer})
        print("I know know the aswer to \"" + question + "\" now!")
        ask()
    else:
        
        answer = questions.find({"question": question})
 
        for x in answer:
            x = str(x)
            x = x.split(", ")
            x = x[2]
            x = x.split(":")
            x = x[1]
            x = x[:-1]
            print(x)
        ask()
        
ask()
