from serializers import JsonSerializer, XmlSerializer
from yaml_serializer import YamlSerializer


class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format("JSON", JsonSerializer)
factory.register_format("XML", XmlSerializer)
factory.register_format("YAML", YamlSerializer)


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


if __name__ == "__main__":
    import songs

    song = songs.Song("1", "Radinat City", "Deftones")
    nirvana = songs.Song("2", "Peniroyal Tea", "Nirvana")
    # breakpoint()
    serializer = ObjectSerializer()
    print(serializer.serialize(nirvana, "JSON"))
    print(serializer.serialize(nirvana, "XML"))
    print(serializer.serialize(nirvana, "YAML"))
