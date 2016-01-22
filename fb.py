import facebook
import json

token = 'CAACEdEose0cBAC5i7z6m1JhOMGhlgkFjAldpqTD8epW0Sgmy1D5pvO5Bx8ErliNe6wZCc0T2RzLWJ1nXJ3nFgDJvmPpyqg2aC3otahXZBxDi3eSaHKzuc3ZCKno4iHoAjPY9BZCH0UdqFdN6QFnwyEYrsaH0Lx7w4bvNO8WdN6QIuxM6mZAPyZAQ2el2bbdTRG9NWkSiO2F8mZCmi7QPQdC'

graph = facebook.GraphAPI(token)

page_name = "XiaomiMalaysia"
status = graph.get_object(page_name+"/statuses")

print str(status).encode('utf-8')

f = open('fb-results.json','w')
f.write(json.dumps(status, indent = 4))
f.close()
