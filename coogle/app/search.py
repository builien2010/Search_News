from pyvi import ViTokenizer

import gensim

import pysolr
import json

solr = pysolr.Solr('http://localhost:8983/solr/tktdtt', always_commit=True)


# tìm kiếm chính xác , nhập vào 1 từ, tìm kiếm trong descrption



def searchDescription(sentence):

    key = "description : " + "\"" + sentence + "\""

    results = solr.search(key)

    return results


# tìm kiếm các bài có chứa 1 từ trong câu nhập vào, nhập vào 1 từ , tìm kiếm trong description
def searchDescription1(sentence):

    key = "description : " + sentence

    results = solr.search(key)

    return results

def searchTitle(sentence):

    key = "title : " + sentence

    results = solr.search(key)

    return results


def searchTopic(sentence):

    key = "topic : " + sentence

    results = solr.search(key)

    return results



# tìm kiếm trong tất cả các trường
def searchAll(sentence):
      
    results = solr.search(sentence)

    return results


# tìm kiếm từ đồng nghĩa

def searchDongNghia(sentence):
    
    content  = ViTokenizer.tokenize(sentence)

    list_word = content.split()

    stopwords = []
    f = open('vietnamese-stopwords.txt', 'r')
    for line in f:
        line = line.rstrip()
        #print(line)
        line = line.replace(' ', '_')
        
        stopwords.append(line)
    f.close()



    content  = ViTokenizer.tokenize(sentence)

    list_word = content.split()

    words = []
    for word in list_word: 
        word = word.lower()
        if word not in stopwords:
            words.append(word)

    model = gensim.models.KeyedVectors.load_word2vec_format('model/baomoi.model.bin', binary = True)  

    N = 3

    list_dongnghia = []

    for word in words:

        # kiểm tra nếu word có trong từ điển ko, nếu có thì lấy tra N từ đồng nghĩa với từ đó

        dongnghia = model.wv.most_similar(positive=[word], topn=N)  

        for i in range( 0, N):

            list_dongnghia.append(dongnghia[i][0].replace('_', ' '))
            #print(list_dongnghia)

    results = []
    for word in list_dongnghia:
        key = "description : " + "\"" + sentence + "\""

        result = solr.search(key)

        results.append(result)

    return results

text_search = "Trường Giang"
results = searchDescription1(text_search)

# print(results.docs)

# n = json.dumps(results.docs)
# o = json.loads(n)

# print('----------------------')
# print(type(o))

# # Write JSON file
# import io

# try:
#     to_unicode = unicode
# except NameError:
#     to_unicode = str


# with io.open('data.json', 'w', encoding='utf8') as outfile:
#     str_ = json.dumps(results.docs, ensure_ascii=False)
#     outfile.write(to_unicode(str_))
 
# # Read JSON file
# with open('data.json') as data_file:
#     data_loaded = json.load(data_file)
 
# print(data_loaded)

# import json
# with open('data.json', 'w', encoding='utf8') as outfile:
#     json.dumps(results.docs, outfile)



#print(results)

# for result in results:
#     n = json.dumps(result)
#     o = json.loads(n)
#     print('--------------------------------')
#     print(o)

#     break
    


print(type(results.docs[0]))









