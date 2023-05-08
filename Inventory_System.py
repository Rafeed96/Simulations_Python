import numpy as np
import matplotlib.pyplot as plt

M = int(input())
N = int(input())


beginning_inventory = 3  # must be initialized
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8  # must be initialized
days_until_arrival = 2  # must be initialized


np.random.seed(1)
shortage_day_count = 0
avg_ending = 0
end_Graph = []
days = []


for cycle in range(10):
    print("Cycle no: ", cycle)
    for day in range(1, N+1):
        print("Day no: ", day)

        days_until_arrival = days_until_arrival - 1

        # calculate beginning_inventory, consider arrival of orders placed
        if days_until_arrival < 0:
            beginning_inventory = beginning_inventory + order_quantity
            order_quantity = 0

        daily_demand = np.random.choice(a=[0, 1, 2, 3, 4, 5], p=[
                                        0.10, 0.15, 0.25, 0.25, 0.15, 0.10])  # edit according to the spec

        # update total_demand using daily demand
        total_demand = daily_demand + shortage_quantity

        if total_demand > beginning_inventory:
            # shortage occurs
            # Update -> shortage_quantity, ending_inventory
            shortage_quantity = total_demand - beginning_inventory
            ending_inventory = 0
            end_Graph.append(ending_inventory)
            avg_ending = avg_ending + ending_inventory
            shortage_day_count = shortage_day_count + 1
            temp = beginning_inventory
        else:
            shortage_quantity = 0
            ending_inventory = beginning_inventory - total_demand
            avg_ending = avg_ending + ending_inventory
            end_Graph.append(ending_inventory)
            print("")
            # No shortage
            # Update -> shortage_quantity, ending_inventory

        print("Beginning Inventory: ", beginning_inventory)
        print("Daily Demand: ", daily_demand)
        print("Ending Inventory: ", ending_inventory)
        print("Shortage Quantity: ", shortage_quantity)
        print("")
        print("")
        beginning_inventory = ending_inventory

        # Code for review day
        # beginning_inventory = beginning_inventory - total_demand
        if (day == N):
            # calculate order_quantity using M, ending_inventory, shortage_quantity
            order_quantity = (M - ending_inventory) + shortage_quantity
            # sample days_until_arrival value (similar to daily_demand sampling)

            days_until_arrival = np.random.choice(
                a=[1, 2, 3, 4], p=[0.50, 0.35, 0.10, 0.05])  # edit according to the spec

            if days_until_arrival > 2:
                order_quantity = order_quantity + 3
