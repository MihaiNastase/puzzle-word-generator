# puzzle-word-generator
A Python console app used to create words for a puzzle game called Word4Word.

### The rules of the game are : 
You have 4 words with the letters scrambled in a 4x4 grid, but the order of the letters are maintained per row (i.e first row will contain the first letter in all 4 words, second row the second letter of each word etc). The goal of the game is to combine the letter to create all 4 words, going from top to bottom, without reusing a letter if you already created a word.

Example:
['t' 'm' 'i' 'f']
['o' 'u' 'p' 'o']
['x' 'c' 'a' 'g']
['k' 'y' 'a' 'd']

The words you have to create here are "foxy", "ipad", "toga", "muck". Starting from the top, you get first row, letter 't', second row, letter 'o', third row, letter 'g', fourth row, letter 'a' and you get 'toga'. 

