class Call(object):

    def __init__(self, s_0, K, r, sigma, n, T):
        """
        This is the constructor for a European call option.

        :param s_0: current stock price e. g. 15,673.64
        :param K: strike price
        :param r: risk-free interest rate e. g. EURIBOR rate
        :param sigma: volatility
        :param T: time to maturity
        :param n: number of steps
        """

        self._s_0 = s_0
        self._K = K
        self._sigma = sigma
        self._r = r
        self._n = n
        self._T = T
        self._C = 0

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
        return f"Call with s_0:{self._s_0}, K:{self._K}, sigma:{self._sigma}, " \
               f"r:{self._r}, n:{self._n}, T:{self._T} with " \
               f"current price {self._C}."
