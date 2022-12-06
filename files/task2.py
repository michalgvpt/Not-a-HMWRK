fr=open('files/texts/hada.txt','r')
fw=open('files/texts/hadawrite.txt','w')
def snake(fr):
    fl=0
    counter=0
    counter2=1
    for line in fr:
        counter+=1
        if len(line)>fl:
            fl=len(line)
        for i in range(1,len(line)):
            if line[i-1]!=line[i]:
                fw.write(line[i-1])
                fw.write(str(counter2))
                counter2=1
            else:
                counter2+=1
            if line[i]=='\n':
                fw.write('\n')
    if fr.readline()=="":
        fw.write(line[i-1])
        fw.write(str(counter2))
    print('Number of games:', counter)
    print('Number of steps of the longest game:', fl-1)
print(snake(fr))