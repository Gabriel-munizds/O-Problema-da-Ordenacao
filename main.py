#insira quantos números em ordem aleatória quiser
A = [11,10,9,8,7,6,5,4,3,2,1,0]
for j in range(0,len(A)):
    chave = A[j]
    # inserir A[j] na sequência ordenada A[1, ..., j-1]
    i = j - 1
    while i>=0 and A[i] > chave:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = chave
print(A)