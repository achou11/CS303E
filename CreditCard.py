#  File: CreditCard.py

#  Description: This program determines whether a 15 or 16-digit credit card number is valid or not.

#  Student Name: Andrew Chou

#  Student UT EID: aoc349

#  Course Name: CS 303E

#  Unique Number: Morning (50860)

#  Date Created: 4/6/16

#  Date Last Modified: 4/8/16

#Function to check if input is appropriate length
def is_valid(cc_num):
  if(len(str(cc_num)) == 15) or (len(str(cc_num)) == 16):
    return True 
  else:
    return False

#Function to determine type of credit card
def cc_type(cc_num):
    if (cc_num[0] == "3" and cc_num[1] == "4") or (cc_num[0] == "3" and cc_num[1] == "7"):
        card_type = "American Express"
    
    elif cc_num[0] == "6" and (cc_num[1:4] == "011" or cc_num[1:3] == "44" or cc_num[1] == 5):
        card_type = "Discover"
    
    elif cc_num[0] == "5" and (cc_num[1] == "0" or cc_num[1] == "1" or cc_num[1] == "2" or cc_num[1] == "3" or cc_num[1] == "4" or cc_num[1] == "5"):
          card_type = "MasterCard"
    
    elif cc_num[0] == "4":
        card_type = "Visa"
    
    else:
        card_type = ""
    
    return card_type
        


def eval_ccNUM(cc_num):
    
    #Convert input string into list
    cred_list = list(cc_num)
    use_list = []
    
    for i in cred_list:
        a = int(i)
        use_list.append(a)
    
    #Create empty lists for odd and even digits
    odd_list = []
    even_list = []
    
    #Use Luhn's Test to evaluate credit card number
    
    #Add odd digits into odd list, and even digits into even list
    for i in range(len(cc_num)-2, -1, -2):
        odd_list.append(use_list[i])
    
    for j in range (len(cc_num)-1, -1, -2):
        even_list.append(use_list[j])
    
    #Multiply each element in odd list by 2
    new_odd_list = []
    for k in odd_list:
        k *= 2
        new_odd_list.append(k)
    
    
    #Sum up digits in the odd list
    sum_odd = 0
    for dig in new_odd_list:
        if dig >= 10:
            sum_digits = (dig // 10) + (dig % 10)
            sum_odd += sum_digits
        else:
            sum_odd += dig
    
    #Sum up digits in even list
    sum_even = 0
    for digi in even_list:
        sum_even += digi
    
    #Get the sum of the digits from the odd list and the digits of the even list
    tot_sum = sum_odd + sum_even
    
    #Check to see if sum is divisible by 10. If so, input is valid credit card number.
    
    if tot_sum % 10 == 0:
        check_cred = True
        
    else:
        check_cred = False
        
    return check_cred
        

def main():
    
    #Ask user to enter credit card number
    ask_card = int(input("Enter 15 or 16-digit credit card number: "))
    
    #Check if input is valid length
    if is_valid(ask_card) == False:
        print ("Not a 15 or 16-digit number")
        return 
    
    cc_num = str(ask_card)
    
    cctype = cc_type(cc_num)
    
    eval_card = eval_ccNUM(cc_num)
    
    #Print out appropriate statement
    
    if eval_card == True:
        if cctype == "":
          print ("Valid credit card number")
        else:
          print ("Valid " + cctype + " credit card number")
        
    else:
        print ("Invalid credit card number")


main()
    
    