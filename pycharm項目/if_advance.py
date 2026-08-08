tired_index = int(input("疲勞指數為(滿分為100):"))
mind_check = int(input("精神分數為(滿分為100):"))
if tired_index < 60 :
    if mind_check >= 60 :
        print("let's gooo!")
    else:
        print("算了休息吧")
elif tired_index >= 60 :
    if mind_check >= 60 :
        print("我們還是出門去做吧!")
    else:
        print("讓我再拖5分鐘")