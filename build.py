def build(code):
    tail = open('helpers/TAIL', 'r').read()
    tail = tail.replace("CODE2MACHINE\n", open('helpers/code2machine.py', 'r').read())
    B = code
    B += tail
    import helpers.code2machine as code2machine
    A = code2machine.code2machine(code2machine.escape(B))
    return A + B


if __name__ == '__main__':
    code = open('example/hello.py', 'r').read()
    open('example/SELF.py', 'w').write(build(code))

