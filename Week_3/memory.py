import chromadb
import uuid

# Persistent database
client = chromadb.PersistentClient(path="memory_storage")

# Collection
collection = client.get_or_create_collection(
    name="user_preferences"
)

# Save preference
def save_preference(text):
    collection.add(
        documents=[text],
        ids=[str(uuid.uuid4())]
    )

# Search preference
def search_preference(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    if results["documents"]:
        return results["documents"][0]
    else:
        return []