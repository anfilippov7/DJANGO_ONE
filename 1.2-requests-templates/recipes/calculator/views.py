from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cocktail': {
        'клубника, г': 300,
        'молоко, г': 300,
        'мороженое, г': 150,
        'сахар, ст.ложки': 2,
    },
    # можете добавить свои рецепты ;)
}


def dish_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    data_copy = {dish: DATA[dish].copy()}
    for keys, values in data_copy[dish].items():
        data_copy[dish][keys] = values*servings
    context = {
        'recipe': data_copy[dish]
    }
    return render(request, 'calculator/index.html', context)





