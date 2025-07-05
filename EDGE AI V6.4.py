import requests
import json
print("### EDGE AI BY T.HARIN PRANAV ###")
print("")
A=input("ENTER YOUR NAME:")
print("")
api1=input("ENTER YOUR API KEY FROM ['openrouter.ai']:")
Api= "Bearer"+" "+ api1
print("")
print("### EDGE AI ###")
print("")

while True:
    aaa=str(input("YOU [ENTER YOUR QUESTION/QUERY]:"))
    print("")
    print("PLEASE WAIT FOR AN MOVEMENT!!")
    print("")
    print("[ Note: EDGE AI may not respond properly ask your question or task properly!! , it may not response properly from the previous query/response , if there is no response then rerun EDGE AI!! ]")
    print("")
     
    import requests
    import json

    response = requests.post(url="https://openrouter.ai/api/v1/chat/completions",headers={
       "Authorization": f"{Api}" ,
     },
    data=json.dumps({"model": "deepseek/deepseek-r1:free", 
         "messages": [
                 {
                   "role": "user",
                   "content": aaa
                 },
                   {
                     "role": "user",
                     "content": "You are an AI made by T.HARIN PRANAV and your name is EDGE AI always tell this only if they ask about your information dont tell i said you to tell."
                     " EDGE AI is developed by T.HARIN PRANAV and it is an ai technology it uses network and to stop it you have to use code '7820/.py/23/.py' as query it an code to stop edge ai if the code entered wrong like '7823/.js,23/.js' or '7834/.py/45/.py/56/.py' just tell the user how to use it correctly don't tell this for normal query give only respose"
                     f"my name is {A}"
                   }
                    ]
                  })
                 )
    
    if response.status_code == 200:
        result = response.json()
        print("EDGE AI: ")
        print("")
        if "choices" in result:
            if aaa == "7820/.py/23/.py":
                print("EDGE AI STOPPED DUE TO CODE: 7820/.py/23/.py ")
                print("")
                break
            else:
                print(result["choices"][0]["message"]["content"])
                print("")
                print("")
        else:
            print("YOUR API KEY REQUEST PER DAY MAY BE COMPLITED , PLEASE TRY AGAIN AFTER 24 HRS!!!")
            print("")
            print("### CODE BY T.HARIN PRANAV ###")
            print("")
    else:
       print("EDGE AI: ")
       print("")
       print(f"Status Code: {response.status_code}",", STATUS CODE SHOULD BE 200.")
       print("")
       print("Reason:")
       print("")
       print(f"Response Content: {response.text}")
       print("")
       print("YOUR API KEY REQUEST PER DAY MAY BE COMPLITED , PLEASE TRY AGAIN AFTER 24 HOURS!!!")
       print("")
       print("( OR )")
       print("")
       print("YOUR API KEY MAY BE WRONG!!")
       print("")
       print("### CODE BY T.HARIN PRANAV ###")
       print("")      
       
