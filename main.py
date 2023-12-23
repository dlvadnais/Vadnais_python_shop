#as03 shopping system David Vadnais
# main.py

from shopping_system import Store, Person

if __name__ == "__main__":
    # Dropping in at random stores with vibes
    store1 = Store("Mc ronalds")
    store2 = Store("floormart")
    store3 = Store("arkenanian tire")

    # Our adventurous shopper with a budget
    shopper = Person("dave")

    # Displaying store information
    store1.get_store_info()
    store2.get_store_info()
    store3.get_store_info()

    # Deciding where to throw some dollars
    shopper.decide_store([store1, store2, store3])

    # Interacting with the chosen store (BudgetBazaar in this case)
    
    # Introducing a special offer with a 15% discount and updating the store's cost factor
    store2.introduce_special_offer(15)

    # Personal shopper activities
    
    # Setting a new budget for Alice
    shopper.set_budget(180)

    # Sharing Alice's shopping experience at BudgetBazaar
    shopper.share_shopping_experience("BudgetBazaar")

    # Browsing online stores for more shopping options
    shopper.browse_online_stores()
