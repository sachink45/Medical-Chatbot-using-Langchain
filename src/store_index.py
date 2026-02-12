from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import config


# Initialize embedding model
embedding_model = OpenAIEmbeddings(
    model=config.EMBEDDING_MODEL_NAME
)

# Initialize Pinecone client
pc = Pinecone(api_key=config.PINECONE_API_KEY)


def create_or_load_index():

    if not pc.has_index(config.INDEX_NAME):
        pc.create_index(
            name=config.INDEX_NAME,
            dimension=config.VECTOR_DIMENSION,
            metric=config.METRIC,
            spec=ServerlessSpec(
                cloud=config.CLOUD,
                region=config.REGION
            )
        )

    # if index is already present then load it from existing vector
    vector_store = PineconeVectorStore.from_existing_index(
        embedding=embedding_model,
        index_name=config.INDEX_NAME
    )

    return vector_store


def get_retriever():
    vector_store = create_or_load_index()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": config.TOP_K}
    )

    return retriever
