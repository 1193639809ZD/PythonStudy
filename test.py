from torch import nn


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
        self.conv2 = nn.Conv2d(64, 64, 3)
        self.maxpool1 = nn.MaxPool2d(2, 2)

        self.features = nn.Sequential(
            nn.Conv2d(64, 128, 3),
            nn.Conv2d(128, 128, 3),
            nn.ReLU()
        )

        self.features_list = nn.ModuleList([nn.Linear(128, 256), nn.ReLU()])

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.maxpool1(x)
        x = self.features(x)

        return x


net = MyNet()
print(net)
# optimizer = optim.SGD()
