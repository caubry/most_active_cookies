from abc import abstractmethod

from exceptions.parsing_error import ParsingError


class Parser:
    NO_PARSER_FOUND = "Unable to find the correct parser for the file"

    @abstractmethod
    def parse(self, filepath):
        raise ParsingError(filepath, Parser.NO_PARSER_FOUND)

    @staticmethod
    def can_handle_file(filepath, ext):
        return not filepath or filepath.endswith(ext)
