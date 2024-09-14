questions=[["which language was used to create fb?","python","french","javascript","php","None",4],
           ["which language was used to create fb?","python","french","javascript","php","None",4],
           ["which language was used to create fb?","python","french","javascript","php","None",4],
           ["which language was used to create fb?","python","french","javascript","php","None",4],
            ["which language was used to create fb?","python","french","javascript","php","None",4],
             ["which language was used to create fb?","python","french","javascript","php","None",4]]
levels=[1000,2000,3000,4000,80000,32000]
money=0
i=0
for i in range(0,len(questions)):
    questions=questions[i]
    print(f"question for RS.{levels[i]}")
    print(f"a.{questions[1]} b.{questions[2]} ")
    print(f"c.{questions[3]} d.{questions[4]} ")
    reply=int(input("enter your answer(1-4)"))
    if(reply==questions[-1]):
        print(f"correct answer,you have won rs.{levels[i]}")
    else:
        if(i==4):
            money=10000
        elif(i==9):
          money=32000
        elif(i==14):
            money=500000
        print("wrong answer")
        break
print(f"your take home money is{money}")



