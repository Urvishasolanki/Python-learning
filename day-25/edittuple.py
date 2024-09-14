countries=("spain","italy","india","england")
temp=list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)