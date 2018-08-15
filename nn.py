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


    def map(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val)
        return self

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


def sigmoid(y):
    return 1/(1+math.exp(-y))
def dsigmoid(y):
    return y*(1-y)

class fnn:

    def __init__(self, arr, lr):
        # super([object Object], self).__init__()
        self.neurons = []
        self.weights = []
        self.lr = lr or 0.01
        arrlen = len(arr)
        for i in range(arrlen):
            self.neurons.append(arr[i])
        for i in range(arrlen-1):
            weight = matrix(self.neurons[i+1], self.neurons[i])
            self.weights.append(weight)

    def predict(self, input):
        inputs = matrix.fromArray(input)
        outputs = []
        weightlen = len(self.weights)
        for i in range(weightlen):
            inputs = matrix.multiply(self.weights[i], inputs)
            inputs.map(sigmoid)
            outputs.append(inputs)
        return outputs

    def query(self, input):
        n = self.predict(input)
        m = n[len(n)-1]
        k = m.toArray()
        return k

    def learn(self, input, outputarr):
        inputs = matrix.fromArray(input)
        answer = matrix.fromArray(outputarr)
        output = self.query(inputs)
        err = matrix.subtract(answer, output)










nn = fnn([2,3,10,20,50,4,1], 0.01)
nn.learn([1,0], [1])
