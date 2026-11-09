# Q13. Cheapest Flights Within K Stops
# Find the cheapest flight price with at most k stops.

n = 4

flights = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 100],
    [1, 3, 600],
    [2, 3, 200]
]

src = 0
dst = 3
k = 1

# Set the initial distance of every city to infinity.
distance = [float('inf')] * n

# The source city has zero cost.
distance[src] = 0

# At most k stops means at most k + 1 flights.
for i in range(k + 1):

    # Make a copy so that each round uses only previous-round values.
    temp = distance.copy()

    for start, end, price in flights:

        if distance[start] != float('inf'):

            new_price = distance[start] + price

            if new_price < temp[end]:
                temp[end] = new_price

    distance = temp

# Display the cheapest price.
if distance[dst] == float('inf'):
    print("Cheapest Price:", -1)
else:
    print("Cheapest Price:", distance[dst])