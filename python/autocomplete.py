class TrieNode():

    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, letters):
        return self._insert(letters, 0)

    def _insert(self, letters, i):
        if i == len(letters):
            self.is_word = True
            return

        key = letters[i]

        if key in self.children:
            self.children[key]._insert(letters, i+1)

        else:
            child_node = TrieNode()
            self.children[key] = child_node
            child_node._insert(letters, i+1)

    def depth_search(self, accumulated):
        if len(self.children) == 0:
            print "Match:", accumulated
            return

        if self.is_word:
            print "Match: ", accumulated

        for child_key in self.children.keys():
            self.children[child_key].depth_search(accumulated+child_key)

    def search(self, query):
        self._search(query, 0, "")

    def _search(self, query, q, accumulated):

        if q < len(query):
            key = query[q]

            if key in self.children:
                accumulated += key
                self.children[key]._search(query, q+1, accumulated)
            else:
                print "No match"

        else:
            if self.is_word:
                print "Match: ", accumulated

            for child_key in self.children.keys():
                self.children[child_key].depth_search(accumulated+child_key)

words = ["A", "to", "tea", "ted", "ten", "i", "in", "inn"]
root = TrieNode()
for w in words:
    root.insert(w)

root.search("te")