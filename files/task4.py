fr=open('files/texts/meteostanice.txt', 'r')

def stations(fr):
    counter=0
    temper=0
    temp=False
    average=0
    result=' '
    for line in fr:
        counter+=1
        variable=line[21:26:1]
        result+=variable
        result+='\n'
        variable=variable[1::]
        variable=variable.replace(',','.')
        if float(variable)>float(temper):
            temper=float(variable)
            station=line[:3]
            temper=str(temper)
            if float(variable)<0:
                temper='-'+temper
            else:
                temper='+'+temper
        average+=float(variable)
    average=average/counter
    print('Number of measurements: ',counter)
    print('Measurements:','\n',result)
    print('Highest temperature: ',temper, 'Station: ',station)
    ave=('Average temperature of stations: '+str(average))
    return(ave)
print(stations(fr))