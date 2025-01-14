# Author   : Haluk Yuzukirmizi
# Email    : hyuzukirmizi@umass.edu
# Spire ID : 34419060

class VendingMachine:
    def __init__(self,balance=0,total_sales=0,history=[],historycost={}):
        self.items_list= {}
        self.balance= balance
        self.total_sales= total_sales
        self.history=history
        self.historycost=historycost

    def list_items(self):
        if self.items_list=={}:
            print('No items in the vending machine')
        else:
            print('Available items:')
            sorted_list = sorted(self.items_list)
            for dict in sorted_list:
                print(f"{dict} (${self.items_list[dict]['cost']}): {self.items_list[dict]['num']} available")
    def add_item(self,name,price,quantity):
        if name in self.items_list.keys():
            total=quantity+self.items_list[name]['num']
            (self.items_list[name])=({'cost': price,
                                            'num':total})
        else:
           self.items_list[name]= {'cost':price,
                                   'num':quantity} 
        print(f"{quantity} {name}(s) added to inventory")

    def insert_money(self,dollar):
        if dollar== 1 or dollar== 2 or dollar== 3:
            self.balance+=dollar
            self.balance=round(self.balance,2)
            print(f'Balance: {self.balance}')
        else:
            print('Invalid amount')
    def purchase(self,name):
        if name not in self.items_list.keys():
            print('Invalid item')
        elif self.items_list[name]['num']==0:
            print(f'Sorry {name} is out of stock')
        elif self.items_list[name]['cost']>self.balance:
            print(f'Insufficient balance. Price of {name} is {self.items_list[name]["cost"]}')
        else:
            self.items_list[name]['num']-=1
            self.balance-=self.items_list[name]['cost']
            round(self.balance,2)
            print(f'Purchased {name}')
            print(f'Balance: {self.balance}')
            self.total_sales+=self.items_list[name]['cost']
            self.total_sales=round(self.total_sales,2)
            self.history.append(name)
            self.historycost[name]=self.items_list[name]['cost']



    def display_change(self):
        if self.balance==0:
            print('No change')
        else:
            print(f'Change: {self.balance}')
            self.balance=0
    def get_item_price(self,name):
        if name not in self.items_list.keys():
            print('Invalid item')
        else:
            return self.items_list[name]['cost']
    def empty_inventory(self):
        self.items_list={}
        print('Inventory cleared')
    def get_total_sales(self):
        return self.total_sales
    def get_item_quantity(self,name):
        if name not in self.items_list.keys():
            print('Invalid item')
        else:
            return self.items_list[name]['num']
    def remove_item(self,name):
        if name not in self.items_list.keys():
            print('Invalid item')
        else:
            self.items_list.pop(name)
            print(f'{name} removed from inventory')
    def stats(self,N):
        purchase=len(self.history)
        if purchase<N:
            print(f'Sale history for the most recent {purchase} purchase(s):')
            for items in sorted(set(self.history)):
                count=0
                for name in self.history:
                    if name==items:
                        count+=1
                print(f'{items}: ${count*self.historycost[items]} for {count} purchase(s)')
        else:
            print(f'Sale history for the most recent {N} purchase(s):')
            self.history.reverse()
            sale_stat=self.history[0:N]
            for items in sorted(set(sale_stat)):
                count=0
                for name in sale_stat:
                    if name==items:
                        count+=1
                print(f'{items}: ${count*self.historycost[items]} for {count} purchase(s)')



vm = VendingMachine()
vm.add_item("Cjasch", 0.11, 20)
vm.add_item("Hsackmcs", 1.04, 25)
vm.add_item("Bsajc", 1.98, 30)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.insert_money(1)
vm.purchase('Cjasch')
vm.purchase('Hsackmcs')
vm.purchase('Bsajc')
vm.purchase('Bsajc')
vm.purchase('Bsajc')
vm.empty_inventory()
vm.stats(3)