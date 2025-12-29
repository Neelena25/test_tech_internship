# TESTCASES.md

## 1. Сохранить объявление

### POST_01 — Успешное сохранение объявления

Шаги:

1. Отправить POST baseUrl/api/1/item с телом:
{
  "sellerID": 488283,
  "name": "Seller_10",
  "price": 700,
  "statistics": {
    "likes": 6,
    "viewCount": 14,
    "contacts": 4
  }
}

Ожидаемый результат:
- HTTP статус 200 (Request successful)
- В ответе тело:
{
    "status": "Сохранили объявление - {Уникальный идентификатор}"
}