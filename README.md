# ctf-tools
All of my tools which I write for capture the flag competitions in one location.
# content
* Caesar cypher solver
* Xor cypher solver
## Xor cypher solver usage:
* A fairly optimal brute force algorithm to find the xor key.
### usage:
python3 xor_brute_force.py 
* --f [filename of the cyphertext] 
* --r [regex pattern to look for] 
* --l [max key length]

i.e.: python3 xor_brute_force.py --f "something.txt" --r ".*this is totally a pattern.*" --l 3
### usage example in custom code (your own):
![Preview](http://www.imageurl.ir/images/90340979868660328213.png)

## Caesar cypher solver usage:
python3 caesar.py --f [filename]
and voilà:
![Preview](http://www.imageurl.ir/images/14026727511808012822.png)
