"""
task: https://pl.spoj.com/problems/AL_17_01/
ASCII: space = 32; 0-9 = 48-57
"""
text = "Mundial "
text += chr(ord('R') - ord(' '))
text += chr(ord('P') - ord(' '))
text += chr(ord('Q') - ord(' '))
text += chr(ord('T') - ord(' '))
print(text)