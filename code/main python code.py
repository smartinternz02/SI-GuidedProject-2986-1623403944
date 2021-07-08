from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-26nfu4gqvyxcmu556d5ny604qqnb18zdxg7nk1s6d8gu", "5f55403d7e64e3f62356312c03a4a8f0",
                  url="https://apikey-v2-26nfu4gqvyxcmu556d5ny604qqnb18zdxg7nk1s6d8gu:5f55403d7e64e3f62356312c03a4a8f0@af1bea6a-629e-4a60-a77e-96164b416359-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "gas_sensor"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "1001",
                    "name":"keerthi"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']  #search by id, if id=1001   

print("---------------")
print("the data with id =1001 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['1001'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['gaslevel'] = 55

# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']     
# Iterate over the result collection
print (result)
