import tweepy

#login to twitter's servers
auth = tweepy.OAuthHandler("customer_token_here", "customer_secret_here")
auth.set_access_token("app_token_here", "app_security_here")
authTwo = tweepy.API(auth)

print("1. Search for a term")
print("2. Display a list of current trends in the United States")
print("3. Exit")
userSelection = input("What do you want: ")
if(userSelection == '1'):
    #Asking user what term they want to search for
    searchTerm = input("Please enter the term you would like to search for: ")
    # Search for whatever item q. q = query in twitter's api, printing out 10 since limiting returns via API is unclear
    searchReturn = tweepy.Cursor(authTwo.search, q=searchTerm).items(10)
    print("Printing out search results now boss: ")
    for item in searchReturn:
        print(item.text)
elif(userSelection == '2'):
    #Finding and returning trends using WOEID 2450022 for USA, used USA for test since mostly english, gives less unreadable characters
    trendsReturn = authTwo.trends_place(2450022)
    print("Printing out Trends now boss: ")
    for item in trendsReturn[0]["trends"]:
        print(item['name'])