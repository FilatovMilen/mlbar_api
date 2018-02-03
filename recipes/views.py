from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class GenerateRecipe(APIView):
    queryset = Recipe.objects.all()

    def get(self, request, format=None):
        recipe = Recipe.objects.first()
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
