'''from django.conf import settings
settings.configure()
from .models import War


for obj in War.objects.filter(text_embedding__isnull=True): # Только объекты без векторов
    obj.save()  # save() вызовет generate_embedding()'''


from .models import War




from sentence_transformers import SentenceTransformer
import numpy as np

def jkk():
    # Получаем не эмбеддированные предложения
    unembeded_objs = War.objects.filter(embedding__isnull=True)
    sentences = list(unembeded_objs.values_list('description', flat=True))  # Получаем список "description"
    # сортируем список предложений по длинне
    length_sorted_idx = np.argsort([len(s) for s in sentences])
    sentences_sorted = [sentences[int(idx)] for idx in length_sorted_idx]
    # преобразуем предложения в векторы
    model = SentenceTransformer("all-mpnet-base-v2")
    embeddings = model.encode(sentences_sorted)

    # Сохраняем векторы в базу данных (ВНИМАНИЕ: порядок важен!)
    # Создаем список объектов War в том же порядке, что и отсортированные эмбеддинги
    sorted_objs = [unembeded_objs[int(idx)] for idx in length_sorted_idx]

    for i, obj in enumerate(sorted_objs):  # перебираем отсортированный список объектов, i - это индекс
        obj.embedding = embeddings[i].tolist()
        obj.save()

