from ast import Tuple
from re import M
from unittest import result
from graphene import (
    Field,
    Int,
    List,
    ObjectType,
    Schema,
    String
    )
from command import mycursor

from collections import namedtuple
mycursor.execute("SELECT * FROM Productdata")
results = []
for x in mycursor:
    Person=namedtuple("Person",['name','description','sku','price','image'])

    data={
        Person(x[0],x[1],x[2],x[3],x[4])
    }
    results.append(data)

"""
class ItemType:
    name:str,
    description:str,
    sku:str,
    price:int,
    image:str

"""

class ItemType(ObjectType):
    name=String()
    description =String()
    sku =String()
    price =Int()
    image =String()

    #resolvers

    def resolve_name(item,info):
        return item.name

    def resolve_description(item,info):
        return item.description

    def resolve_sku(item,info):
        return item.sku

    def resolve_price(item,info):
        return item.price

    def resolve_image(item,info):
        return item.image

class Query(ObjectType):
    all_items=List(ItemType)
    
    def resolve_all_items(root,info):
        return results


#schema
schema=Schema(query=Query)


#query
query_string="{allItems{name}}"

print(schema.execute(query_string))

# print(result)