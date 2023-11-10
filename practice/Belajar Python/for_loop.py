# for loop

for i in range(0,5):
    print('for loop ke-' + str(i))
    print ('for loop part 2 ke-{i}')

dataMahasiswa= ['anton', 'budi', 'andi']
for i in dataMahasiswa:
    print (f'Mahasiswa : {i}')

# for loop urutan

for i in range(0 , 10):
# continue
    if i == 2:
        continue        #skip
# break
    if i == 7:
        break  
             #stop
    if i == 1:
        pass            #kosong
    print('for loop ke-'+ str(i))
# print (f' for loop part 2' ke {i})

for i in range(0, 5):
    pass