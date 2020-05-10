import pickle

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from sklearn.feature_extraction.text import TfidfVectorizer


def get(request):
    return HttpResponse("<pre>Hello world</pre>")


@api_view(['POST'])
def post_test(request):
    if request.method != 'POST':
        return JsonResponse({"response": "Wrong request type. Please use post"})
    comment = request.POST.get("key")
    model = pickle.load(open("bgreview/model/model.pkl", "rb"))
    vocabulary = pickle.load(open("bgreview/model/vocab.pkl", "rb"))
    vectorizer = TfidfVectorizer(vocabulary=vocabulary)
    comment = vectorizer.fit_transform([comment])
    prediction = model.predict(comment)
    return JsonResponse({"response": round(prediction[0], 1)})
