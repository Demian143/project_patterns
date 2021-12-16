import yaml
import factory.serializer.serializers as serializers


class YamlSerializer(serializers.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
