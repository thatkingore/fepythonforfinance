current_asset = "Current " + "Assets"
print(current_asset + " equal 10,000")
print(current_asset + " equal " + str(10000))

terms = ['NPV', 'DCF', 'Equities', 'FICC', 'LBO', 'M&A']
print(terms[0])
print(terms[1])

terms.append("WACC")
print(terms)

terms.remove("WACC")
print(terms)

del terms

terms = {'NPV', 'DCF', 'Equities', 'FICC', 'LBO', 'M&A'}

terms.add('FIG')
print(terms)

terms.remove('FIG')
print(terms)

terms.update(["DCF", "WACC"])
print(terms)

work = [5, 10, 15, 20]
print(work)

print(type(work))

work_string = str(work)
print(work_string)
print(type(work_string))

b = "10000"
print(b)
print(type(b))
a = int(b)
print(a)
print(type(a))
