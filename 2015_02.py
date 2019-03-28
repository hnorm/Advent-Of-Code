boxes = [line.strip().split('x') for line in open("2015_02_dimensions.txt", "r")]

def part_one(boxes):

    def paper_needed(h, l, w):
        slack = min(w*l, w*h, h*l)
        return 2*w*l + 2*w*h + 2*h*l + slack

    area = 0
    for box in boxes:
        area += paper_needed(int(box[0]), int(box[1]), int(box[2]))
    return area

def part_two(boxes):

    def ribbon_needed(h, l, w):
        wrap_length = min(2*h+2*l, 2*h+2*w, 2*l+2*w)
        bow_length = h*l*w
        return wrap_length + bow_length

    length = 0
    for box in boxes:
        length += ribbon_needed(int(box[0]), int(box[1]), int(box[2]))
    return length

print(part_two(boxes))