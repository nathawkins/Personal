class Playfair:

    def __init__(self, key):
        self.message = ""
        self.key = key
        self.alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"

    def get_message(self, message):
        self.message = message

    def split(self):
        punc = [" ", "'", ".", ",", "?", "!"]
        self.message = "".join([x for x in self.message if x not in punc])
        self.pairs = [self.message[i:i + 2] for i in range(0, len(self.message), 2)]
        self.pairs = [x.upper() for x in self.pairs]

    def encrypt(self, message):
        self.key = self.key.upper()
        self.encrypt_alpha = ""
        for i in self.key:
            if i not in self.encrypt_alpha:
                self.encrypt_alpha += i

        for i in self.alphabet:
            if i not in self.encrypt_alpha:
                self.encrypt_alpha += i
        self.get_message(message)
        self.split()
        self.encrypted_pairs = []
        for pair in self.pairs:
            new_pair = ""
            for letter in pair:
                ind = self.alphabet.find(letter)
                if ind == -1:
                    new_pair += "Q"
                    continue
                new_pair += self.encrypt_alpha[ind]
            self.encrypted_pairs.append(new_pair)
        self.show_encrypt()

    def show_encrypt(self):
        print(" ".join(self.encrypted_pairs)+".")


    def decrpyt(self, encryption, key):
        if type(encryption) == type(str()):
            string_list = list(encryption)
            punc = [" ", "'", ".", ",", "?", "!"]
            string_list = [x for x in string_list if x not in punc]
            encryption_cleaned = "".join(string_list)

            self.decrypt_alpha = ""
            for i in key:
                if i not in self.decrypt_alpha:
                    self.decrypt_alpha += i.upper()

            for i in self.alphabet:
                if i not in self.decrypt_alpha:
                    self.decrypt_alpha += i


            self.decrypted_string = ""
            for letter in encryption_cleaned:
                ind = self.decrypt_alpha.index(letter)
                if ind == "-1":
                    self.decrypted_string += "Q"
                    continue
                self.decrypted_string += self.alphabet[ind]

            print(self.decrypted_string)

        if type(encryption) == type(list()):
            self.decrpyt("".join(encryption), key)


pf = Playfair("rocketman")
pf.encrypt("my name is nat")
pf.decrpyt("GY HR GE NP HR S.", "death")
pf.decrpyt(["LY", "MD", "LH", "GR", "MD", "S."], "death")
