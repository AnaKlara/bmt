from xml.sax.saxutils import XMLFilterBase, XMLGenerator
from xml.sax import make_parser
import os


class FileFilter(XMLFilterBase):

    def __init__(self, tag_names_to_exclude, parent=None):
        super().__init__(parent)
        self._tag_names_to_exclude = tag_names_to_exclude
        self._project_1_count = 0

    def _forward_events(self):
        # will return True when we are not inside a project1 element
        return self._project_1_count == 0

    def startElement(self, name, attrs):
        if name in self._tag_names_to_exclude:
            self._project_1_count += 1

        if self._forward_events():
            super().startElement(name, attrs)

    def endElement(self, name):
        if self._forward_events():
            super().endElement(name)

        if name in self._tag_names_to_exclude:
            self._project_1_count -= 1
        if name == "RECORD":
            super().characters("\n")


    def characters(self, content):
        if self._forward_events():
            super().characters(content.rstrip('\n'))

def main():
    tag_names_to_exclude = {'EXTRACT','SOURCE','CITATIONS','REFERENCES','AUTHORS', 'MEDLINENUM', 'RECORDNUM','CITE','TOPIC','PAPERNUM','MAJORSUBJ','ABSTRACT','MINORSUBJ'}
    reader = FileFilter(tag_names_to_exclude, make_parser())
    userFolderPath = os.getcwd()[0:-14]

    with open('titulo.xml', 'w') as f:
        handler = XMLGenerator(f)
        reader.setContentHandler(handler)
        reader.parse(userFolderPath + "CysticFibrosis2/data/cf79.xml")


if __name__ == "__main__":
    main()
