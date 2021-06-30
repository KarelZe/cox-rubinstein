import numpy as np
from scipy.stats import norm


class Call(object):

    def __init__(self, s_0, K, r, sigma, T, subscription_ratio):
        """
        This is the constructor for a European call option.

        Object can be used to calculate prices using Black Scholes and Cox Ross Rubinstein

        :param s_0: current stock price e. g. 15,673.64
        :param K: strike price e. g. 15,100
        :param r: risk-free interest rate e. g. EURIBOR rate e. g. -0.00513
        :param sigma: volatility e. g. 0.1862
        :param T: time to maturity e. g. 0.05
        :param subscription_ratio: subscription ratio e. g. 0.01
        """

        self._s_0 = s_0
        self._K = K
        self._sigma = sigma
        self._r = r
        self._T = T
        self._C = 0
        self._u = 0
        self._d = 0
        self._p = 0
        self._n = 0
        self._subscription_ratio = subscription_ratio

    def get_bs(self, t=0) -> float:
        """
        Function to calculate the price of a European option as described in:
        @article{black_pricing_1973,
            title = {The {Pricing} of {Options} and {Corporate} {Liabilities}},
            volume = {81},
            number = {3},
            journal = {The Journal of Political Economy},
            author = {Black, Fischer and Scholes, Myron},
            year = {1973},
            pages = {637--654},
	    }

        :rtype: float
        :param t: starting point in time, default is 0
        :return: call_price
        """

        # See p. 640 following
        delta_t = self._T - t
        sigma_sqrt_t = self._sigma * np.sqrt(delta_t)

        d_1 = (np.log(self._s_0 / self._K) + (self._r + 0.5 * self._sigma ** 2) * delta_t) / (sigma_sqrt_t)
        d_2 = d_1 - sigma_sqrt_t

        call = (self._s_0 * norm.cdf(d_1, 0.0, 1.0) - self._K * np.exp(-self._r * delta_t) * norm.cdf(d_2, 0.0, 1.0))

        return call * self._subscription_ratio

    def get_crr(self, n: int) -> float:
        """
        Function calculate the option price of a call option using a binomial tree as described in:

        and
        @article{
            title = {{OPTION} {PRICING}: {A} {SIMPLIFIED} {APPROACH}},
            author = {Cox, John C and Ross, A},
            pages = {35},
        }

        Idea for matrix-based implementation is inspired from:

        @article{gilli_implementing_2009,
            title = {Implementing {Binomial} {Trees}},
            issn = {1556-5068},
            doi = {10.2139/ssrn.1341181},
            journal = {SSRN Electronic Journal},
            author = {Gilli, Manfred and Schumann, Enrico},
            year = {2009},
        }


        :param n: number of time steps
        :return: call_price
        """

        self._n = int(n)

        # see p. 232 following
        delta_t = self._T / self._n
        sigma_sqrt_t = self._sigma * np.sqrt(delta_t)

        self._u = np.exp(sigma_sqrt_t)
        self._d = 1.0 / self._u
        self._p = (np.exp(self._r * delta_t) - self._d) / (self._u - self._d)

        # build rectangular matrix for asset prices. Use NaNs as default values for better visualization.
        stock_matrix = np.zeros(shape=(self._n + 1, self._n + 1))
        stock_matrix.fill(np.nan)

        # create second matrix for option prices
        option_matrix = stock_matrix.copy()

        # build asset tree, populate only upper triangle matrix
        for i in range(self._n + 1):
            for j in range(i + 1):
                stock_matrix[j, i] = self._s_0 * (self._u ** (i - j)) * (self._d ** j)

        # calculate pay-off for entire, very last column of matrix
        option_matrix[:, self._n] = np.maximum(np.zeros(self._n + 1), (stock_matrix[:, self._n] - self._K))

        # calculate prices in matrix recursively. Start at very end and iterate to the very left.
        for i in range(self._n - 1, -1, -1):
            for j in range(i + 1):
                # see p. 234
                option_matrix[j, i] = (self._p * option_matrix[j, i + 1] + (1 - self._p) * option_matrix[
                    j + 1, i + 1]) * np.exp(
                    -self._r * (self._T / self._n))

        # return very first price as current option value
        call = option_matrix[0, 0]

        # print("Asset Tree")
        # print(stock_matrix)

        # print("Option Tree")
        # print(option_matrix)

        print(n)

        return call * self._subscription_ratio

    def __str__(self) -> str:
        """
        Function to return string representation of object.
        :return: string with object info
        """
        return f"Call with s_0:{self._s_0}, K:{self._K}, sigma:{self._sigma}, " \
               f"r:{self._r}, n:{self._n}, T:{self._T} and " \
               f"subscription ratio:{self._subscription_ratio}."
