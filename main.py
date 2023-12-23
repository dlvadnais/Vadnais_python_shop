# main.py

from shopping_system import Store, Person

if __name__ == "__main__":
    # Creating stores with random reputations and cost factors
    store1 = Store("SuperMart")
    store2 = Store("BudgetBazaar")
    store3 = Store("LuxuryGrocers")

    # Creating a person with a random budget
    shopper = Person("Alice")

    # Displaying store information
    store1.get_store_info()
    store2.get_store_info()
    store3.get_store_info()

    # Deciding where to shop
    shopper.decide_store([store1, store2, store3])
