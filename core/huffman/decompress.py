import ast
import flask
from core.huffman.exceptions import Empty_Input, Incorrect_Key_Message_Pair, Insufficient_Decryption_Key, Equal_Binary_Sequencies

class Huff_Dec():
    '''Summary: This class decodes a string using Huffman coding. \n
    Object Initialization: Huff_Dec(compressed_message = '...', huffman_code={...}).'''

    def __init__(self, compressed_message:str, huffman_code:str):
        '''Constructor and method manager. Private class variables'''
        # Class variables
        self.__compressed_message = compressed_message
        self.__original_message = str()
        self.__huffman_code = dict()
        self.__used_keys = set()
        self.__unused_key = set()
        self.fails = True

        # Method manager and exeption handler
        try:
            if ((len(self.__compressed_message) == 0) or (len(huffman_code) == 0)):
                raise Empty_Input("decompress")
            self.__huffman_code = {items[1]:items[0] for items in ast.literal_eval(huffman_code)}
            if len(self.__huffman_code) < len(ast.literal_eval(huffman_code)):
                raise Equal_Binary_Sequencies
            self.__decompress_message__()
            self.fails = False
        except Empty_Input:
            flask.flash(Empty_Input("decompress").msg,"error")
        except SyntaxError:
            flask.flash("Incorrect key format.","error")
        except ValueError:
            flask.flash("Incorrect key format.","error")
        except Equal_Binary_Sequencies:
            flask.flash (Equal_Binary_Sequencies.msg, "error")
        except Insufficient_Decryption_Key:
            flask.flash(Insufficient_Decryption_Key.msg,"error")
        except Incorrect_Key_Message_Pair:
            flask.flash(Incorrect_Key_Message_Pair(self.__unused_key).msg,"error")

    def __decompress_message__(self):
        '''Private Method: Decodes the selected message.'''
        # Local variables
        code_to_test = str()
        code_tested = ''

        # Decoding strategy
        for bit in self.__compressed_message:
            code_to_test = code_to_test + bit
            if code_to_test in self.__huffman_code.keys():
                code_tested = code_tested + code_to_test
                self.__original_message = self.__original_message + self.__huffman_code[code_to_test]
                self.__used_keys.add(code_to_test)
                code_to_test = ''
        if not (self.__used_keys == set(self.__huffman_code.keys())):
            self.__original_message = ''
            for key, value in self.__huffman_code.items():
                if key not in self.__used_keys:
                    self.__unused_key = (value,key)
                    break
            raise Incorrect_Key_Message_Pair(self.__unused_key)
        if not (code_tested == self.__compressed_message):
            self.__original_message = ''
            raise Insufficient_Decryption_Key

    def get_compressed_message(self):
        '''Public Method: Returns the encoded message as a string.'''
        return self.__compressed_message

    def get_decompressed_message(self):
        '''Public Method: Returns the original message as a string.'''
        return self.__original_message

    def get_decompressed_message_HTML(self):
        '''Public Method: Returns the original message as a string.'''
        return list(self.__original_message.split('\r\n'))
