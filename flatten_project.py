
# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

output_list = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
# is instance metodu veri tipi karşılaştırmak için kullanılırmış.
            pass
        else:
            output_list.append(i)

nested_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten(nested_list)
print(output_list)

    






    


