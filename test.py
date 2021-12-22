def __init__(self, c, a, b):
        self.c = c.astype(np.float64)
        self.a = a.astype(np.float64)
        self.b = b.astype(np.float64)
        self.num_x = self.a.shape[1]