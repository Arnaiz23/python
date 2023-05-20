import psutil

addrs = psutil.net_if_addrs()
# for name in addrs:
#     print(name)

# print(type(addrs.keys()))
# print(addrs.keys())
print(list(addrs.keys())[1])
# print(sorted(psutil.net_if_addrs().keys())[2])
