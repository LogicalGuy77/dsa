strength = [7, 3, 6, 18, 22, 50]
K = 4
x = 1  # Initial multiplier
gates = len(strength)  # Number of locks
time = 0  # Time tracker
energy = 0  # Sword energy


def largest_less_than_k_with_index(lst, k):
    largest = None
    largest_index = -1

    for i, num in enumerate(lst):
        if num <= k and (largest is None or num > largest):
            largest = num
            largest_index = i

    return largest_index


while gates > 0:
    time += 1
    energy += x

    # Find the largest lock that can be opened with current energy
    largest_ind = largest_less_than_k_with_index(strength, energy)
    if largest_ind != -1:
        # Open the lock
        x += K
        energy = 0  # Reset energy after breaking lock
        gates -= 1
        strength[largest_ind] = float('inf')

print(time)