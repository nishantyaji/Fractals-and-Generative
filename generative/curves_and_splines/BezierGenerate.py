import sys
sys.path.append('.')
sys.path.append('./generative')
#from Bezier import RandomBezierSmall
import Bezier
rb = Bezier.RandomBezierSmall()
iterations = 2000
for i in range(0, iterations):
    print(i)
    rb.bezier()
rb.save()
rb.show()