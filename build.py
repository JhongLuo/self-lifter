# the function does the transformation work
def build(code):
    tail = open('helpers/TAIL', 'r').read()
    tail = tail.replace("CODE2MACHINE\n", open('helpers/code2machine.py', 'r').read())
    B = code
    B += tail
    from helpers.code2machine import code2machine, escape
    A = code2machine(escape(B))
    return A + B


if __name__ == '__main__':
    code = open('example/hello.py', 'r').read()
    open('example/SELF.py', 'w').write(build(code))

