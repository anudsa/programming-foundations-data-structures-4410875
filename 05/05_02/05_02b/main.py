from collections import deque 
playlistOrder = deque()
#Adding songs
playlistOrder.append("Rosa Pastel")
playlistOrder.append("Como nadie")
playlistOrder.append("tap twice")
for item in playlistOrder:
  print(item)
#popleft to remove an item from the beginning of the queue
playlistOrder.popleft()
print(playlistOrder)
playlistOrder.append("emotions and math")
print(playlistOrder)