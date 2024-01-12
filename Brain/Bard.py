from bardapi import BardCookies

import datetime

cookie_dict ={
    "__Secure-1PSID" : "fQgRan34QmLw3utzZj2NOsEIX9v9yp0F1PDxbhZrxNC_r7mdzekB_0ktpkYQbqU265wHuw.",
    "__Secure-1PSIDTS" : "sidts-CjEBPVxjSmsO0ONeyMr7zhGBWiv1-R-JUusVLI4uWKz_3QsjY7UnSY8ZGc57wBFnwHJ6EAA",
    "__Secure-1PSIDCC" : "ABTWhQHERytmxEMFrrcMw5K7mVr4R64xFmSnNWFQwsrembFWuCI2ab7L8GO17C87NGdQlJ8A"
    
}

bard= BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter  your query : ")
    Reply =bard.get_answer(Query)['content']
    print(Reply)
