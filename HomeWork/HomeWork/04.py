

# домашнее задание
# Примечание: Добавил уникальный идентификатор UUID. Это помогает отслеживать данные в базе.

import uuid

def add_qa_material():
    print(" --- Регистрация нового модуля курса QA --- ")
    
    # Тип материала
    material_type = input("Тип материала (книга/видео/чек-лист): ")
    
    # Стоимость с валидацией
    while True:
        try:
            price = float(input("Стоимость: "))
            if price > 100:
                break
            print("Ошибка: цена должна быть положительной.")
        except ValueError:
            print("Ошибка: введите число.")
            
            
    # Категория
    category = input("Категория (API/AUTO/UI|UX): ")
    
    # Генерируем короткий уникальный ID (первые 8 символов UUID)
    material_id = str(uuid.uuid4())[:8].upper()
    
    # Итоговое подтверждение
    print("\n[SUCCESS] Запись создана в системе обучения")
    print(f"ID: {material_id} | Тип: {material_type} | Цена: {price} | Категория: {category}")
    
if __name__ == "__main__":
    add_qa_material()

















