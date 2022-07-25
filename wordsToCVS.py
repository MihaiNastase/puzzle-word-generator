import pdb
import pandas as pd

f = open("words.txt", 'r')

words_list = []

for line in f:
    for word in line.split():
        words_list.append(word)

df = pd.Series(words_list)
df.to_csv("words.csv", index=False, header=0)

def main():
    print(df.sample(4).to_list())

if __name__ == "__main__":
    main()