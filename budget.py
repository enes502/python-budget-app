class Category:

    def __init__(self,name):

        self.name=name

        self.ledger= []



    def deposit(self,amount,description=""):

        self.ledger.append({'amount':amount,'description': description})

    

    def get_balance(self):

        self.current_balance=0

        for spend in self.ledger:

            self.current_balance += spend['amount']

        return self.current_balance

    def check_funds(self,amount):

        if self.get_balance()>= amount:

            return True

        else:

            return False     

    

    def withdraw(self,amount,description=""):    

        if self.check_funds(amount):

            self.ledger.append({'amount':-amount,'description':description})

            return True 

        else:

            return False

    def transfer(self,amount,category):

        if self.check_funds(amount):

            self.withdraw(amount,f"Transfer to {category.name}")

            category.deposit(amount,f"Transer from {self.name}")

            return True

        else:

            return False

    def __str__(self):

        category_name="Food"

        text= f"{category_name:*^30}\n"

        for spend in self.ledger:

            short_desc = spend['description'][:23]

            text+= f"{short_desc:<23}{spend['amount']:>7.2f}\n"

        text+= f"Total: {self.get_balance()}\n"

        return text

        

        

food = Category('Food')

food.deposit(1000, 'initial deposit')

food.withdraw(10.15, 'groceries')

food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')

food.transfer(50, clothing)

print(food)     



def create_spend_chart(categories):

    

    spent_amounts = []

    for category in categories:

        spent = 0

        for item in category.ledger:

            if item['amount'] < 0:

                spent += abs(item['amount'])

        spent_amounts.append(spent)

    

    total_spent = sum(spent_amounts)

    

   

    percentages = []

    for spent in spent_amounts:

        if total_spent == 0:

            percentages.append(0)

        else:

            

            percentages.append(int((spent / total_spent) * 100 // 10) * 10)

            

    

    chart = "Percentage spent by category\n"

    

   

    for i in range(100, -1, -10,):

        chart += f"{i:>3}|"

        for percent in percentages:

            if percent >= i:

                chart += " o "

            else:

                chart += "   "

        chart += " \n" 

        

    

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    

    

    max_len = max([len(cat.name) for cat in categories])

    names = [cat.name.ljust(max_len) for cat in categories]

    

    for i in range(max_len):

        chart += "    "

        for name in names:

            chart += f" {name[i]} "

        chart += " "

        if i < max_len - 1:

            chart += "\n"

            

    return chart



food = Category('Food')

food.deposit(1000, 'initial deposit')

food.withdraw(60, 'groceries') 



clothing = Category('Clothing')

clothing.deposit(500, 'initial deposit')

clothing.withdraw(20, 'clothes')



auto = Category('Auto')

auto.deposit(500, 'initial deposit')

auto.withdraw(10, 'gas')





print(create_spend_chart([food, clothing, auto]))
