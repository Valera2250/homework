def difference(*args):
    if not args:
        return 0

    result = max(args) - min(args)
    return round(result, 2)

print(difference(1, 2, 3))             # 2
print(difference(5.5, 2.2, 7.7))       # 5.5
print(difference())                    # 0
print(difference(-10, 10, 0))          # 20
