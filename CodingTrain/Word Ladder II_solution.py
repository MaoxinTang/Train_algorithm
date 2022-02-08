Solution 1, BFS, directly store the path in queue. 318 ms, 18.7 MB
Solution 2, BFS to build graph (parents), DFS to get the shortest path, 356 ms, 20.6 MB
Solution 3, biBFS to build graph (parents), DFS to get the shortest path, 224 ms, 18.9 MB
Note that: propocessing words as below will greatly improve the algorithm speed.

# Dictionary to hold combination of words that can be formed,
# from any given word. By changing one letter at a time.
all_combo_dict = collections.defaultdict(list)
for word in wordList:
	for i in range(L):
		all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
## Solution 1
def findLadders(self, beginWord, endWord, wordList):
	if not endWord or not beginWord or not wordList or endWord not in wordList \
		or beginWord == endWord:
		return []

	L = len(beginWord)

	# Dictionary to hold combination of words that can be formed,
	# from any given word. By changing one letter at a time.
	all_combo_dict = collections.defaultdict(list)
	for word in wordList:
		for i in range(L):
			all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

	# Shortest path, BFS
	ans = []
	queue = collections.deque()
	queue.append((beginWord, [beginWord]))
	visited = set([beginWord])
	
	while queue and not ans:
		# print(queue)
		length = len(queue)
		# print(queue)
		localVisited = set()
		for _ in range(length):
			word, path = queue.popleft()
			for i in range(L):
				for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
					if nextWord == endWord:
						# path.append(endword)
						ans.append(path+[endWord])
					if nextWord not in visited:
						localVisited.add(nextWord)
						queue.append((nextWord, path+[nextWord]))
		visited = visited.union(localVisited)
	return ans
## Solution 2
def findLadders(self, beginWord, endWord, wordList):
	"""
	:type beginWord: str
	:type endWord: str
	:type wordList: List[str]
	:rtype: List[List[str]]
	"""
	if not endWord or not beginWord or not wordList or endWord not in wordList \
		or beginWord == endWord:
		return []

	L = len(beginWord)

	# Dictionary to hold combination of words that can be formed,
	# from any given word. By changing one letter at a time.
	all_combo_dict = collections.defaultdict(list)
	for word in wordList:
		for i in range(L):
			all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

	# Build graph, BFS
	# ans = []
	queue = collections.deque()
	queue.append(beginWord)
	parents = collections.defaultdict(set)
	visited = set([beginWord])
	found = False 
	depth = 0
	while queue and not found:
		depth += 1 
		length = len(queue)
		# print(queue)
		localVisited = set()
		for _ in range(length):
			word = queue.popleft()
			for i in range(L):
				for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
					if nextWord == word:
						continue
					if nextWord not in visited:
						parents[nextWord].add(word)
						if nextWord == endWord:    
							found = True
						localVisited.add(nextWord)
						queue.append(nextWord)
		visited = visited.union(localVisited)
	# print(parents)
	# Search path, DFS
	ans = []
	def dfs(node, path, d):
		if d == 0:
			if path[-1] == beginWord:
				ans.append(path[::-1])
			return 
		for parent in parents[node]:
			path.append(parent)
			dfs(parent, path, d-1)
			path.pop()
	dfs(endWord, [endWord], depth)
	return ans
## Solution 3
def findLadders(self, beginWord, endWord, wordList):
	"""
	:type beginWord: str
	:type endWord: str
	:type wordList: List[str]
	:rtype: List[List[str]]
	"""
	if not endWord or not beginWord or not wordList or endWord not in wordList \
		or beginWord == endWord:
		return []

	L = len(beginWord)

	# Dictionary to hold combination of words that can be formed,
	# from any given word. By changing one letter at a time.
	all_combo_dict = collections.defaultdict(list)
	for word in wordList:
		for i in range(L):
			all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

	# Build graph, bi-BFS
	# ans = []
	bqueue = collections.deque()
	bqueue.append(beginWord)
	equeue = collections.deque()
	equeue.append(endWord)
	bvisited = set([beginWord])
	evisited = set([endWord])
	rev = False 
	#graph
	parents = collections.defaultdict(set)
	found = False 
	depth = 0
	while bqueue and not found:
		depth += 1 
		length = len(bqueue)
		# print(queue)
		localVisited = set()
		for _ in range(length):
			word = bqueue.popleft()
			for i in range(L):
				for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
					if nextWord == word:
						continue
					if nextWord not in bvisited:
						if not rev:
							parents[nextWord].add(word)
						else:
							parents[word].add(nextWord)
						if nextWord in evisited:    
							found = True
						localVisited.add(nextWord)
						bqueue.append(nextWord)
		bvisited = bvisited.union(localVisited)
		bqueue, bvisited, equeue, evisited, rev = equeue, evisited, bqueue, bvisited, not rev
	# print(parents)
	# print(depth)
	# Search path, DFS
	ans = []
	def dfs(node, path, d):
		if d == 0:
			if path[-1] == beginWord:
				ans.append(path[::-1])
			return 
		for parent in parents[node]:
			path.append(parent)
			dfs(parent, path, d-1)
			path.pop()
	dfs(endWord, [endWord], depth)
	return ans


class Solution(object):

    # Solution using double BFS

    def findLadders(self, begin, end, words_list):
        
        def construct_paths(source, dest, tree):
            if source == dest: 
                return [[source]]
            return [[source] + path for succ in tree[source]
                                    for path in construct_paths(succ, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw: tree[word]  += neigh,
            else:       tree[neigh] += word,

        def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
            if not this_lev: return False
            if len(this_lev) > len(oth_lev):
                return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
            for word in (this_lev | oth_lev):
                words_set.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)                
                        if not done and neigh in words_set:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
                            
        tree, path, paths = collections.defaultdict(list), [begin], []
        is_found = bfs_level(set([begin]), set([end]), tree, True, words_list)
        return construct_paths(begin, end, tree)