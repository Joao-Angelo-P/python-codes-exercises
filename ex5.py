# Listcomps vs map and filter
symbols = "%$¨&*@"
__ascii = [ord(x) for x in symbols if ord(x) > 41] # listcomps

__ascii_ = list(filter(lambda x: x > 41, map(ord, symbols))) # map and filter

# Unpacking sequences

