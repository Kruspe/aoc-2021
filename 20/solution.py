import numpy as np


def solve(times):
    # brightness determines if the infinite image is bright or dark (the sample is always dark 🤘🏿)
    def get_binary(x, y, from_image, brightness):
        if brightness:
            pixels = np.ones((3, 3), dtype=int)
        else:
            pixels = np.zeros((3, 3), dtype=int)

        for a in range(-1, 2):
            for b in range(-1, 2):
                try:
                    if x + a >= 0 and y + b >= 0:
                        if brightness:
                            if from_image[(x + a, y + b)] == '.':
                                pixels[a + 1, b + 1] = 0
                        else:
                            if from_image[(x + a, y + b)] == '#':
                                pixels[a + 1, b + 1] = 1
                except IndexError:
                    pass
        return pixels

    def enhance(image_to_enhance, time):
        image_rows, image_cols = image_to_enhance.shape
        enhanced_image = np.zeros((image_rows + 2, image_cols + 2), dtype=str)

        for i in range(-1, image_rows + 1):
            for f in range(-1, image_cols + 1):
                enhanced_image[i + 1, f + 1] = algorythm[
                    int(''.join(map(lambda x: str(x), np.concatenate(get_binary(i, f, image_to_enhance, time % 2)))), 2)]
        return enhanced_image

    enhance_image = image.copy()
    for update_time in range(times):
        enhance_image = enhance(enhance_image, update_time)

    return len(np.where(enhance_image == '#')[0])


def parse(data):
    rows = []
    for line in data[2:]:
        rows.append(list(line))

    return data[0], np.array(rows)


if __name__ == '__main__':
    algorythm, image = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve(2))
    print('Part 2', solve(50))
