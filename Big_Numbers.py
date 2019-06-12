def negative(a):
    if a[0] == "-":
        return a[1:]
    else:
        return "-" + a

def less(a, b):
    if len(a) == len(b):
        return a < b
    return len(a) < len(b)
    
def bit_add(a, b):
    return str(int(a) + int(b))
def bit_minus(a, b):
    return str(int(a) - int(b))
def bit_times(a, b):
    return str(int(a) * int(b))

def simple_add(a, b):
    sum_s = ""
    i = 1
    carry = 0
    while True:
        aBit = bBit = "0"
        if i > len(a) and i > len(b):
            break
        if i <= len(a):
            aBit = a[-i]
        if i <= len(b):
            bBit = b[-i]
        bit_sum = bit_add(aBit, bBit)
        if carry == 1:
            bit_sum = bit_add(bit_sum, "1")
        if int(bit_sum) > 9:
            carry = 1
            bit_sum = bit_sum[1:]
        else:
            carry = 0
        sum_s = bit_sum + sum_s
        i += 1
    if carry == 1:
        sum_s = "1" + sum_s
    return sum_s

def simple_minus(a, b):
    diff_s = ""
    i = 1
    borrow = 0
    while True:
        aBit = bBit = "0"
        if i > len(a) and i > len(b):
            break
        if i <= len(a):
            aBit = a[-i]
        if i <= len(b):
            bBit = b[-i]
        bit_diff = bit_minus(aBit, bBit)
        if borrow == 1:
            bit_diff = bit_minus(bit_diff, "1")
        if int(bit_diff) < 0:
            borrow = 1
            bit_diff = bit_add(bit_diff, "10")
        else:
            borrow = 0
        diff_s = bit_diff + diff_s
        i += 1
    length = len(diff_s)
    for i in range(length):
        if diff_s[i] != "0":
            diff_s = diff_s[i:]
            break
        if i == length - 1:
            diff_s = diff_s[-1]
            break
    return diff_s

def b_nb_times(a, b):
    prod_s = ""
    i = 1
    carry = 0
    while True:
        if i > len(b):
            break
        bBit = b[-i]
        bit_prod = bit_times(a, bBit)
        bit_prod = bit_add(bit_prod, str(carry))
        carry = int(bit_prod) // 10
        bit_prod = str(int(bit_prod) % 10)
        prod_s = bit_prod + prod_s
        i += 1
    if (carry != 0):
        prod_s = str(carry) + prod_s
    return prod_s

def simple_times(a, b):
    prod_s = ""
    i = 1
    while True:
        if i > len(a):
            break
        aBit = a[-i]
        nb_prod = b_nb_times(aBit, b)
        prod_s = simple_add(prod_s, (nb_prod + ("0" * (i-1))))
        i += 1
    return prod_s

def simple_floordiv(a, b):
    levels = [b_nb_times(i, b) for i in range(10)]
    i = len(b) - 1
    q = ""
    r = a[:i]
    while True:
        if i >= len(a):
            break
        if r != "0":
            divor = r + a[i]
        if less(divor, b):
            r = divor
            q += "0"
            i += 1
            continue
        bit_q = 9
        while less(divor, levels[bit_q]):
            bit_q -= 1
        r = simple_minus(divor, levels[bit_q])
        q += str(bit_q)
        i += 1
    length = len(q)
    for i in range(length):
        if q[i] != "0":
            q = q[i:]
            break
        if i == length - 1:
            q = q[-1]
            break
    return (q, r)

class BigInt:
    num = "0"
    def __init__(self, num):
        self.num = num
    def __len__(self):
        return len(self.num)
    def __pos__(self):
        return self
    def __neg__(self):
        return BigInt(negative(self.num))
    def __eq__(self, a):
        return self.num == a.num
    def __ne__(self, a):
        return self.num != a.num
    def __lt__(self, a):
        negS = (self.num[0] == "-")
        negA = (a.num[0] == "-")
        if not negS and not negA:
            return less(self.num, a.num)
        elif negS and not negA:
            return True
        elif not negS and negA:
            return False
        elif negS and negA:
            return (-a) < (-self)
    def __gt__(self, a):
        return a < self
    def __le__(self, a):
        return self < a or self == a
    def __ge__(self, a):
        return self > a or self == a
    def __abs__(self):
        if self >= ZERO:
            return self
        else:
            return -self
    def __add__(self, a):
        if self < ZERO and a < ZERO:
            return -((-self) + (-a))
        elif self < ZERO:
            if abs(self) <= abs(a):
                return BigInt(simple_minus(abs(a).num, abs(self).num))
            else:
                return -BigInt(simple_minus(abs(self).num, abs(a).num))
        elif a < ZERO:
            if abs(self) <= abs(a):
                return -BigInt(simple_minus(abs(a).num, abs(self).num))
            else:
                return BigInt(simple_minus(abs(self).num, abs(a).num))
        else:
            return BigInt(simple_add(self.num, a.num))
    def __sub__(self, a):
        return self + (-a)
    def __mul__(self, a):
        if self == ZERO or a == ZERO:
            return ZERO
        mult = BigInt(simple_times(abs(self).num, abs(a).num))
        if (self > ZERO and a < ZERO) or (self < ZERO and a > ZERO):
            mult = -mult
        return mult
    def __floordiv__(self, a):
        if self < a:
            return ZERO
        if self == a:
            return ONE
        q = BigInt(simple_floordiv(abs(self).num, abs(a).num))
        if (self > ZERO and a < ZERO) or (self < ZERO and a > ZERO):
            q = -q
        return q

ZERO = BigInt("0")
ONE = BigInt("1")
