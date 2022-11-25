from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['quantity', 'product', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for item in positions:
            StockProduct.objects.create(quantity=item['quantity'], price=item['price'], product_id=item['product'].id,
                                        stock_id=stock.id)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)


        for item in positions:
            print(instance.id)
            print(item['product'].id, item['quantity'], item['price'], item['product'].id, stock.id)
            StockProduct.objects.filter(stock_id=instance.id).filter(product_id=item['product'].id).update(quantity=item['quantity'], price=item['price'],
                                        product_id=item['product'].id, stock_id=stock.id)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
