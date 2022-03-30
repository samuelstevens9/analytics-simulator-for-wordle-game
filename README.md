# Analytics Simulator for Wordle Game

For fun, wondering how I might use the popular Wordle game to learn some machine learning.
Maybe implement a reinforced learning RL algorithm to learn to play? Monte Carlo method? Brute force?

Also some general game plat strategy questions:

 * What is the best start word?
 * what about a second start word if no letters are in the first word?

# Some Analytics

The first brute force method was to try each word form the dictionary as the start word.
Then play 2000 games using that start word, and save the win rate.
After all that we got these top twenty words:

| Start Word | Win of 2000 | Win % |
| ----- | ---- | -- |
| clump | 1734 | 87% |
| clamp | 1721 | 86% |
| plant | 1719 | 86% |
| blimp | 1718 | 86% |
| clint | 1715 | 86% |
| chomp | 1714 | 86% |
| mulct | 1713 | 86% |
| paint | 1711 | 86% |
| blurt | 1711 | 86% |
| plumb | 1710 | 86% |
| grump | 1708 | 85% |
| nymph | 1706 | 85% |
| wroth | 1705 | 85% |
| bract | 1703 | 85% |
| amble | 1703 | 85% |
| thump | 1702 | 85% |
| thank | 1702 | 85% |
| trump | 1701 | 85% |
| ponit | 1701 | 85% |
| pinto | 1701 | 85% |

This is just from one round, and due to the nature of randomness this this will change at each run. But it's an interesting start.


# Wordle Game Env

The game is simulated in `/wordle_env`. It starts a game, picks a random word or uses on given to it.
Then returns a 5 x 6 matrix after each word attempt.

```
[
  [1, 1, -1, -1, 1],
  [1, 1, 1, 5, 1], 
  [5, 5, 5, 5, 5], 
  [0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0]
]
```

 * `0` for not attempted yet
 * `-1` for the letter that is not in the word
 * `1` for the letter that is in the word but not that location
 * `5` for the letter that is in the right spot

# Brute Force Solver

First I created a simple brute force solver (in `/solver/brute.py`) that tried a word, then eliminated the words from the dictionary
based on the environment state returned. From those words left it picked a random one and repeated.

# Dictionary

For this I started with `/usr/share/dict/words` and then tired http://www.gwicks.net/dictionaries.htm, specifically `usa2.txt` but any dictionary will do. 

# What's Next

Welp, if I get some more free time, I might try to do some actual RL or Monte Carlo optimization on top of the Brute method. 