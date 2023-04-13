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

