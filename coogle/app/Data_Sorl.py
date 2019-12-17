# đưa dữ liệu lên solr

import pysolr
import json

solr = pysolr.Solr('http://localhost:8983/solr/tktdtt', always_commit=True)

with open('exporters.json', 'r', encoding='UTF-8') as f:
    row_data = f.read().split('},')
    
    data = []
    i = 0
    for item in row_data:
        item = item.replace('{', '')
        item = item.replace('}', '')
        item = '{ ' + item + '}'
        try:
            item = eval(item)
            # print(item)
            data.append(item)
        except:
            print('error!! + {}'.format(i))
            # pass
        i = i + 1


solr.add(data)

