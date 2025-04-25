count_card = int(input('Количество видеокарт: '))
list_model_cards = []

def deletes_older_model(list_models: list[int]) -> list[int]:
    old_model = max(list_models)
    for model in list_models:
        if model == old_model:
            list_models.remove(model)
    return list_models

for num in range(1, count_card + 1):
    model_card = int(input(f'Видеокарта {num}: '))
    list_model_cards.append(model_card)
    
print('Старый список видеокарт:', list_model_cards)
print('Новый список видеокарт:', deletes_older_model(list_model_cards))