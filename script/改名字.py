# @Author: eveleaf
# @Date: 2024-11-02 10:23
# @LastEditTime: 2024-11-02 10:29
# @Description:

from pathlib import Path
from natsort import natsorted
import argparse


print("更改完成")


if __name__ == "__main__":
    # 获取命令行参数
    # 需要用到的参数：文件夹地址，是否需要转平台wsl需要，其他不需要，重命名模式
    parse = argparse.ArgumentParser()
    parse.add_argument("--video_dir", default=r"D:\Videos\精灵宝可梦\test", help="视频文件夹地址")
    parse.add_argument(
        "--platform",
        default="wsl",
        choices=["windows", "wsl", "linux"],
        help="如果是windows或者wsl，需要进行路径转化",
    )
    # 模式：
    # 1. 字幕文件模式：按照字幕文件进行改名字
    # 2. 自定义文件名格式：比如文件名 + 数字 + .mp4后缀等
    parse.add_argument(
        "--mode",
        default="2",
        choices=["1", "2"],
        help="重命名模式",
    )
    parse.add_argument(
        "--pattern",
        type=str,
        default="[c2club][精灵宝可梦超世代][Advanced Generation][{{number:>0{}d}}]",
        help="自定义文件名模式，其中number指序号",
    )
    parse.add_argument("--width", type=int, default=3, help="序号宽度")
    parse.add_argument("--start", type=int, default=100, help="序号起始号")
    args = parse.parse_args()

    # 根据平台，转化文件夹路径
    if args.platform == "windows":
        video_dir = Path(args.video_dir.replace("\\", "/"))
    elif args.platform == "wsl":
        temp = ["/mnt"] + args.video_dir.split("\\")
        # 转化盘符：将':'去掉，大写盘符改小写
        temp[1] = temp[1].replace(":", "").lower()
        video_dir = Path("/".join(temp))
    else:
        video_dir = Path(args.video_dir)

    # 根据不同模式转化文件名
    if args.mode == "1":
        # 支持多种视频格式，如mp4，mkv；支持多种字幕文件格式，如srt，ass
        video_list = list(video_dir.glob("*.mkv")) + list(video_dir.glob("*.mp4"))
        subtitle_list = list(video_dir.glob("*.srt")) + list(video_dir.glob("*.ass"))
        # print(video_list)
        # print(subtitle_list)

        # 视频和字幕数量一致
        assert len(video_list) == len(subtitle_list)

        # 对视频列表和字幕列表进行自然排序
        video_list = natsorted(video_list)
        subtitle_list = natsorted(subtitle_list)
        # 将字幕的名字改为视频的名字
        for i in range(len(subtitle_list)):
            subtitle_list[i].replace(subtitle_list[i].with_stem(video_list[i].stem))
    elif args.mode == "2":
        # 获取文件列表，并自然排序
        video_list = (
            list(video_dir.glob("*.mkv")) + list(video_dir.glob("*.mp4")) + list(video_dir.glob("*.rmvb"))
        )
        video_list = natsorted(video_list)
        # print(video_list)
        for i in range(len(video_list)):
            video_list[i].replace(
                video_list[i].with_stem(args.pattern.format(args.width).format(number=args.start + i))
            )
