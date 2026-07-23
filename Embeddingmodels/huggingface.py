from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=["my name is alokit",
       "I am fine "]
vector = embedding.embed_documents(texts)
print(len(vector))
print(len(vector[1]))