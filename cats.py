import random
import requests
import os
import argparse

parser = argparse.ArgumentParser(description='Print images of the cats ot the folder')
parser.add_argument('amount', type=int, help='Amount of photos')
parser.add_argument('color', type=str, help='For gray photos [gray] / for color [color]')
parser.add_argument('out_dir', type=str, nargs='?', help='Output dir for image')
args = parser.parse_args()


def entry_data():
    amount = args.amount

    urls_color = [
        'http://placekitten.com/'f'{random.randint(720, 5000)}' + '/' + f'{random.randint(720, 5000)}'
    ]

    urls_gray = [
        'http://placekitten.com/g/'f'{random.randint(720, 5000)}' + '/' + f'{random.randint(720, 5000)}'
    ]

    if args.color == 'gray':
        for n in range(amount - 1):
            urls_gray.append('http://placekitten.com/g/'f'{random.randint(720, 5000)}'
                             + '/' + f'{random.randint(720, 5000)}')
            n += 1
        urls_updated = urls_gray
        return urls_updated
    elif args.color == 'color':
        for n in range(amount - 1):
            urls_color.append('http://placekitten.com/'f'{random.randint(720, 5000)}'
                              + '/' + f'{random.randint(720, 5000)}')
            n += 1
        urls_updated = urls_color
        return urls_updated
    else:
        print(TypeError, 'Wrong entry! Choose from "gray" or "color"')
        quit()


def get_name(url):
    name = "cat " + url.split('/')[-2] + '&' + url.split('/')[-1] + '-' + format(random.randint(0, 1000)) + '.jpeg'

    if args.out_dir is None:
        path = os.path.abspath(os.getcwd())
        print('Path:', path)
        return path + '/' + name
    else:
        if not os.path.exists(args.out_dir):
            os.makedirs(args.out_dir)
        path = os.path.abspath(args.out_dir)
        print('Path:', path)

        return path + '/' + name


def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(24576):
            f.write(chunk)


def main(urls_updated):
    for url in urls_updated:
        print('URL:', url)
        save_image(get_name(url), get_file(url))


def get_file(url):
    r = requests.get(url, stream=True)
    return r


if __name__ == '__main__':
    ti = entry_data()
    main(ti)
