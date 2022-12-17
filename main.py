import random #bcoz we want to generate slot machine values randomly 
#we have to figure out how many items we want in a reel and how long we want each line to be 
#Entering no. of rows and columns in a slot machine
ROWS=3
COLUMNS=3


#global constant for no.of lines 
MAX_LINES=3 
#global constant for maximum  bet on each line
MAX_BET=100
#global constant for minimum  bet on each line
MIN_BET=1
#we are taking ABCD AS symbols
#for every single real we are taking 2As 4BS 6Cs and 8Ds
symbol_count={
    'A':2,#the values are symbols frequency
    'B':4,
    'C':6,
    'D':8
}
symbol_values={
    'A':2,#the values are symbols frequency
    'B':4,
    'C':6,
    'D':8}

def check_winnings(columns,bet,lines,values):
    winnings=0
    #to check want lines they won on
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_check=column[line]
            if symbol!=symbol_check:
                break
        else: #execued loop terminated by completion not break
            winnings+=values[symbol]*bet
            winnings_lines.append(line+1)
    return winnings ,winnings_lines           

def to_get_slot_machine_spin(rows,cols,symbols):
    #now we want to add all symbols in a list from where we can randomly choose symbols in each columns
    all_symbols=[]
    for symbol ,symbol_count in symbols.items(): #symbol will take dic values and symbol_count take the fre.
        #the above loop select the symbol and its fre.
        #this loop append each symbols the no. of frequencies times to list
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    #to add symbols in a column
    columns=[]  
    for _ in range(cols):
        column=[]
        current_symbol=all_symbols[:]
        for _ in range(rows) :     
            value=random.choice(current_symbol)  #we need to create a copy of a list all_symbols because after filling of each columns we lost some values so we need all values for next columns
            column.append(value)
            current_symbol.remove(value)
        columns.append(column)

    return columns
#TO display the slit 
def print_slot_machine(columns):
    for row in range(len(columns[0])): #this will select the rows like 0 ,1,..
        for i,column in enumerate(columns):#this gives the index and item also
            if i!=len(columns)-1:
                print(column[row],end=" | ")#we want print | except the first ke pahle and last row ke baad
            else:
                print(column[row],end="")#we want print | except the first ke pahle and last row ke baad

        print()#this empty print statement brings to new line every next row






#function to take users deposit
def deposit():
    while True: #I am using while loop here because i want user to keep depositing  amount until they enter a valid deposit amount 
        amount=input("What would you like to deposit? $ ")
        #to check whether the entered amount is valid or not if it is valid we proceed 
        # otherwise went to condition statemnt like if they entered negative numbers or strings  it will not taken
        if amount.isdigit():#fails for -ve numbers also
            amount=int(amount)#if amount is valid convert it into int  
            if amount>0:
                break #if amount is greter than zero it is what needed
            else:
                print("The amount must be greater than 0 .")
        else:
            print("Enter a number ")
    
    return amount 
# funtion to enter no. of lines we gonna bet on and then we gonna multiply bet amount  with no. of lines 
def get_number_of_lines():
    while True: 
        lines=input("Enter the no. of lines you want to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():#fails for -ve numbers and strings
            lines=int(lines)#if amount is valid convert it into int  
            if 1<=lines<=MAX_LINES:# OR lines>0 and lines<=MAX_LINES:
                break 
            else:
                print("Enter a valid no. of lines .")
        else:
            print("Enter a number ")
    
    return lines
#here in this function we gonna take the bet amount on each line  from the user 
def get_bet():
    while True: 
        amount=input("What would you like to bet on each line ? $ ")
        if amount.isdigit():#check if the string entered is a collection digits or not
            amount=int(amount)#if amount is valid convert it into int  
            if MIN_BET<=amount<=MAX_BET:
                break #if amount is greter than zero it is what needed
            else:
                #print("Amount must be between ("+str(MIN_BET)+"-"+str(MAX_BET)+").")#OR Another way to add variables in string
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")#f will convert values in {} in string
        else:
            print("Enter a number ")
    
    return amount 
#to make game runutimateltly
def spin(Balance):
    
    lines= get_number_of_lines()
    #the total bet must be within there balance it cannot be beyond balance 
    while True:

        bet=get_bet()
        total_bet=bet*lines
        if total_bet>Balance:
            print(f"You donot have enough money to bet ,You are current balance is ${Balance} ")
        else:
            break    
    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to ${total_bet}")
    #print(Balance,lines)
    slots=to_get_slot_machine_spin(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_line=check_winnings(slots,bet,lines,symbol_values)
    print(f"You Won ${winnings}.")
    print(f"You won on lines ",*winnings_line) #this * isgoing to pass all the values of winning_lines 
    return winnings-total_bet #this will tell how much win or lose
    



def main():                   
    #CALLING A FUNCTION
    Balance=deposit() #storing returned value of function to amount
    while True:
        print(f"Your current balance is ${Balance} ")
        spinc=input("press enter to spin or (q to quit ) :")
        if spinc=='q':
            break #it will end the game
        else:
            Balance+=spin(Balance)
    print(f"You left with {Balance}")
main()    

