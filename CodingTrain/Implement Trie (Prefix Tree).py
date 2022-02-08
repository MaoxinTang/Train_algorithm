class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
		# The idea is to insert words in a linked fashion. For example "cars" will be inserted as
		# {'c':{'a':{'r':{'s':{}}}}
        for w in word:
          if w not in t:
            t[w] = {}
          t = t[w]
		# Another key named "end" will distinguish that the word  "cars" actually exists
		# Without the end key it simply means that the traversed part is just prefix
        t["end"] = True 

    def search(self, word: str) -> bool:
        t = self.trie
		# Traverse through the word
        for w in word:
          if w in t:
            t = t[w]
          else:
            return False
		# As the end key denotes the existence of the word
        return "end" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
		# Traverse through the word
        for w in prefix:
          if w in t:
            t = t[w]
          else:
            return False
		# Here it is okay to find whether we had traversed the entire prefix or not
        return True