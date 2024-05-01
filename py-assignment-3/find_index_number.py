def find_number(lst):
  number = 99
  index = []
  for i, el in enumerate(lst):
      if number == el:
          number = el
          index.append(i)
  return index
test_scores = [109, 9, 30, 95, 1, 404, 69, 78, 99, 101]
print(find_number(test_scores)) # returns [8]
