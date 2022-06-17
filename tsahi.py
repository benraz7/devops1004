import time

loader_list = ['-', '\\', '|', '/']
for i in range(200):
    print(loader_list[i % len(loader_list)], end = '', flush = True)
    time.sleep(0.01)
    print(end = '\r', flush = True)
    # print()

