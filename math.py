class matrix:
    def __init__(self, a, b):
        # super([object Object], self).__init__()
        self.rows = a
        self.cols = b
        self.data = []
        for i in range(self.rows):
            self.data.append(0)
            self.data[i] = []
            for j in range(self.cols):
                self.data[i].append(0)


    def add(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = self.data[i][j] + n


    def multiply(self, n):
        if(isinstance(n, matrix)):
            if(self.cols != n.rows):
                print("columan of A do not atch with B")
            else:
                result = matrix(self.rows, n.cols)
                for i in range(self.rows):
                    for j in range(n.cols):
                        sum = 0
                        for k in range(self.cols):
                            sum = sum+self.data[i][j]*n.data[k][j]
                        result.data[i][j] = sum
                return result
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] = self.data[i][j] * n


    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr

    @classmethod
    def dot(self, a, b):
        if(a.cols != b.rows):
            print("columan of A do not atch with B")

        result = matrix(a.rows, b.cols)
        for i in range(a.rows):
            for j in range(b.cols):
                sum = 0
                for k in range(a.cols):
                    sum = sum+a.data[i][j]*b.data[k][j]
                result.data[i][j] = sum
        return result

    @classmethod
    def fromArray(self, a):
        m = matrix(len(a), 1)
        for i in range(len(a)):
            m.data[i][0] = a[i]
        return m

    @classmethod
    def transpose(self, a):
        m = matrix(a.cols, a.rows)
        for i in range(a.rows):
            for j in range(a.cols):
                m.data[j][i] = a.data[i][j]
        return m

    @classmethod
    def subtract(self, a, b):
        if(a.rows == b.rows & a.cols == b.cols):
            m = matrix(a.rows, a.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    m.data[i][j] = a.data[i][j] - b.data[i][j]
            return m
        else:
            print("cant subtract these matrix")

    @classmethod
    def sum(self, a, b):
        if(a.rows == b.rows & a.cols == b.cols):
            m = matrix(a.rows, a.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    m.data[i][j] = a.data[i][j] + b.data[i][j]
            return m
        else:
            print("cant sum both of these matrix")


    @classmethod
    def map(self, y, func):
        m = matrix(y.rows, y.cols)
        for i in range(y.rows):
            for j in range(y.cols):
                val = y.data[i][j]
                m.data[i][j] = func(val)
        return m

class math:
    @classmethod
    def exp(self, x):
        return 2.71828182845904523536028747135266249775724709369995**x


# def mac(y):
#     return y*2
#
#
#
#
# m = matrix(2, 3)
# m.add(2)
# # m.multiply(2)
# n = matrix(3, 2)
# n.add(5)
# p = matrix.map(n, mac)
# print(p.data)
