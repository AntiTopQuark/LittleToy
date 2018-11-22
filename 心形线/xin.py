print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
import msvcrt
  
print("Press 'D'/'d' to exit...")
  
while True:
 if ord(msvcrt.getch()) in [68, 100]:
  break