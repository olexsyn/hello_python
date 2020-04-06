from pathlib import Path
# for Python 3.5+

work1 = Path.cwd()
print(work1)
print(work1.parent)

work2 = str(Path.cwd())
print(work2)
# print(work2.parent)  # error! т.к. строка