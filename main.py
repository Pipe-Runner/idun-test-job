from utils.check_gpu import get_training_device


def main():
    device = get_training_device()
    print(device)


if __name__ == '__main__':
    main()
