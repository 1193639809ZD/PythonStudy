from tqdm import tqdm


def test():
    loader = tqdm(range(10000), leave=False, desc='loop 2st:')
    for idx, data in enumerate(loader):
        pass


if __name__ == "__main__":
    step = 0
    loader = tqdm(range(10000), leave=True, desc='loop 1st:')
    for idx, data in enumerate(loader):
        step += 1
        if step % 100 == 0:
            test()
