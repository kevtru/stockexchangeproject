
# account class.
class Account:
   next_id = 1000




   def __init__(self, first_name='', last_name='', email=''):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.user_id = Account.next_id
       Account.next_id += 1




   def __str__(self):
       return f"ID: {self.user_id} | Name: {self.first_name} {self.last_name} | Email: {self.email}"








# store all the created accounts here:
accounts = []




# create function
def create_account():
   first_name = input("Enter first name: ")
   last_name = input("Enter last name: ")
   email = input("Enter email: ")




   new_account = Account(first_name, last_name, email)
   accounts.append(new_account)




   print("\nAccount created successfully!")
   print(new_account)




bids = []
class Bidding():
    def __init__(self, stock_name, price, amount, user_id):
        self.stock_name = stock_name
        self.price = price
        self.amount = amount
        self.user_id = user_id
        
    def __str__(self):
        return (f'User ID: {self.user_id} | Stock name: {self.stock_name} | Bidding price: {self.price} | Amount: {self.amount}')
        
def make_bid():
    if not accounts:
        print('You must create an Account')
        create_account()
        
    else:
        
        user_id = input('Enter user ID: ')
        stock_name = input('Enter stock name: ')
        price = float(input('Enter bid price: '))
        amount = int(input('Enter bid amount: '))
    
        bid = Bidding(stock_name, price, amount, user_id)
        bids.append(bid)
    
        print(bid)
        match()








asks = []
class Asking():
    def __init__(self, stock_name, price, amount, user_id):
        self.stock_name = stock_name
        self.price = price
        self.amount = amount
        self.user_id = user_id
        
    def __str__(self):
        return (f'User ID: {self.user_id} | Stock name: {self.stock_name} | Asking price: {self.price} | Amount: {self.amount}')
        
def make_ask():
    if not accounts:
        print('You must create an Account')
        create_account()
        
    else:
        
        user_id = input('Enter user ID: ')
        stock_name = input('Enter stock name: ')
        price = float(input('Enter asking price: '))
        amount = int(input('Enter asking amount: '))
    
        ask = Asking(stock_name, price, amount, user_id)
        asks.append(ask)
        match()








def view_accounts():
   if not accounts:
       print("No accounts created yet.")
   else:
       print("\n--- All Accounts ---")
       for acc in accounts:
           print(acc)




#matching logic
def match():
    trade_amount = 0
    for bid in bids:
        for ask in asks:
            if bid.stock_name == ask.stock_name and bid.price >= ask.price and bid.amount > 0 and ask.amount > 0 :
               
                if bid.amount == ask.amount:
                    trade_amount = bid.amount
                    print(f'{trade_amount} order(s) successfully has been exectued at {bid.price}')
                    with open('stock_exchange.txt', 'w') as wf:
                        wf.write(f'Stock Name: {bid.stock_name}\nNumber of Orders: {trade_amount}\nExecution Price: {bid.price}\nBidding User ID: {bid.user_id}\nAsking User ID: {ask.user_id}')
                    del bid
                    del ask
                    
                elif bid.amount > ask.amount:
                    bid.amount = bid.amount - ask.amount
                    trade_amount = ask.amount
                    print(f'{trade_amount} order(s) successfully has been exectued at {bid.price}')
                    with open('stock_exchange.txt', 'w') as wf:
                        wf.write(f'Stock Name: {bid.stock_name}\nNumber of Orders: {trade_amount}\nExecution Price: {bid.price}\nBidding User ID: {bid.user_id}\nAsking User ID: {ask.user_id}')
                    del ask.amount
                    
                elif ask.amount > bid.amount:
                    ask.amount = ask.amount - bid.amount
                    trade_amount = bid.amount
                    print(f'{trade_amount} order(s) successfully has been exectued at {bid.price}')
                    with open('stock_exchange.txt', 'w') as wf:
                        wf.write(f'Stock Name: {bid.stock_name}\nNumber of Orders: {trade_amount}\nExecution Price: {bid.price}\nBidding User ID: {bid.user_id}\nAsking User ID: {ask.user_id}')
                    del bid.amount
            




#main menu
def menu():
   print("\n===== Automated Stock Exchange =====")
   print("a. Create an account")
   print("b. Make a stock bid")
   print("c. Make a stock ask")
   print("d. View all accounts")
   print("e. Exit")








# main program
def main():
   while True:
       menu()
       choice = input("Choose an option: ").lower()




       if choice == 'a':
           create_account()




       elif choice == 'b':
           make_bid()




       elif choice == 'c':
           make_ask()




       elif choice == 'd':
           view_accounts()




       elif choice == 'e':
           print("Exiting program... Goodbye!")
           break




       else:
           print("Invalid choice. Please try again.")








#run
main()

