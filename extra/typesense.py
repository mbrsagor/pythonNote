# pip install typesense

import typesense

client = typesense.Client({
    'nodes': [{'host': 'localhost', 'port': '8108', 'protocol': 'http'}],
    'api_key': 'xyz'
})

schema = {
    "name": "books",
    "fields": [
        {"name": "title", "type": "string"},
        {"name": "author", "type": "string"},
        {"name": "ratings", "type": "int32"}
    ],
    "default_sorting_field": "ratings"
}
client.collections.create(schema)

documents = [
    {"title": "Book 1", "author": "Author1", "ratings": 24},
    {"title": "Book 2", "author": "Author2", "ratings": 31},
    {"title": "Book 3", "author": "Author3", "ratings": 30}
]
client.collections['books'].documents.import_(documents)

# Run
print(client.collections['books'].documents.search({
    'query_by': 'title,author',
    'q': 'boo'
}))
