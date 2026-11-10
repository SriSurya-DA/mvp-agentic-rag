from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import engine

#Data load
loader = PyPDFLoader("company_data.pdf")
text=loader.load()
#print(len(text))

# Chuncking
# RecursiveCharacterTextSplitter -- It will split line wise, sentence wise, paragraph wise

data_splitter=RecursiveCharacterTextSplitter(

    chunk_size=120,
    chunk_overlap=20
)

chunk=data_splitter.split_documents(text)

# engine.add_documents(chunk)
# Due to API_Token limitation, skipping the above one
# Choosing the below-method

"""
import time

batch_size = 20

for i in range(0, len(chunk), batch_size):

    batch = chunk[i:i + batch_size]

    try:
        engine.add_documents(
            documents=batch,
            ids=[f"chunk_{j}" for j in range(i, i + len(batch))]
        )

        print(f"Successfully processed {i + len(batch)}/{len(chunk)}")

        time.sleep(10)

    except Exception as e:
        print(f"Error processing batch starting at {i}: {e}")
        print("Wait before retrying this batch.")
        break

        """

# After Completing the 1st 100 chunk vectorization, using the below-method

import time

batch_size = 20

for i in range(100, len(chunk), batch_size):
    batch = chunk[i:i + batch_size]
    ids = [f"chunk_{j}" for j in range(i, i + len(batch))]

    for attempt in range(5):
        try:
            engine.add_documents(
                documents=batch,
                ids=ids
            )

            print(f"Successfully processed {i + len(batch)}/{len(chunk)}")
            break

        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                wait_time = 60 * (attempt + 1)
                print(f"Rate limit reached. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise
    else:
        print(f"Failed to process batch starting at {i}")
        break