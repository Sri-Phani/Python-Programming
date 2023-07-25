import random
#for i in range(5):
    #print(random.random())#in b/w 0 and 1
    #print(random.uniform(1,10))
    #print(random.randint(1,5))
    #print(random.randrange(100,111,2))

a=['21a91a05d8','21a91a05d9','21a91a05g0','21a91a05g5','21a91a05g6','21a91a05e3']
for i in range(1):
    #print(random.choice(a))
    print(random.sample(a,2))
random.shuffle(a)
#print("After some random shuffling:",a)

