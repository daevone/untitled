from mayan_api_client import API

api = API(host='http://192.168.22.188:81', username='Dave', password='dbvjdu123')



with open('/home/ucitel/Plocha/bcrypt.c') as file_object:
    response = api.documents.documents.post({'document_type': 2}, files={'file': file_object})

#print (response)


#print(api.document_indexing.indexes.get())
#print(api.metadata.metadata_types.get())
print(api.documents.documents_type.get())