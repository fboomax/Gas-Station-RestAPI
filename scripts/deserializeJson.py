from django.core import serializers
import json

# Assuming your JSON string is stored in a variable called `json_data`
# Serialize the JSON using Django's built-in serialization methods
json_data = open('./data.json')

serialized_data = serializers.serialize('json', json.loads(json_data))

# Deserialize the JSON using Django's built-in deserialization methods
deserialized_data = serializers.deserialize('json', serialized_data)

# `deserialized_data` is now a generator object that you can iterate over to access the deserialized objects
for obj in deserialized_data:
    # `obj` is an instance of `django.core.serializers.base.DeserializedObject`
    # You can access the deserialized object using `obj.object`
    print(obj.object)
