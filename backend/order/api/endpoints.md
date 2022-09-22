# order API endpoints
***
**endpoint:** api/order/list/

**method:** GET

**serializer:** OrderListSerializer

**view:** OrderListAPIView

**filterset_fields:** ['is_delivered', 'shipping_address']


## JSON
```
[
    {
        "id": 1,
        "order_key": "TR-123456789",
        "total_price": 100.0,
        "is_delivered": true,
        "shipping_address": {
            "id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",
            "country": {
                "id": 228,
                "iso2": "TR",
                "name": "Turkey",
                "region": "Asia"
            },
            "address_name": "Home",
            "first_name": "Berke",
            "last_name": "Karataş",
            "company_name": null,
            "phone_number": "+905393182715",
            "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
            "street_address_2": null,
            "postal_code": "34055",
            "city": "Eyüpsultan",
            "city_area": "İstanbul",
            "user": 3
        },
        "shipping_method": 0
    }
]
```
***
**endpoint:** api/order/detail/<order_key>/

**method:** GET

**serializer:** OrderDetailSerializer

**view:** OrderDetailAPIView


## JSON
```
{
    "id": 1,
    "order_key": "TR-123456789",
    "user": {
        "username": "customer",
        "email": "customer@gmail.com",
        "first_name": "Berke",
        "last_name": "Karataş"
    },
    "is_paid": false,
    "paid_date": null,
    "payment_method": "Bank Account",
    "total_price": 100.0,
    "is_delivered": true,
    "delivered_date": "2022-09-17T11:12:55Z",
    "shipping_address": {
        "id": "8ed6ce48-b6e2-479a-90da-8d6c5b949551",
        "country": {
            "id": 228,
            "iso2": "TR",
            "name": "Turkey",
            "region": "Asia"
        },
        "address_name": "Home",
        "first_name": "Berke",
        "last_name": "Karataş",
        "company_name": null,
        "phone_number": "+905393182715",
        "street_address_1": "Düğmeciler Mahallesi Şifa Yokuşu Sokak No:36/10",
        "street_address_2": null,
        "postal_code": "34055",
        "city": "Eyüpsultan",
        "city_area": "İstanbul",
        "user": 3
    },
    "shipping_method": 0,
    "shipping_price": 20.0,
    "tracking_number": null,
    "order_items": [
        {
            "id": 1,
            "item_key": "TR-123456789-123456789",
            "product": {
                "id": 1,
                "name": "AUDI ERA 06A919501A",
                "oem_code": "06A919501A",
                "slug": "audi-era-06a919501a-merc-aud3-era43-06a919501a",
                "sku": "MERC-AUD3-ERA43-06A919501A",
                "price_net": 78.14
            },
            "quantity": 3,
            "price": 100.0
        }
    ],
    "created_date": "2022-09-17T11:13:55.048331Z",
    "updated_date": "2022-09-17T11:13:55.048331Z"
}
```
***
**endpoint:** api/order/item/detail/<item_key>/

**method:** GET

**serializer:** OrderItemDetailSerializer

**view:** OrderItemDetailAPIView


## JSON
```
{
    "id": 1,
    "item_key": "TR-123456789-123456789",
    "product": {
        "id": 1,
        "name": "AUDI ERA 06A919501A",
        "oem_code": "06A919501A",
        "slug": "audi-era-06a919501a-merc-aud3-era43-06a919501a",
        "sku": "MERC-AUD3-ERA43-06A919501A",
        "price_net": 78.14
    },
    "quantity": 3,
    "price": 100.0
}
```
***
**endpoint:** api/order/create/

**method:** POST

**view:** OrderCreateAPIView


## Fields
- **is_paid** - bool -> True
- **payment_method** - string -> Bank
- **total_price** - double -> 100.0
- **is_delivered** - bool -> True
- **shipping_address** - FK -> 1
- **shipping_method** - int -> 0
- **shipping_price** - double -> 20.0
- **cartItems** - List -> ['..','..']


## JSON
```
...
```