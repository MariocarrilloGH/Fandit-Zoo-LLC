from rest_framework import serializers
from .models import Zoo, Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["nombre_vulgar", "nombre_cientifico", "familia", "en_peligro"]

class ZooSerializer(serializers.ModelSerializer):
    animales = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    animales_detalle = AnimalSerializer(many=True, read_only=True, source="animales")

    class Meta:
        model = Zoo
        fields = ["id", "nombre", "ciudad", "pais", "tamano_m2", "presupuesto_anual", "animales", "animales_detalle"]

    def create(self, validated_data):
        animales_data = validated_data.pop("animales", [])
        zoo = Zoo.objects.create(**validated_data)
        for nombre_cientifico in animales_data:
            try:
                animal = Animal.objects.get(nombre_cientifico=nombre_cientifico)
                zoo.animales.add(animal)
            except Animal.DoesNotExist:
                pass
        return zoo

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        animales = instance.animales.all()
        rep["cantidad_animales"] = animales.count()
        familias = {}
        for a in animales:
            familias.setdefault(a.familia, []).append(a.nombre_vulgar)
        rep["animales_por_familia"] = familias
        return rep