import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def selrialize(self, song, format):
        if format == "JSON":
            return self.serialize_to_json(song)

        elif format == "XML":
            return self.serialize_to_xml(song)

        else:
            raise ValueError(format)

    def serialize_to_json(self, song):
        song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
        return json.dumps(song_info)

    def serialize_to_xml(self, song):
        song_info = et.Element("song", attrib={"id": str(song.song_id)})
        title = et.SubElement(song_info, "title")
        title.text = song.title
        artist = et.SubElement(song_info, "artist")
        artist.text = song.artist
        return et.tostring(song_info, encoding="unicode")


if __name__ == "__main__":
    deftones = Song(1, "Brilhant City", "Deftones")
    serializer = SongSerializer()
    print(serializer.selrialize(deftones, "JSON"))
    print(80 * "-")
    print(serializer.selrialize(deftones, "XML"))
