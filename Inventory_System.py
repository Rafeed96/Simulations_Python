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
