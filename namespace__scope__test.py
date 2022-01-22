a=1
print(globals())
print(locals())

if a==1:
    msg='hello scope'

print(globals())

def ppp():
    ppp1='ppp local'
    print(locals())
    def qqq():
        qqq1='qqq local'
        print(locals())
    print(locals())
    qqq()

ppp()