#this program is about welcoming the buyers and vendors on Amazon site in two different welcome messages.
# 1. if the customer is buyer welcome them by - welcome to buyer family message
# 2. if the customer is vendor welcome them by - welcome to vendor family message

def welcome_amazon_greet(is_buyer,name):
    print("hello "+ name )

    if(is_buyer):
        print("welcome to Amazon BUYER Family")

    else:
        print("welcome to Amazon VENDOR Family")

welcome_amazon_greet(True,"subbu")







