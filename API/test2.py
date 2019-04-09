from multiprocessing.dummy import Pool

def test(i):
 
    print(i)

arr=[1,2,3]
pool=Pool(3)
pool.map(test,arr)
pool.close()
pool.join()