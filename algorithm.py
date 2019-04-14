def fun_watson(N,p,q):
    list = []
    try:
        if isinstance(p, (int, long)) and isinstance(q, (int, long)) and isinstance(N, (int, long)):
            if p == q:
                return "Please note: Value of p and q are same. Provide different values."
            if (p < 2 or q < 2):
                return "Please note: Value of p and q should be greater than 1."
            if (N<1):
                return "Please note: Value of N should be greater than 0."
            for i in range(1,N+1):
                if((i%p == 0 and i%q == 0) and (i != p and i != q)):
                    list.append("WATSON")
                elif(i%p == 0 and i!=p):
                    list.append("WAT")
                elif(i%q == 0 and i!=q):
                    list.append("SON")
                else:
                    list.append(i)
            output = ' '.join(str(e) for e in list)
            return output
        return "Please note: p, q, N should be positive integers."
    except:
        return "Something went wrong in algorithm.py"
# print fun_watson(20,3,4)
# print fun_watson(30,5,10)
# print fun_watson(10,2,4)
