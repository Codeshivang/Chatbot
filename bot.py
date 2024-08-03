# creating a chatbot for a randome payment app 
print("hello !")
print("I am andrew from worldPay, where you are geting problem")

#the issues

a = print("a = payment issues !")
b = print("b = profile & payment !")
c = print("c = money Transfer !")
d = print("d = recharge & bill payment !")

problem = print(input("enter your problem:"))


# payment issues 
if problem == a:
   a1 = print(" a1 = issue with failed payments")
   a2 = print(" a2 = issue with payments made to merchant")
   a3 = print(" a3 = issue with sucessful payments")

   problem_a = print (input("enter your option: ")) 
#issue with failed payments
   if problem_a == a1:
     a1_1 = print("a1_1 = why did my UPI payment fail ?")
     a1_2 = print("a1_2 = why is my money deducted for my failed payment ?")
#issue with payments made to merchant
   elif problem_a==a2:
      a2_1 = print("a2_1 = what if i have paid twice to an order or booking ?")
      a2_2 = print("a2_2 = what if the order or booking is not confirmed ?")
#issue with sucessful payments
   elif problem_a==a3:
      a3_1 = print("a3_1 = how does the reciver know into which account the money is deposited ?")
      a3_2 = print("a3_2 = what if the money is not deposited into the receiver's account after 5 days?")
#the else one 
   else:
      print("you can contact our costomer care - ''9411736***'' ")



#profile and payment 
elif problem == b:
   b1 = print("b1 = my worldPay profile")
   b2 = print("b2 = payment method")

   problem_b = print (input("enter your option: ")) 
#my phonePe profile
   if problem_b == b1:
     b1_1 =  print("b1_1 = personal detail")
     b1_2 =  print("b1_2 = my acc detail")
     b1_3 =  print("b1_3 = saved addresses")
     b1_4 =  print("b1_4 = kyc")
#my payment method 
   elif problem_b==b2:
     b2_1 =  print("b2_1 = UPI")
     b2_2 =  print("b2_2 = bank acc")
     b2_3 =  print("b2_3 = worldPay gift card")
#the else statements
   else:
      print("you can contact our costomer care - ''9411736***'' ")



#money Transfer
elif problem == c:
   c1 = print("c1 = send money")
   c2 = print("c2 = send message")
   c3 = print("c3 = UPI international")

   problem_c = print (input("enter your option: ")) 
#send money 
   if problem_c == c1:
     c1_1 =  print( "c1_1 = can i send money using my wallet balance?")
     c1_2 =  print("c1_2 = what if i faced an issue with a payment?")
     c1_3 =  print("c1_3 = can i cancel a payment?")
#send message
   elif problem_c==c2:
     c2_1 =  print("c2_1 = can I send an attachment to a contact?")
     c2_2 =  print("c2_2 = can i delet mesage and chat history?")
     c2_3 =  print("c2_3 = how do i block user?")
#UPI international
   elif problem_c==c3:
     c3_1 =  print("c3_1 = can I cancel a UPI International payment?")
     c3_2 =  print("c3_2 = how do i detactive UPI International")
# the else statements
   else:
      print("you can contact our costomer care - ''9411736***'' ")



#recharge and bill payments
elif problem == d:
   d1 = print(" d1 = bill payments")
   d2 = print("d2 = recharge")
   d3 = print("d3 = purchase")

   problem_d = print (input("enter your option: ")) 
#bill payments
   if problem_d == d1:
     d1_1 = print("d1_1 = electric bill")
     d1_2 = print("d1_2 = rent payments")
     d1_3 = print("d1_3 = cable tv")
     d1_4 = print("d1_4 = credit card")
#recharge
   elif problem_d==d2:
     d2_1 = print("d2_1 = postpaid recharge")
     d2_2 = print("d2_2 = DTH Recharge")
     d2_3 = print("d2_3 = fast tag")
     
#purchase
   elif problem_d==d3:
      d3_1 = print(" d3_1 = gold")
      d3_2 = print(" d3_2 = gift cards")
      d3_3 = print(" d3_3 = google play ")
      d3_4 = print(" d3_4 = app store code")
     
#the else statements
   else:
      print("you can contact our costomer care - ''9411736***'' ")


#the last else statement
else:
    print("you can contact our costomer care - ''9411736***'' ")

#thanking
print("thankyou user :)")
