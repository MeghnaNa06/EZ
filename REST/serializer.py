from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    Username=serializers.CharField(max_length=10)
    Frist_name=serializers.CharField(max_length=10)
    Last_name=serializers.CharField(max_length=10)
    email_id=serializers.CharField(max_length=20)
    is_staff=serializers.CharField(max_length=10)
    

    def __str__(self):
        return "Dummy Serialzer Object"
    
