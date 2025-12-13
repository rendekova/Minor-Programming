# due 50
due = 50
# have paid 0
received = 0

# repeat asking until have paid > 50
while received < due:
    print(f"Amount Due: {due - received}")
# ask for a coin
    coin = input("Insert Coin: ")
    coin = int(coin)

# check if coin in [5, 10, 25]
    if not coin in [5, 10, 25]: continue
# if not: ignore
# # calculate the amount due
    received += coin



# at the end
# print how much change owed
print(f"Change owed: {received - due}")


