unit_fracs = []                                                     # Create list of all reciprocal frac 1-1000
for i in range(1, 1000):
    unit_fracs.append(str(1/i)[2:])

unit_fracs = [frac for frac in unit_fracs if len(frac) > 4]         # Filter all list elements under 4 characters
print(unit_fracs)



