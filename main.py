import json
sessions=[]
with open("data.json","r") as file:
    sessions=json.load(file)
print("NEXUS")
print("PERSONAL ACADEMIC OS")
choice=0
while choice!=4:
    print("1. 📚 Study")
    print("2. 🧠 Knowledge")
    print("3. 📊 Progress")
    print("4. ❌ Exit")
    choice =int(input("Choose an option: "))
    if choice==1:
        print("Study mode activated")
        q1=input("What did you study?")
        q2=int(input("How many minutes did you study? "))
        q3 =int(input("How confident are you? (1-5)"))
        print("✓ Study session recorded.")
        session = {
        "topic": q1,
        "minutes": q2,
        "confidence": q3}
        sessions.append(session)
        with open("data.json","w") as file:
            json.dump(sessions,file)
        sh=int(input("type 1 for showing the info"))
        if sh=="1":
            print(session)
    elif choice==2:
        topics = set()
        for i in sessions:
            topics.add(i["topic"])
        weakest_topic =""
        lowest_confidence = 6
        for topic in topics:
            total_topic_time = 0
            for i in sessions:
                if i["topic"] == topic:
                    total_topic_time += i["minutes"]

            print(topic, ":", total_topic_time, "minutes")
    elif choice==3:
        total_session=len(sessions)
        print("Your total study time is")
        total_time=0
        for i in sessions:
            total_time +=i["minutes"]
        total_confidence=0
        for i in sessions:
            total_confidence+=i["confidence"]
        avg_confidence=total_confidence/total_session
        print("Total Sessions     :",total_session)
        print("Total minutes studied",total_time,"minutes")
        print("Your avg confidence is",avg_confidence)
    elif choice==4:
        print("have a nice day")
    else:
        print("invalid")