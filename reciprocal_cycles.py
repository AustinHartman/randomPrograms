unit_fracs = []
for i in range(1, 1000):
    unit_fracs.append(1/i)

print(1/72)
print(unit_fracs)


pat = ''
for let in range(len(s), 0, -1):
    print(pat)
    pat = pat + let
    if pat == s[let - len(pat) : let]:
        print(pat, len(pat))




