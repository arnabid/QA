#input = [ 'cat', 'dog', 'rats', 'moon', 'god', 'star', 'tsar' ]
#output = [ 'dog', 'rats', 'god', 'star', 'tsar' ]

from collections import defaultdict

def get_anagrams(words):
	process_dic = defaultdict(list) # key: X, value : word
	ans = []
	for word in words:
		x = ''.join(sorted(word))
		process_dic[x].append(word)

	for key in process_dic:
		if len(process_dic[key]) > 1:
			ans.extend(process_dic[key])

	return ans

if __name__ == '__main__':
	words = [ 'cat', 'dog', 'rats', 'moon', 'god', 'star', 'tsar', 'noon', 'oonn' ]
	print (get_anagrams(words))
