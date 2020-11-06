import matplotlib.pyplot as plt

def print_histogram (word):   
    char_freq = {} 
    for keys in word: 
        char_freq[keys] = char_freq.get(keys, 0) + 1    

    plt.bar(char_freq.keys(), char_freq.values(), width=0.3, color='c')

    plt.title("PHOC")
    plt.ylabel("Characters count")
    plt.xlabel("Characters")
    plt.show()
    return

def split_word (word, n) :

    for index in range(0, len(word), n):
        print(word[index : index + n])
        print_histogram(word[index : index + n])
    return


word = "रामायण"
i = 2
while i <= len(word) / 2:
    split_word(word, i)
    i += 1



