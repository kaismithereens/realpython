print(1<2 and 3<4)#both True
print(2<1 and 4<3)
print(1<2 and 4<3)
print(2<1 and 3<4)
print()

print(1<2 or 3<4)
print(2<1 or 4<3)#both False
print(1<2 or 4<3)
print(2<1 or 3<4)
print()

print(False or (False and True))
print(True and (False or True))
print()

print((not False) or True)
print(False or (not False))
print()

print(True and not(1 !=1))
print(("A" != "A") or (not(2 >=3)))