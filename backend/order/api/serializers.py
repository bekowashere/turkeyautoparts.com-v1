from rest_framework import serializers
from order.models import OrderItem, Order
from account.models import Address, CustomerUser
from world.models import Country
from autopart.models import Product

class UserInformationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    class Meta:
        model = CustomerUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'iso2', 'name', 'region')

class AddressSerializer(serializers.ModelSerializer):
    country = CountryDetailSerializer()

    class Meta:
        model = Address
        fields = '__all__'


# ORDER ITEM
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'oem_code', 'slug', 'sku', 'price_net')

class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'item_key', 'product', 'quantity', 'price')


# ORDER
class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    shipping_address = AddressSerializer()
    user = UserInformationSerializer()

    def get_order_items(self, obj):
        return OrderItemDetailSerializer(obj.get_all_items, many=True).data

    class Meta:
        model = Order
        fields = (
            'id',
            'order_key',
            'user',
            'is_paid',
            'paid_date',
            'payment_method',
            'total_price',
            'is_delivered',
            'delivered_date',
            'shipping_address',
            'shipping_method',
            'shipping_price',
            'tracking_number',
            'order_items',
            'created_date',
            'updated_date'
        )


class OrderListSerializer(serializers.ModelSerializer):
    shipping_address = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'order_key',
            'total_price',
            'is_delivered',
            'shipping_address',
            'shipping_method',
            # 'tracking_number',
        )



