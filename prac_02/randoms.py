"""
Random Numbers
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1. What was the smallest number you could have seen, what was the largest?
# The smallest number was 5 and the largest was 20.

# 2. What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# The smallest number was 3 and the largest was 9.
# No. The possible outcomes would be 3,5,7,9.

# 3. What was the smallest number you could have seen, what was the largest?
# The smallest and largest number I could have seen was 2.6357812410700614 and 5.486334861048834 respectively.

# 4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

# the alternative way using 'from random import *'
from random import *

print(randint(5, 20))
print(randrange(3, 10, 2))
print(uniform(2.5, 5.5))
