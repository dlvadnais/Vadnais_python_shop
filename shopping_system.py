# shopping_system.py

import random

class Store:
    def __init__(self, name):
        self.name = name
        self.reputation = random.uniform(3.0, 5.0)  # We give it a reputation between 3.0 and 5.0
        self.cost_factor = random.uniform(50, 150)  # The cost factor is set between $50 and $150

    def get_store_info(self):
        """Print store information."""
        print(f"{self.name} - Reputation: {self.reputation:.2f}, Cost Factor: ${self.cost_factor:.2f}")


class Person:
    def __init__(self, name):
        self.name = name
        self.budget = random.uniform(50, 200)  # Budget is randomly set between $50 and $200

    def decide_store(self, stores):
        """Decide where to shop based on reputation and cost."""
        eligible_stores = [store for store in stores if store.cost_factor <= self.budget]

        if not eligible_stores:
            print(f"Oops! {self.name} with a budget of ${self.budget:.2f} couldn't find any stores within budget.")
            return

        best_store = max(eligible_stores, key=lambda store: store.reputation / store.cost_factor)

        print(f"{self.name} with a budget of ${self.budget:.2f} decided to check out {best_store.name}.")


