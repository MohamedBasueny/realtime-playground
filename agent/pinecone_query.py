# import os
# from openai import OpenAI
# import pinecone
# from typing import List, Union
# import time
# import asyncio
# from dotenv import load_dotenv

# load_dotenv()

# async def query_pinecone(query: Union[str, dict], top_k: int = 1) -> List[str]:
#     """
#     Query Pinecone index for realated vetinary content
    
#     Args:
#         query (Union[str, dict]): Either the query text directly or a dict with query_text key
#         top_k (int): Number of results to return
    
#     Returns:
#         List[str]: List of matching text content
#     """
#     # Handle both string and dict input
#     query_text = query if isinstance(query, str) else query.get('query_text')
#     if not query_text:
#         raise ValueError("No query text provided")

#     # API keys and configuration
#     index_name = "vetpulse"

#     # Initialize OpenAI
#     client = OpenAI()

#     # Initialize Pinecone
#     pc = pinecone.Pinecone()
    
#     # Generate embedding for the query text
#     response = client.embeddings.create(
#         input=[query_text],
#         model="text-embedding-3-small"
#     )
#     query_embedding = response.data[0].embedding

#     # Initialize Pinecone index and query
#     index = pc.Index(index_name)
#     results = index.query(
#         namespace="",
#         vector=query_embedding,
#         top_k=top_k,
#         include_values=False,
#         include_metadata=True
#     )

#     # Extract only the texts from results
#     texts = [match['metadata'].get('text', '') for match in results['matches']]
#     print(f"Query_tool was called successfully with query_results: '{query_text}', output: {texts}")
#     return texts

# if __name__ == "__main__":
#     # Example usage
#     query = input("Enter your query: ")
#     start_time = time.time()
#     results = asyncio.run(query_pinecone(query))
#     duration = time.time() - start_time

#     for i, text in enumerate(results, 1):
#         print(f"\nResult {i}:")
#         print(text)
#         print("---")
#     print(f"\nQuery execution time: {duration:.2f} seconds")

