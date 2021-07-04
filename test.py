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
    #european_call = Call(s_0=95, K=100, r=0.10, sigma=0.25, T=1, subscription_ratio=1)
    

    time_steps = np.linspace(1, 100, 100)
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
    df_option_prices.plot(kind='line', logx=True, figsize=(16, 9), title="comparison of CRR, BS and market price",
                          xlabel="periods", ylabel="price")
    plt.show()

    # add. exercise
    print("solutions to additional exercise")
    european_call_add_exercise = Call(s_0=15673.64, K=15600, r=-0.00513, sigma=0.1862, T=0.5, cap=16000, maximum_amount=164, subscription_ratio=0.01, participation_ratio=2)
    print(european_call_add_exercise)
    res = european_call_add_exercise.get_crr(1000,is_capped=True)

    print(res)

if __name__ == "__main__":
    main()
