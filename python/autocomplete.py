class TrieNode():
    def __init__(self):
        """
        A Trie is a ordered tree for strings based on their prefixes.
        All descendants of a Trie node share the same prefix.
        Leaf nodes are always completed words, but intermediates can be either.
        """
        self.children = {}
        self.is_word = False

    def insert(self, letters):
        """
        Recursively insert the word by creating a Trie node for the current leading character.
        :param letters: The complete word.
        """
        return self._insert(letters, 0)

    def _insert(self, letters, i):

        # If the word ends, this node (be it intermediate or leaf) is a completed word
        if i == len(letters):
            self.is_word = True
            return

        # Get the current letter at this level
        key = letters[i]

        # Some word also have the same prefix, follow it down the Trie
        if key in self.children:
            self.children[key]._insert(letters, i + 1)

        # No previous words have the same prefix, create a new Trie
        else:
            child_node = TrieNode()
            self.children[key] = child_node
            child_node._insert(letters, i + 1)

    def depth_search(self, accumulated):
        if len(self.children) == 0:
            print
            "Match:", accumulated
            return

        if self.is_word:
            print
            "Match: ", accumulated

        for child_key in self.children.keys():
            self.children[child_key].depth_search(accumulated + child_key)

    def search(self, query):
        self._search(query, 0, "")

    def _search(self, query, q, accumulated):

        if q < len(query):
            key = query[q]

            if key in self.children:
                accumulated += key
                self.children[key]._search(query, q + 1, accumulated)
            else:
                print
                "No match"

        else:
            if self.is_word:
                print
                "Match: ", accumulated

            for child_key in self.children.keys():
                self.children[child_key].depth_search(accumulated + child_key)


words = ["A", "to", "tea", "ted", "ten", "i", "in", "inn"]
root = TrieNode()
for w in words:
    root.insert(w)

root.search("te")
