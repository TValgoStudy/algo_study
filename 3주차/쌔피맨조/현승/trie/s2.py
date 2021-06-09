# leetcode 211

"""
trie 구조로 문자를 저장했을 경우 장점
1.
"""

# trie 노드
class TrieNode:
    def __init__(self):
        # 리프노드 판별변수
        self.is_end = False
        self.links = {}


class Trie:
    def __init__(self):
        # 루트 노드를 생성
        self.root = TrieNode()

    def recur_add(self, node: TrieNode, word: str) -> None:
        if len(word) == 0:
            node.is_end = True
            return

        ch = word[0]
        node.links[ch] = node.links.get(ch, TrieNode())
        self.recur_add(node.links[ch], word[1:])


    def recur_search(self, node: TrieNode, word: str) -> bool:
        if len(word) == 0:
            is_end = node.is_end
            return is_end

        ch = word[0]
        # 현재 문자가 '.'일 경우에는 모든 문자로 매칭이 가능하다
        if ch == '.':
            # 현재 노드의 모든 자식 노드에 대해 조사한다.
            letters = node.links.keys()
            for key in letters:
                ret = self.recur_search(node.links[key], word[1:])
                if ret is True:
                    return True
            return False

        else:
            next_link = node.links.get(ch)
            if next_link:
                return self.recur_search(next_link, word[1:])
            return False


trie = Trie()
trie.recur_add(trie.root, 'baby')
trie.recur_add(trie.root, 'ball')
trie.recur_add(trie.root, 'tree')
trie.recur_add(trie.root, 'trie')

print('baby', trie.recur_search(trie.root, 'baby'))
print('ba..', trie.recur_search(trie.root, 'ba..'))
print('.ree', trie.recur_search(trie.root, '.ree'))
print('nocope', trie.recur_search(trie.root,'nocope'))