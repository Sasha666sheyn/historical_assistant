import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from .models import War

def search_faiss(query, top_k=5):
    model = SentenceTransformer('all-mpnet-base-v2')
    query_embedding = model.encode(query).astype('float32')

    db_embeddings = War.objects.all().values_list('embedding', flat=True)
    # Преобразуем данные из базы данных в numpy array
    index = faiss.IndexFlatIP(768)  # 768 - размерность векторов
    index.add(np.array([np.array(x) for x in db_embeddings]).astype('float32'))

    D, I = index.search(np.array([query_embedding]), k=5)  # k=5 - возвращает 5 ближайших

    results = [War.objects.get(pk=i + 1) for i in I[0]]  # +1 т.к. индексы начинаются с 0

    return results
