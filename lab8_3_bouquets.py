import time
def bouquets(narcissus_price, tulip_price, rose_price, summ):
    i = 0
    for narcissusQ in range(int(summ/narcissus_price) + 1):
        for tulipQ in range(int((summ - narcissusQ * narcissus_price)/tulip_price) + 1):
            for roseQ in range(int((summ - narcissusQ * narcissus_price - tulipQ * tulip_price)/rose_price) + 1):
                if (narcissusQ + tulipQ + roseQ) % 2 != 0:
                    i += 1
    return i
s = time.time()
print bouquets(1,1,1,5), "elapsed = ", time.time() - s
s = time.time()
print bouquets(2,3,4,10), "elapsed = ", time.time() - s # 12
s = time.time()
print bouquets(2,3,4,100), "elapsed = ", time.time() - s # 4019
s = time.time()
print bouquets(200,300,400,10000), "elapsed = ", time.time() - s # 4019
s = time.time()
print bouquets(200,300,400,100000), "elapsed = ", time.time() - s # 3524556
