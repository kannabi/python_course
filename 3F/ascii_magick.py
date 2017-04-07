import argparse

pixel_values = tuple("@%#*+=-:. ")


def correct_brightness(correction, pic):

    def shift(y):
        try:
            return pixel_values[pixel_values.index(y) + correction]
        except IndexError:
            if correction < 0:
                return pixel_values[0]
            else:
                return pixel_values[len(pixel_values) - 1]

    if not isinstance(correction, int):
        raise ValueError
    return list(map(lambda x: list(map(lambda y: shift(y), x)), pic))


def crop(pic, l, t, r, b):
    return tuple(map(lambda x: x[l:r], pic[t:b]))


def rotate(pic, corner):
    if corner == 180:
        pic = list(map(lambda x: reversed(x), pic))
        return reversed(pic)
    if corner == 90:
        return [[x[i] for x in pic] for i in range(len(pic[0]) - 1, 0, -1)]
    if corner == 240:
        pic.reverse()
        return [[x[i] for x in pic] for i in range(len(pic[0]) - 1, 0, -1)]
    if corner == 360:
        return pic


def init_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")

    crop_parser = subparsers.add_parser("crop")
    crop_parser.add_argument("-l", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("--left", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("-r", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("--right", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("-t", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("--top", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("-b", action="store", nargs=1, type=str, required=False)
    crop_parser.add_argument("--bottom", action="store", nargs=1, type=str, required=False)

    expose_parser = subparsers.add_parser("expose")
    expose_parser.add_argument("bright", action="store", nargs=1, type=str)

    rotate_parser = subparsers.add_parser("rotate")
    rotate_parser.add_argument("corner", action="store", nargs=1, type=str)

    return parser

with open("input.txt") as fin:
    args = init_parser().parse_args(fin.readline().split())
    picture = list()
    for line in fin:
        picture.append(list(line.strip('\n')))

    if args.subparser_name == 'expose':
        try:
            res = correct_brightness(int(args.bright[0]), picture)
            for item in res:
                print(''.join(item))
        except ValueError:
            print("!!!Parameter of rotate is incorrect")
    if args.subparser_name == 'crop':
        left = int(args.l[0]) if args.l else None
        right = -int(args.r[0]) if args.r else None
        top = int(args.t[0]) if args.t else None
        bottom = -int(args.b[0]) if args.b else None
        res = crop(picture, left, top, right, bottom)
        for item in res:
            print(''.join(item))
    if args.subparser_name == 'rotate':
        res = rotate(picture, int(args.corner[0]))
        for item in res:
            print(''.join(item))
