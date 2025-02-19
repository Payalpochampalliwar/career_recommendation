from rest_framework import serializers
from .models import CareerPath, CareerDetail

class CareerCategorySerializer(serializers.Serializer):
    category = serializers.CharField()

class CareerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerDetail
        fields = '__all__'

class CareerPathSerializer(serializers.ModelSerializer):
    details = CareerDetailSerializer(read_only=True)

    class Meta:
        model = CareerPath
        fields = ['id', 'category', 'name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        career = CareerPath.objects.create(**validated_data)
        CareerDetail.objects.create(career=career, **details_data)
        return career

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', None)
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if details_data:
            detail_instance = instance.details
            detail_instance.description = details_data.get('description', detail_instance.description)
            detail_instance.salary_range = details_data.get('salary_range', detail_instance.salary_range)
            detail_instance.required_courses = details_data.get('required_courses', detail_instance.required_courses)
            detail_instance.skills_required = details_data.get('skills_required', detail_instance.skills_required)
            detail_instance.save()

        return instance
