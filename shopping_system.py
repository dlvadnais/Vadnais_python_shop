#as03 shopping system David Vadnais
# shopping_system.py

import random

class Store:
    def __init__(self, name):
        self.name = name
        self.reputation = random.uniform(3.0, 5.0)  # The store's rep is somewhere between decent and awesome
        self.cost_factor = random.uniform(50, 150)  # They've got prices ranging from wallet-friendly to a bit fancy

    def get_store_info(self):
        """Print store information."""
        print(f"Welcome to {self.name}! Reputation: {self.reputation:.2f}, Cost Factor: ${self.cost_factor:.2f}")

    def introduce_special_offer(self, discount_percent):
        """Introduce a special offer with a given discount percentage."""
        print(f"🌟 Special Offer at {self.name}! {discount_percent}% off on selected items! 🌟")
        
        # Reduce the store's cost factor by the discount percentage
        self.cost_factor -= (self.cost_factor * discount_percent / 100)

    def ask_for_feedback(self):
        """Ask customers for feedback about their shopping experience."""
        print(f"Hey shoppers! We'd love to hear your thoughts about {self.name}. Share your feedback with us!")

class Person:
    def __init__(self, name):
        self.name = name
        self.budget = random.uniform(50, 200)  # Rocking a budget between a coffee date and a nice dinner out

    def decide_store(self, stores):
        """Decide where to shop based on vibes and budget."""
        eligible_stores = [store for store in stores if store.cost_factor <= self.budget]

        if not eligible_stores:
            print(f"Uh-oh! {self.name} with ${self.budget:.2f} couldn't find any stores within budget.")
            return

        best_store = max(eligible_stores, key=lambda store: store.reputation / store.cost_factor)

        print(f"{self.name} with ${self.budget:.2f} decided to check out {best_store.name}. Let's do this!")

    def set_budget(self, new_budget):
        """Set a new budget for the person."""
        self.budget = new_budget
        print(f"{self.name} adjusted their budget. New budget: ${self.budget:.2f}")

    def share_shopping_experience(self, store_name):
        """Share the shopping experience at a specific store."""
        print(f"Just came back from {store_name}! Great vibes, and my budget didn't take a big hit. Recommended!")

    def browse_online_stores(self):
        """Explore online stores for more shopping options."""
        print(f"{self.name} is exploring online stores for some virtual window shopping. Any recommendations?")
