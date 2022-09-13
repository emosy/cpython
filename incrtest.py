import ast


print(ast.dump(ast.parse("""
a = 5
a++
"""), indent=4))

# a = 5
# a++

print(ast.dump(ast.parse("""
a = 5
print(f'a = {a}')
"""), indent=4))