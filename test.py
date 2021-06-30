import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from call import Call


def main():
    """
    Function to test correctness of program and create required plots
    :return: None
    """
    european_call = Call(s_0=15673.64, K=15100, r=-0.00513, sigma=0.1862, T=0.5, subscription_ratio=0.01)
    print(european_call)

    time_steps = np.linspace(1, 1000, 1000)
    df_option_prices = pd.DataFrame(index=time_steps)

    # given in bonus exercise
    df_option_prices['market_price'] = 11.29
    df_option_prices['bs'] = european_call.get_bs()
    df_option_prices['crr'] = df_option_prices.apply(lambda x: european_call.get_crr(x.name), axis=1)

    # c) part
    print("solutions to c):")
    print(f"BS: {european_call.get_bs()}")
    print(f"CRR: {european_call.get_crr(100)}")

    # d) part
    df_option_prices.plot(kind='line', logx=True, figsize=(16, 9), title="comparison CRR, BS and Market Price",
                          xlabel="periods", ylabel="price")
    plt.show()



if __name__ == "__main__":
    main()
