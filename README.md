# Proving Collatz wrong since 2022

## Who?

This Collatz dude in 1937 proposed the following (copied from [this](https://en.wikipedia.org/wiki/Collatz_conjecture) Wikipedia article): "if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence."

In simpler terms, pick a number and call it whatever you want. Yes, really. When asked if you can do this, my 7th grade math teacher spent the rest of the lesson naming all variables on the graph "Ralph" and I will continue that here. So we have a number Ralph. If Ralph is even, divide it by 2. If Ralph is odd, multiply Ralph by 3 and add 1. 

For my visual learners: 

Mod is short of modulus, or the remainder after division. Any even integer divided by 2 will always have a remainder of 0, and any odd integer divided by 2 will always have a remainder of 1. 

<img src="https://latex.codecogs.com/svg.image?f{(Ralph)}:\;_{\mathrm{if}\;Ralph\;\mod\;2\;=\;0:\;Ralph\;\ast\;3\;&plus;\;1}^{\mathrm{if}\;Ralph\;\mod\;2\;=\;1:\;\frac{Ralph}2}" title="f{(Ralph)}:\;_{\mathrm{if}\;Ralph\;\mod\;2\;=\;0:\;Ralph\;\ast\;3\;+\;1}^{\mathrm{if}\;Ralph\;\mod\;2\;=\;1:\;\frac{Ralph}2}" />

It should be noted the Collatz conjecture has never been proven nor disproven, but all tested numbers thus far always reach 1. However, there has yet to be a mathematical function that proves the Collatz conjecture for all real integers (if you haven't figured it out, decimal numbers do not work). That's why I am trying to find out for all Real numbers from 1 to Googl (1 with 100 zeros) if there is even just one number that breaks the Collatz conjecture.

## Why?...

Bored, lol.

## What's this code doing?

A [recent paper](https://arxiv.org/abs/math/0601622) written by Alex Kontorovich proposes the idea that there might be certain "seeds" that break the Collatz conjecture. Such seeds are named that way due to interesting phenomena that occurs when playing Conway's Game of Life. When certain seeds, or strings of integers that setup the game state, are used, the game continues on forever due to the way the game is designed (certain cells die if they are adjacent to too many or too few other cells). Alex (yo Alex if you're reading this for whatever reason and you prefer I call you Mr. Kontorovich just shoot me an email) is much smarter than I am and I'm not that good with math nor programming for that matter but I am good at being stubborn. And there is nothing more stubborn than cobbling together two python programs that essentially try to brute force the conjecture one way or another by testing either a large breadth of random seeds at extremely high values, and checking every single number from 1 to 1 Googl. 

Collatzthingy.py uses numpy to generate a random integer from 1 to 429496729 (a significant digit away from the maximum integer value numpy can randomly generate, 2^32 -1. For whatever reason, using the limit or just below it wouldn't work on my machine and throw an error even StackOverflow had no solution for so I just went with it.) then generate and multiply 5 more times using more random numbers of the same parameter. There is 0 logic or reasoning for the generation, asides from I hope such numbers generated would be large enough to potentially be seeds for breaking the conjecture. 

BRUTEFORCE.py is checking for the conjecture on every single number from 1 to 1 Googl. I actually mistakenly only started checking odd numbers, thinking any even number would immediately be out, but we know that not every even number divided by two will remain even. 10, for example, divides by 2 into 5. This has been reflected in the latest code on the repository.

So yeah. I'm running BRUTEFORCE.py on my computer, and will soon move and run both programs on a virtual machine on my server to allow for more efficient 24/7 calculation. I severely doubt that my code will break the conjecture. But my favorite answer to asked "Why?" is always "Why not?".

If somehow it does by some (pseudo literally) random miracle break said conjecture, I will update this readme reflecting as such. Until then, good luck and do good works.