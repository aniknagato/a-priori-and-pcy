import count_filter
cf = count_filter.CountPair(50000)
# cf.print()



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
    frequent_items = {}
    cf = count_filter.CountPair(50000)
    for basket in baskets:
        for i in range(len(basket)):
            item = basket[i]
            if item not in freq:
                freq[item] = 0
            freq[item] += 1
            if freq[item] > threshold:
                frequent_items[item] = freq[item]

            for j in range(i+1, len(basket)):
                a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
                cf.add((a,b))

    return freq, frequent_items, cf

def fis2(baskets, f1, cf, threshold):
    freq = {}
    frequent_items = {}
    cf2 = count_filter.CountPair(50000)
    
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
                if (basket[i] in f1) and (basket[j] in f1):
                    if (a,b) not in freq:
                        freq[(a,b)] = 0
                    freq[(a,b)] += 1
                    if freq[(a,b)] > threshold:
                        frequent_items[(a,b)] = freq[(a,b)]
                for k in range(j+1,len(basket)):
                    l = [basket[i],basket[j],basket[k]]
                    l.sort()                  
                    a,b,c = l[0],l[1],l[2]
                    cf2.add3((a,b,c))
                        
    return freq, frequent_items, cf2


def fis3(baskets, f1, cf2, threshold):
    freq = {}
    frequent_items = {}
    
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                for k in range(j+1,len(basket)):
                    l = [basket[i],basket[j],basket[k]]
                    l.sort()                  
                    a,b,c = l[0],l[1],l[2]                
                    if (basket[i] in f1) and (basket[j] in f1) and (basket[k] in f1) and cf2.is_candidate3((a,b,c),threshold):
                        if (a,b,c) not in freq:
                            freq[(a,b,c)] = 0
                        freq[(a,b,c)] += 1
                        if freq[(a,b,c)] > threshold:
                            frequent_items[(a,b,c)] = freq[(a,b,c)]
                        
    return freq, frequent_items

# def fis2(baskets, f1, cf, threshold):
#     freq = {}
#     frequent_items = {}
#     cf2 = count_filter.CountPair(50000)
    
#     for basket in baskets:
#         for i in range(len(basket)):
#             for j in range(i+1, len(basket)):
#                 a, b = min(basket[i], basket[j]),  max(basket[i], basket[j])
#                 if (basket[i] in f1) and (basket[j] in f1) and cf.is_candidate((a,b),threshold):
#                     if (a,b) not in freq:
#                         freq[(a,b)] = 0
#                     freq[(a,b)] += 1
#                     if freq[(a,b)] > threshold:
#                         frequent_items[(a,b)] = freq[(a,b)]
                        
#     return freq, frequent_items


def pcy(filename):

    Baskets = gen_baskets(filename)
    t = 0.005 * len(Baskets)

    Freq_1, FIS_1, cf = fis1(Baskets, t)
    
   #print for set with one item 
#     for k,v in FIS_1.items():
#         print(k,v)
#     print('There are', len(FIS_1), 'sets.')



    Freq_2, FIS_2, cf2 = fis2(Baskets, FIS_1, cf, t)
# print for set with two items.
#     print('There are', len(FIS_2), 'sets.  Threshold is', t)
#     print('We only look at fewer than', len([x for x in cf.Table if x > t]), "items.")
    
    Freq_3, FIS_3 = fis3(Baskets,FIS_1, cf2, t)
    
    
    #print for set with three items.
    
    print('There are', len(FIS_3), 'sets containing 3 items.  Threshold is', t)
    print('We only look at fewer than', len([x for x in cf2.Table if x > t]), "items.")
    
    for k,v in FIS_3.items():
        print (k,": ",v)
    
    
DATA_FILE = 'C:/Users/anik/GEM/class/retail.txt'
# baskets = gen_baskets(DATA_FILE)
# print (baskets[0:100])

pcy(DATA_FILE)