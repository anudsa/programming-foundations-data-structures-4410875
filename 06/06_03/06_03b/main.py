#stacks using deques
from collections import deque
history=deque()
history.append("google.com")
history.append("fb.com")
history.append("x.com")
print(history)
#goin back to the latest page:
print(history[-1])
#alternatively:
print(history.pop())