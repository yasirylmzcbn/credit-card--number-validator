class Luhn:
    # nothing
    def pass_luhn(self, acct):
        try:
            acct = int(acct)
        except:
            print("acct contains non-number characters")
            return False
        else: acct = str(acct)
        strr = acct[::-1]
        sum = 0
        for i in range(1, len(strr)):
            if i % 2 == 0:
                sum += int(strr[i])
            else:
                if int(strr[i]) > 4:
                    sum += int(strr[i])*2 - 9
                else:
                    sum += int(strr[i])*2
        return (sum + int(strr[0])) % 10 == 0
        
    def is_amex(self, acct):
        try:
            acct = int(acct)
        except:
            print("acct contains non-number characters")
            return False
        else: acct = str(acct)
        if len(acct) != 15:
            return False
        if acct[0] == '34' or acct[0] == '37':
            return False
        bln = self.pass_luhn(acct)
        if bln:
            return True
        return False

    def is_visa(self, acct):
        try:
            acct = int(acct)
        except:
            print("acct contains non-number characters")
            return False
        else: acct = str(acct)
        if len(acct) != 13 and len(acct) != 16:
            return False
        if acct[0] != '4':
            return False

        bln = self.pass_luhn(acct)
        if bln:
            return True
        return False

    def is_mastercard(self, acct):
        try:
            acct = int(acct)
        except:
            print("acct contains non-number characters")
            return False
        acct = str(acct)
        if len(acct) != 16:
            return False
        if int(acct[0:2]) < 51 or int(acct[0:2]) > 55:
            return False
        if self.pass_luhn(acct):
            return True
        return False

    def is_discover(self, acct):
        try:
            acct = int(acct)
        except:
            print("acct contains non-number characters")
            return False
        else: acct = str(acct) 	
        if len(acct) != 16:
            return False
        if acct[:4] != '6011':
            return False
        bln = self.pass_luhn(acct)
        if bln:
            return True
        return False

    def is_valid_cc(self, acct):
        bln = self.is_amex(acct)
        if bln:
            return True
        bln = self.is_discover(acct)
        if bln:
            return True
        bln = self.is_mastercard(acct)
        if bln:
            return True
        bln = self.is_visa(acct)
        if bln:
            return True
        return False
