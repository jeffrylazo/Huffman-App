
import flask
from core.huffman.exceptions import Empty_Input

class Node_Value():
    '''Summary: This class instantiates the data of a Huffman node, which is defined as a list composed by a symbol and its frequency. \n
    Object Initialization: Node_Value(symbol='a', frequency=0.05).'''

    def __init__(self, symbol:str, frequency:float):
        '''Contructor. Public class variables: data.'''
        self.data = [symbol,frequency]

class Tree_Node():
    '''Summary: This class interconnects two nodes on the same level with another node in a higher level. \n
    Object Initialization: Tree_Node(value = Node_Value('',0)).'''

    def __init__(self, value:Node_Value):
        '''Contructor. Public class variables: value, left_node, right_node.'''
        self.value = value
        self.left_node = None
        self.right_node = None

    def isLeaf(self):
        '''Public Method: Determines whether a Huffman node is a leaf or not.'''
        if self.left_node == self.right_node and self.right_node == None:
            return True
        return False

class Huff_Com():
    '''Summary: This class compresses a string using Huffman coding. \n
    Object Initialization: Huff_Com(message = '...').'''

    def __init__(self, message:str):
        '''Contructor and method manager.'''
        # Class variables
        self.__original_message = message
        self.__compressed_message = str()
        self.__symbol_dict = dict()
        self.__code_dict = dict()
        self.fails = True

        # Method manager and exception handler
        try:
            if len(self.__original_message) == 0:
                raise Empty_Input("compress")
            self.__set_symbol_dict__()
            if (len(self.__symbol_dict) == 1):
                single_symbol = tuple(self.__symbol_dict.items())[0]
                self.__code_dict[single_symbol[0]] = '0'
            else:
                self.__set_base_nodes__()
                self.__create_tree__()
                self.__set_code_dict__(list(self.__symbol_dict.values())[0][1],'')
            self.__compress_message__()
            self.fails = False
        except Empty_Input:
            flask.flash(Empty_Input("compress").msg,"error")


    def __set_symbol_dict__(self):
        '''Private Method: Allocates the symbols and frequencies of the message as key and value in self.__symbol_dict.'''
        for symbol in self.__original_message:
            if symbol not in self.__symbol_dict.keys():
                self.__symbol_dict[symbol] = [0, None]
            self.__symbol_dict[symbol][0] += 1/len(self.__original_message)

    def __set_base_nodes__(self):
        '''Private Method: Creates Huffman nodes per symbol and allocates them as part of the value component in self.__symbol_dict.'''
        for key, value in self.__symbol_dict.items():
            self.__symbol_dict[key][1] = Tree_Node(Node_Value(key, value[0]))

    def __create_tree__(self):
        '''Private Method: Modifies the dictionary containing the symbols of the message until it is only composed by one key-value pair.'''
        while len(self.__symbol_dict.keys()) > 1:
            self.__createBranch__()

    def __createBranch__(self):
        '''Private Method: Creates a new branch in the Huffman Tree by combining the two symbols with the lowest frequency.'''   
        # Local variables
        counter = 0
        new_node = Tree_Node(value = Node_Value('',0))
        symbol = ''
        frequency = 0
        filter_keys = list()

        # Sort the elements in self.__symbol_dict in terms of the frequencies of each of its symbols
        self.__symbol_dict = dict(sorted(self.__symbol_dict.items(), key=lambda input: input[1][0]))

        # Update value of new_node and set its left_node and right_node
        for key, value in self.__symbol_dict.items():
            if counter == 2:
                break
            if counter == 1:
                new_node.right_node = value[1]
            if counter == 0:
                new_node.left_node = value[1]
            filter_keys.append(key)
            symbol += key
            frequency += value[0]
            counter += 1
        new_node.value.data = [symbol,frequency]

        # Pop the two lowest items from self.__symbol_dict
        for key in filter_keys:
            self.__symbol_dict.pop(key)

        # Add new_node to self.__symbol_dict
        self.__symbol_dict[symbol] = [frequency,new_node]

    def __set_code_dict__(self, currentNode:Tree_Node, codeVal:str):
        '''Private Method: Generates the Huffman Code by travelling thru the different nodes in the Huffman Tree.'''
        if currentNode.isLeaf():
            self.__code_dict[currentNode.value.data[0]] = codeVal
        if currentNode.left_node != None:
            self.__set_code_dict__(currentNode.left_node, codeVal+'0')
        if currentNode.right_node != None:
            self.__set_code_dict__(currentNode.right_node, codeVal+'1')

    def __compress_message__(self):
        '''Private Method: Compresses the symbols of the original message using Huffan coding.'''
        for symbol in self.__original_message:
            self.__compressed_message += self.__code_dict[symbol]

    def get_compressed_message(self):
        '''Public Method: Returns the encoded message as a string.'''
        return self.__compressed_message

    def get_original_message(self):
        '''Public Method: Returns the original message as a string.'''
        return self.__original_message

    def get_huffman_code(self):
        '''Public Method: Returns the Huffman code of the encoded message as a list.'''
        return list(self.__code_dict.items())
