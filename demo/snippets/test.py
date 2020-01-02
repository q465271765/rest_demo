from snippets.models import Snippet
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data

content = JSONRenderer().render(serializer.data)
content


import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data


from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))

if __name__ == '__main__':
    print(serializer.data)