# TESTCASES.md

## 1. Сохранить объявление

### POST_01 — Успешное сохранение объявления

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:
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

###### Ожидаемый результат:
- HTTP статус 200 (Request successful)
- В ответе тело:
{
    "status": "Сохранили объявление - {Уникальный идентификатор}"
}

### POST_02 — Cохранение объявления без обязательного поля sellerID

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:
{
  "sellerID": 0,
  "name": "Seller_10",
  "price": 700,
  "statistics": {
    "likes": 6,
    "viewCount": 14,
    "contacts": 4
  }
}

###### Ожидаемый результат:
- HTTP статус 400 (Bad Request)
- В ответе тело:
{
    "result": {
        "message": "поле sellerID обязательно",
        "messages": {}
    },
    "status": "400"

}
### POST_03 — Cохранение объявления c заменой значения поля name со строкового типа на целочисленный тип

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:
{
  "sellerID": 32123233,
  "name": 3,
  "price": -700,
  "statistics": {
    "likes": -6,
    "viewCount": -14,
    "contacts": -4
  }
}

###### Ожидаемый результат:
- HTTP статус 400 (Bad Request)
- В ответе тело:
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявления"

}

### POST_04 — Cохранение объявления c пустой строкой поля name

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:
{
  "sellerID": 321232233,
  "name": "",
  "price": -700,
  "statistics": {
    "likes": -6,
    "viewCount": -14,
    "contacts": -4
  }
}

###### Ожидаемый результат:
- HTTP статус 400 (Bad Request)
- В ответе тело:
{
    "result": {
        "message": "поле name обязательно",
        "messages": {}
    },
    "status": "400"
}

### POST_05 — Cохранение объявления c пустым телом

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:

###### Ожидаемый результат:
- HTTP статус 400 (Bad Request)
- В ответе тело:
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передан объект - объявление"

}

### POST_06 — Проверка обязательности полей

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item без поля sellerID
###### 2. Отправить POST baseUrl/api/1/item без поля name
###### 3. Отправить POST baseUrl/api/1/item без поля price
###### 4. Отправить POST baseUrl/api/1/item без поля statistics

###### Ожидаемый результат:
- В каждом случае сервер возвращает HTTP 400
- В ответе тело:
{
    "result": {
        "message": "поле {Удаленное поле} обязательно",
        "messages": {}
    },
    "status": "400"

}

### POST_07 — Успешное сохранение объявления по уже созданному SellerID

##### Шаги:

###### 1. Отправить POST baseUrl/api/1/item с телом:
{
  "sellerID": 488283,
  "name": "w",
  "price": -700,
  "statistics": {
    "likes": 2,
    "viewCount": -14,
    "contacts": -4
  }
}

###### Ожидаемый результат:
- HTTP статус 200 (Request successful)
- В ответе тело:
{
    "status": "Сохранили объявление - {Уникальный идентификатор}"
}

## 2. Получение всех объявлении по sellerID (GET baseUrl/api/1/item/{id})

### GET-01 — Получение существующих объявлении

##### Шаги:

###### 1. Отправить GET baseUrl/api/1/sellarID/item с sellerID : 488283

###### Ожидаемый результат:
- HTTP статус 200 (Request successful)
- В ответе массив:
[
{
        "createdAt": "2025-12-29 16:36:15.168656 +0300 +0300",
        "id": "25c4a7ed-c175-4c04-96f1-372faf899f0d",
        "name": "Seller_10",
        "price": 700,
        "sellerId": 488283,
        "statistics": {
            "contacts": 4,
            "likes": 6,
            "viewCount": 14
        }
    },
    {
        "createdAt": "2025-12-29 17:33:47.173598 +0300 +0300",
        "id": "c6815627-f498-4639-a77b-320f6cdb11d9",
        "name": "w",
        "price": -700,
        "sellerId": 488283,
        "statistics": {
            "contacts": -4,
            "likes": 2,
            "viewCount": -14
        }
    }
]
### GET-02 — Получение существующих объявлении по несуществующему sellerID

##### Шаги:

###### 1. Отправить GET baseUrl/api/1/sellarID/item с sellerID : 2300421

###### Ожидаемый результат:
- HTTP статус 200 (Request successful)
- В ответе пустой массив:
[]
