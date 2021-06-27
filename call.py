class Call(object):

    def __init__(self, s_0, K, r, sigma, n, T) -> object:
        """
        This is the constructor for a European call option.

        :param s_0: current stock price e. g. 15,673.64
        :param K: strike price
        :param r: risk-free interest rate e. g. Euribor rate
        :param sigma: volatility
        :param T: time to maturity
        :param n: number of steps
        """

        self.s_0 = s_0
        self.K = K
        self.sigma = sigma
        self.r = r
        self.n = n
        self.T = T
        self.C = 0

    def get_price(self) -> float:
        """
        Function to calculate the price of a European option as described in:
        @article{
        title = {{OPTION} {PRICING}: {A} {SIMPLIFIED} {APPROACH}},
        author = {Cox, John C and Ross, A},
        pages = {35},
        }

        :return: price_estimate
        """
        pass

    def __str__(self) -> str:
        return f"Call with s_0:{self.s_0}, K:{self.K}, sigma:{self.sigma}, r:{self.r}, n:{self.n}, T:{self.T} with " \
               f"current price {self.C}."
