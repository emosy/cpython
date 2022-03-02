import ast


print(ast.dump(ast.parse("""
a = 5
a++
"""), indent=4))