class VendingMachine:
    def __init__(self):
        # Lists
        self.acceptMoney = [10000, 5000, 2000, 1000, 500, 200, 100]
        self.products    = ['CrunchyBar', 'SpurtCoke', 'MethCandy', 'IceCream']
        
        # Price dict
        self.price = {
            'CrunchyBar' : 2000, 
            'SpurtCoke'  : 5000, 
            'MethCandy'  : 3000, 
            'IceCream'   : 4000,
        }
        
        # STock Dict
        self.stock = {
            'CrunchyBar' : 5, 
            'SpurtCoke'  : 3, 
            'MethCandy'  : 4, 
            'IceCream'   : 0,
        }
        
        # User defined variables
        self.storedMoney = 0
        self.chosenProduct = ''
        self.change = 0
    
    # Display the list of products followed by the price and available stock
    def displayUI(self):
        print('========================================================')
        print('Le Vendinger Machiner')
        print('========================================================')
        print('No.\tProduct Name\tPrice and Stock')
        print('--------------------------------------------------------')
        for i in range(len(self.products)):
            prodName = self.products[i]
            print(f"{i+1}.\t{prodName}\tRp{self.price[prodName]:,} ({self.stock[prodName]} in stock)")
        print('========================================================')
    
    def error(self, message, callback = print):
        print('--------------------------------------------------------')
        print(f'ERROR: {message}')
        print('--------------------------------------------------------')
        print('========================================================')
        callback()
    
    def chooseProduct(self):
        print('\n========================================================')
        user = input("Please choose a product (type number of product): ")
        if user.isnumeric():
            selection = int(user)
            if selection > 0 and selection <= len(self.products):
                product = self.products[selection - 1]
                if self.stock[product] > 0:
                    self.chosenProduct = product
                    print('--------------------------------------------------------')
                    print(f'Product Selected: {self.chosenProduct} - Rp{self.price[self.chosenProduct]:,}')
                    print('--------------------------------------------------------')
                else:
                    self.error('Product out of stock', self.chooseProduct)
            else:
                self.error('Product number not in list', self.chooseProduct)
        else:
            self.error('Invalid input', self.chooseProduct)
    
    def getMoney(self):
        price = self.price[self.chosenProduct]
        print('\n========================================================')
        print(f'You want {self.chosenProduct}? Feed me money! (Rp{self.storedMoney} out of Rp{price})')
        print('I accept Rp10000, Rp5000, Rp2000, Rp1000, Rp500, Rp200, and Rp100')
        user = input("Money Input: ")
        
        if user.isnumeric():
            money = int(user)
            if money in self.acceptMoney:
                self.storedMoney += money
                if self.storedMoney >= price:
                    self.change = self.storedMoney - price
                    self.stock[self.chosenProduct] -= 1
                    print('--------------------------------------------------------')
                    if self.change > 0: print(f"I'm full! Here's your change: Rp{self.change:,}")
                    else: print(f"I'm full!")
                    print('--------------------------------------------------------')
                    print('========================================================')
                else:
                    print('========================================================')
                    self.getMoney()
            else:
                self.error('I dont accept that!', self.getMoney)
        else:
            self.error('Invalid input', self.getMoney)
    
    def calChange(self):
        print('\n========================================================')
        coins = self.acceptMoney[3:]
        coin_amount = {}
        for coin in coins:
            numOfCoins = self.change // coin
            coin_amount[coin] = numOfCoins
            self.change -= numOfCoins * coin
        
        print('I will give you...')
        print(f'1 x {self.chosenProduct}')
        for coin, num in coin_amount.items():
            if num > 0: print(f'{num} x Rp{coin:,}')
        print('========================================================')
        
    def run(self):
        self.displayUI()
        self.chooseProduct()
        self.getMoney()
        self.calChange()
        
        print('========================================================')
        user = input("Do you want to use Le Vendinger Machiner again? (type 'y' if yes) ")
        if user.upper() == 'Y':
            print('Re-running Le Vendinger Machiner...')
            print('========================================================')
            VendingMachine().run()
        else:
            print('Thank you for using Le Vendinger Machiner!')
            print('========================================================')
            exit(0)
    
if __name__ == '__main__':
    VendingMachine().run()
