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
