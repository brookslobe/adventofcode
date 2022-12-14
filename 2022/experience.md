# Takeaways from first AoC

## Including 
- AoC process itself
- Python familiarization
- Code modularity/flexibity...hindsight improvements

## Day 01
- Function for reading input would be a good first util
- Boolean values as "True" and "False"..."or"/"and" operators
- Jank off-by-one with pointer
- How to print without newline double-up?
- Regex library instead of comparing against string literals for whitespace
- List indexing is neat

## Day 02
- Better way to deal with loop-around fencepost than ternary with min/max idx?
- Python doesn't have constants...guess I could use UPPER_CASE_VAR still
- Ternaries, yay
- Avoided the temptation to make a 3x3 literal using a 2d list.  That'd probably have been quicker, despite the dirtiness.

## Day 03
- Got caught up thinking that there was something like ASCII value for abc that would work
- enumerate in for loop is sweet to get idx
- Feel like it would be _"better"_ to persist input lines instead of saving most recent 3 in vars...though that would save on memory if you had a giant input?  Feel like future problems will require persisted collections.
- Intersection feels weird compared to other languages
- Technically, only have to populate charsets after the first with items contained in the previous set(s)
- Need to use set instead of dictionary in the future...skimmed doc and thought that set contents were frozen after initialization (just can't modify existing value)

## Day 04
- Tuples
- Wasn't able to cast inside of tuple declaration

## Day 05
- Neat that stacks have native implementation with lists
- Reading in unorthodox file that has varied "checkpoints" within the file that you need to deal with differently is interesting...real world would hopefully have separate files or a standardized format like json
- Unsure if reading file lines into list of strings is a good approach...apprehension over storing all that data
- Some nice use of regex
- Used a _list comprehension_ (wow, such python!)
- Multi transfer between stacks would ideally be a function, that feels bug-prone otherwise

## Day 06
- Fairly easy to implement queue in python, just like stack
- Should look how to iterate by character within input file, rather than nested iteration within lines
- Set as unique count check seems like a good option
- Technically should have made into function and returned...only one line in the input, but only broke out of the inner loop
- Had to guess whether packet start indicator and message start indicator could share characters...feel like in the real world they wouldn't?  Requiring identification of packet start (and then message start afterwards).