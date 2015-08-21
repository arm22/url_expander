from django.forms import widgets 
from rest_framework import serializers
from url_app.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:         
        model = Post         
        fields = ('org_url', 'fin_url', 'resp_code', 'title', 'pic')
    org_url = serializers.URLField()
    fin_url = serializers.URLField()
    resp_code = serializers.IntegerField()
    title = serializers.CharField()
    pic = serializers.URLField()

def create(self, validated_data):
       """      Create and return a new `Users` instance, given the validated data.      """      
       return Post.objects.create(**validated_data)

def update(self, instance, validated_data):      
    """      Update and return an existing `Users` instance, given the validated data.      """      
    instance.org_url = validated_data.get('org_url', instance.org_url)      
    instance.fin_url = validated_data.get('fin_url', instance.fin_url)      
    instance.resp_code = validated_data.get('resp_code', instance.resp_code)      
    instance.title = validated_data.get('title', instance.title)      
    instance.pic = validated_data.get('pic', instance.pic)      
    instance.save()      
    return instance