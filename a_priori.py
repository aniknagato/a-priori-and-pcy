def gen_baskets(filename):
    baskets = []
    with open(filename) as f:
        for line in f:
            items = line.strip().split(' ')
            itemlist = []
            for i in items:
                itemlist.append(int(i))
            baskets.append(itemlist)

    return baskets

def fis1(baskets, threshold):
    freq = {}
    freq_items = {}
    for basket in baskets:
        for item in basket:
            if item not in freq:
                freq[item] = 0
            freq[item] += 1
            
    for k,v in freq.items():
        if v > threshold:
            freq_items[k] = v
            
    return freq, freq_items

def fis3(baskets, freq_item1, threshold):
    freq = {}
    freq_items = {}
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1,len(basket)):
                for k in range (j+1,len(basket)):
                    if basket[i] in freq_item1 and basket[j] in freq_item1 and basket[k] in freq_item1:
                        l = [basket[i],basket[j],basket[k]]
                        l.sort()
                        if (l[0],l[1],l[2]) not in freq:
                            freq[(l[0],l[1],l[2])] = 0
                        freq[(l[0],l[1],l[2])] += 1
    for k,v in freq.items():
        if v > threshold:
            freq_items[k] = v
    return freq, freq_items


def a_piori(filename):
    baskets = gen_baskets(filename)
    threshold = 0.01 * len(baskets)
    freq_1, freq_item1 = fis1(baskets,threshold)
    freq_3, freq_item3 = fis3(baskets,freq_item1,threshold)
    
    print ("Output of apiori algorithm containing 3 items")
    print ("Number of sets: ", len(freq_item3))
    for k,v in freq_item3.items():
        print (k,": ",v)
        

DATA_FILE = 'C:/Users/anik/GEM/class/retail.txt'


# baskets = gen_baskets(DATA_FILE)
# threshold = 0.01 * len(baskets)
# f1, freq_item1 = fis1(baskets, threshold)


#print (baskets)
# print ("Number of sets: ", len(freq_item1))
# for k,v in freq_item1.items():
#     print (k,":",v)

# f3, freq_item3 = fis3(baskets, freq_item1, threshold)
# for k,v in freq_item3.items():
#     print (k,":",v)
# print ("Number of sets with 3 items ", len(freq_item3))

a_piori(DATA_FILE)

