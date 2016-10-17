class AttrCls:
    myvar = 'a'


inst = AttrCls()
inst.myvar = 'b'
print(inst.myvar)
print(getattr(inst, 'myvar'))