class Payoff(object):

    def __init__(self) -> None:
        """
        constructor for pay-off
        """
        self._s_t = 0
        self._val = 0
        self._up = Payoff()
        self._down = Payoff()
        super().__init__()

    def get(self, s_t: float, K: float):
        """
        Get payoff at node for Call
        :param s_t: current stock price at node
        :param K: strike price
        :return: Pay-off at node
        """
        self._s_t = s_t
        self._val = max(0.0, self._s_t - K)
        return self._val
