with open ("lec003_ex1.txt", "wt", encoding="cp1251") as f:
    print('абвгд\nеёжэи', file=f)
    print('клмн', file=f)
with open ('lec003_ex1.txt', 'rb')as f_rb:
    content = f_rb.read(10)
print([v for v in content[4:8]])
print("amogus")
print("abobusss")
print("sus")
print("suuuuus")