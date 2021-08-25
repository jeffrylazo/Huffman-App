class Incorrect_Key_Message_Pair(Exception):
    def __init__(self, unused_key):
        self.msg = f"Unable to decompress. {unused_key} does not exist in the compressed message."

class Insufficient_Decryption_Key(Exception):
    msg = "Unable to decompress. Decryption key is not sufficent."

class Equal_Binary_Sequencies(Exception):
    msg = "Unable to decompress. Decryption key contains two or more equal binary sequences."

class Empty_Input(Exception):
    def __init__(self, process):
        self.msg = f"Unable to {process.lower()}. Empty input field."