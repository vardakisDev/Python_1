#pinakas 3x3 opoy exei grafei ws exis kathe grammi einai grammi toy pinaka kai ta stoixeiia diaxoristnai ne kena  kai amefanizei tin orizousa tis
import numpy as np

with open("array.txt","r") as f:
    lines = [line.split() for line in f]

f.close()
print(lines)
new_list = [[int(x) for x in item] for item in lines]
print(np.linalg.det(new_list))