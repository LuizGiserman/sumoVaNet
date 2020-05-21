import csv
#'A1 northbound access at a minor junction between A167 near Washington Birtley and A692 entrySlipRoad 120014302.csv'
times = []
initial_time = '05.44'
with open ('roadLength.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    future_time = initial_time
    for index, row in enumerate(csv_reader):
        time = row[1].split(':')
        if index != 0:
            time_string = str(time[0]) + '.' + str(time[1])
            times.append ((future_time, time_string, row[11]))
            future_time = time_string


# print (times)
# index = 0
# for (hour, minutes, numVeh) in times:
#     file = open ('odFiles/od'+ str (index) + '.txt', 'w')
#     file.write('$OR;\n')
#     file.write('{} {}\n'.format(hour, minutes))
#     file.write('1.00\n')
#     file.write('\t{}\t{}\t{}'.format(1, 3, numVeh))
#     file.write('\n')
#     file.close()
#     index += 1

subtracao_inicial = (int( initial_time.split('.')[0] ) * 60 * 60 ) + (int ( initial_time.split('.')[1] ) * 60)

file = open ('novo/amitran.xml', 'w')
file.write('<demand xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/amitran/od.xsd">\n')
file.write('\t<actorConfig id="0">\n')
for (first, second, numVeh) in times:
    first_list = first.split('.')
    print (first_list)
    first_time = ((int (first_list[0]) *60*60 ) + (int (first_list[1]) * 60)) - subtracao_inicial
    print (first_time)
    second_list = second.split('.')
    print (second_list)
    second_time = ((int (second_list[0]) *60*60 ) + (int (second_list[1]) * 60)) - subtracao_inicial
    file.write('\t\t<timeSlice duration="'+ str((second_time - first_time)) +'" startTime="'+ str(first_time) + '">\n')
    file.write('\t\t\t<odPair amount="'+ numVeh +'" destination="3" origin="1"/>\n')
    file.write('\t\t</timeSlice>\n\n')
file.write('\t</actorConfig>\n')
file.write('</demand>')
