# https://www.geeksforgeeks.org/trie-insert-and-search/

# we are only building trie tree for 26 small characters of alphabets
# No capital letters or space or special characters are allowed

class trieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = trieNode()

    def get_node(self):
        return trieNode()

    def char_to_index(self, char):
        '''ord() : It converts the given string of length one,
        return an integer representing the unicode code point of the character.
        For example, ord(‘a’) returns the integer 97.'''
        return ord(char) - ord('a')

    def insert(self, word):
        crawl = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if crawl.children[index] == None:
                crawl.children[index] = self.get_node()
            crawl = crawl.children[index]
        crawl.end_of_word = True

    def search(self, word):
        crawl = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]
        return crawl.end_of_word

    def no_children(self, node):
        for i in range(26):
            if node.children[i]:
                return False
        return True

    def delete(self, word, node, depth=0):

        if depth < len(word):
            index = self.char_to_index(word[depth])
            if node.children[index]:
                node.children[index] = self.delete(
                    word, node.children[index], depth+1)
                print(node.children[index])
            else:
                return node

        if depth == len(word):
            if self.no_children(node):
                return None
            else:
                node.end_of_word = False
                return node
        else:
            if self.no_children(node) and node.end_of_word == False:
                return None
            else:
                return node


# output


keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "hero", "heroplane"]

t = Trie()

# Construct trie
for key in keys:
    t.insert(key)

# Search for different keys
output = ["Not present in trie", "Present in trie"]
print("{} ---- {}".format("hero", output[t.search("hero")]))
print("{} ---- {}".format("these", output[t.search("these")]))
t.root = t.delete("heroplane", t.root)
print("{} ---- {}".format("heroplane", output[t.search("heroplane")]))
