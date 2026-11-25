from classes_overview_9_Exercise_Base import YouTubeChannel

'''
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
'''

# Base Test
codebasics = YouTubeChannel("codebasics")
codebasics.subscribe()
codebasics.subscribe()
codebasics.subscribe()
codebasics.unsubscribe()
codebasics.show()
