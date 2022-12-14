
irr_fraction = ""
count = 1

while(len(irr_fraction) < 1000000):
    irr_fraction += str(count)
    count += 1

print(int(irr_fraction[0]) *
      int(irr_fraction[9]) *
      int(irr_fraction[99]) *
      int(irr_fraction[999]) *
      int(irr_fraction[9999]) *
      int(irr_fraction[99999]) *
      int(irr_fraction[999999]))
