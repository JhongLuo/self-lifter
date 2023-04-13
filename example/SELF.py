
B = """print(\"hello world, I am excited to be a self lifter!\")
Pw = \"\"\"
B = \\\"\\\"\\\"OUT_CODE\\\"\\\"\\\"
\"\"\"

def escape(s):
    s = s.replace(\"\\\\\", \"\\\\\\\\\")
    s = s.replace(\"\\\"\", \"\\\\\\\"\")
    return s
 
def code2machine(w):
    global Pw
    Pw = Pw.replace(\"OUT_CODE\", w)
    return Pw

A = code2machine(escape(B))
open('example/TAPE', 'w').write(A+B)"""
print("hello world, I am excited to be a self lifter!")
Pw = """
B = \"\"\"OUT_CODE\"\"\"
"""

def escape(s):
    s = s.replace("\\", "\\\\")
    s = s.replace("\"", "\\\"")
    return s
 
def code2machine(w):
    global Pw
    Pw = Pw.replace("OUT_CODE", w)
    return Pw

A = code2machine(escape(B))
open('example/TAPE', 'w').write(A+B)