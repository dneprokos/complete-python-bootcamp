print('This is a string {}'.format('inserted by Kostia'))

# Index position formatting
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # The quick brown fox

# Variable name formatting
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))  # The quick brown fox

# Float formatting
result = 100/777
print("The result was {r:1.3f}".format(r=result))  # 0.129

# f formatting. Available starting from Python 3.6
name = "Jose"
print(f"Hello {name}")

