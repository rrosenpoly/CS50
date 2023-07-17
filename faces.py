def searchSubstring(string, substring):
    emotion = string
    if substring == ":)":
        emotion = string.replace(":)", "😊")
        return emotion
    if substring == ":(":
        emotion = string.replace(":(", "😞")
        return emotion
    else:
        return string
    
userinput = input("please enter a string with :) or :( and state whether you are happy or not")
result = searchSubstring(userinput, ":(") 
print(result)