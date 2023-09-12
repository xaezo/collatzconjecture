import sys
import matplotlib.pyplot as plt
from conjecture import cconjecture

if len(sys.argv) == 1:
    print("Usage: python3 main.py [integer]")
    sys.exit()

#creating a sequence
sequence = cconjecture(sys.argv[1])

plt.plot([_+1 for _ in range(len(sequence))],sequence)
plt.axis([1,len(sequence), min(sequence), max(sequence)])

plt.ylabel("value")
plt.xlabel("step")

print(f"Length of sequence: {len(sequence)}")
print(f"Max: {max(sequence)}")
print(f"Min: {min(sequence)}")
plt.show()