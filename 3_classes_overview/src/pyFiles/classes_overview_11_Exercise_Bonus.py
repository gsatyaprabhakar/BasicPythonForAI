'''
## 🏋️ Exercise: The `YouTubeChannel` class

Time to build your own blueprint! Create a class `YouTubeChannel` that models a channel's subscribers.

Your class should have:
1. `__init__(self, name)` — store the channel `name` and start `subscribers` at `0`.
2. `subscribe(self)` — add 1 subscriber and print `"Thanks for subscribing! Total: <count>"`.
3. `unsubscribe(self)` — remove 1 subscriber (but never go below 0!) and print the new total.
4. `show(self)` — print `"<name> has <count> subscribers"`.

Then test it:
```python
codebasics = YouTubeChannel("codebasics")
codebasics.subscribe()
codebasics.subscribe()
codebasics.subscribe()
codebasics.unsubscribe()
codebasics.show()
```

Expected output (roughly):
```
Thanks for subscribing! Total: 1
Thanks for subscribing! Total: 2
Thanks for subscribing! Total: 3
Total: 2
codebasics has 2 subscribers
```

**Bonus:** create a *second* channel and subscribe to it a few times — confirm its count is completely independent from the first one (just like the two phones). 🔔
'''

class YouTubeChannel:

    def __init__(self, name):
        self.name = name
        self.subscriber = 0

    def subscribe(self):
        self.subscriber += 1
        print(f"Thanks for subscribing  {self.name} ! Total: {self.subscriber}")

    def unsubscribe(self):
        # check before decrementing to avoid negative subscribers
        # Print error message if trying to unsubscribe when there are no subscribers
        if self.subscriber > 0:
            self.subscriber -= 1
        else:
            print("Error: Cannot unsubscribe. No subscribers.")
        print(f"Ubscribed {self.name} ! Total: {self.subscriber}")

    def show(self):
        print(f"{self.name} has {self.subscriber} subscribers")
