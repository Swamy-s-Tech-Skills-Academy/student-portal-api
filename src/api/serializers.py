from rest_framework import serializers
from students.models import Student


# Serializers define the API representation.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Replace with your model, e.g., `YourModel`
        fields = '__all__'  # Specify fields explicitly if needed


# Example custom serializer
# class CustomDataSerializer(serializers.Serializer):
#     field1 = serializers.CharField(max_length=100)
#     field2 = serializers.IntegerField()

#     def validate_field1(self, value):
#         if not value.isalpha():
#             raise serializers.ValidationError(
#                 "Field1 must contain only alphabetic characters.")
#         return value
