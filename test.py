from call import Call


def main():
    """
    Function to test correctness of program
    :return: None
    """
    european_call = Call(s_0=1, K=0.5, r=0.05, sigma=0.5, T=10, n=100)
    print(european_call)


if __name__ == "__main__":
    main()
