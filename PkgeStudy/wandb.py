import wandb
import random
import argparse


def main():
    for i in range(100):
        wandb.log({'key': float(i)})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--batch-size', type=int, default=8, metavar='N',
                        help='input batch size for training (default: 8)')
    args = parser.parse_args()
    wandb.init(project="my-awesome-project", name="test")
    wandb.config.update(args)
    main()
    wandb.finish()
