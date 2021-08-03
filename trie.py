# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = {}
        self.data = []
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key, data):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for ch in key:
            # if current character is not present
            if pCrawl.children.get(ch) is None:
                pCrawl.children[ch] = self.getNode()
            pCrawl.children[ch].data.append(data)
            pCrawl = pCrawl.children[ch]
        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def insert_key(self, key):
        data = key
        while len(key) > 0:
            self.insert(key, data)
            key = key[1:]

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for ch in key:
        # for level in range(length):
            # index = self._charToIndex(key[level])
            if pCrawl.children.get(ch) is None :
                return False
            pCrawl = pCrawl.children[ch]

        return pCrawl != None
    
    def isEmpty(self, node):
        import string
        character = string.printable
        for ch in character:
            if node.children.get(ch) is not None:
                return False
        return True

    def remove_data(self, s, key):
        # print(s)
        node = self.root
        for ch in s:
            if node.children.get(ch) is None:
                return
            node = node.children[ch]
            # print(node.data)
            if key in node.data:
                node.data.remove(key)
            # print(node.data)
            # print(node)

    def remove_key(self, node, key, index):
        self.remove_data(key[index:], key)
        if index == len(key):
            if node.isEndOfWord:
                node.isEndOfWord = False
            if self.isEmpty(node):
                del node
                node = None
            return node
        if node is None:
            return node
        if node.children.get(key[index]) is not None:
            node.children[key[index]] = self.remove_key(node.children[key[index]], key, index+1)
        if self.isEmpty(node) and node.isEndOfWord == False:
            del node
            node = None
        return node


    def get_data(self, key):
        # Get data in the trie
        pCrawl = self.root
        length = len(key)
        for ch in key:
            if pCrawl.children.get(ch) is None:
                return []
            pCrawl = pCrawl.children[ch]
            # print(pCrawl)

        return pCrawl.data

# driver function
def main():
    # Input keys 
    keys = ["21",
        "8218159",
        "9921491",
        "1452125",
        "1836321",
        "2147383",
        "7864216",
        "2157186",
        "9210554",
        "2175228",
        "3485214"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        data = key
        while len(key) > 0:
            t.insert(key, data)
            key = key[1:]

    # Use function
    print(t.isEmpty(t.root))
    print(t.root.children)
    t.root = t.remove_key(t.root,'21',0)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))

    print("{} ---- {}".format("18", output[t.search("18")]))

    print(t.get_data('21'))

# if __name__ == '__main__':
#     main()