import cv2
import numpy as np

ASCII_SETS = [
    " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
    " .:-=+*#%@",
]


def map_to_ascii(gray_small: np.ndarray, ascii_chars: str, invert: bool = False) -> np.ndarray:
    norm = gray_small.astype(np.float32) / 255.0
    if invert:
        norm = 1.0 - norm
    idx = (norm * (len(ascii_chars) - 1)).astype(np.int32)
    return np.array(list(ascii_chars), dtype="<U1")[idx]


def render_ascii(ascii_img: np.ndarray, color_small: np.ndarray, font_scale: float, thickness: int,
                 colorize: bool, bg_color=(0, 0, 0), fg_color=(255, 255, 255)) -> np.ndarray:
    h, w = ascii_img.shape
    (char_w, char_h), baseline = cv2.getTextSize("M", cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    cell_w, cell_h = char_w, char_h + baseline
    canvas = np.full((h * cell_h, w * cell_w, 3), bg_color, dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            ch = ascii_img[y, x]
            if ch == " ":
                continue
            color = tuple(int(c) for c in color_small[y, x]) if colorize else fg_color
            org = (x * cell_w, (y + 1) * cell_h - baseline)
            cv2.putText(canvas, ch, org, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)
    return canvas


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Не удалось открыть камеру :(")
        return

    ascii_set_id, cols, colorize, invert = 1, 160, False, False
    font_scale, thickness, frame_id = 0.45, 1, 0
    window = "ASCII Cam"
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        h, w = frame.shape[:2]
        rows = max(8, int((h / w) * cols / 2))
        small = cv2.resize(frame, (cols, rows), interpolation=cv2.INTER_AREA)
        small_gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        ascii_img = map_to_ascii(small_gray, ASCII_SETS[ascii_set_id], invert)
        out = render_ascii(ascii_img, small, font_scale, thickness, colorize)

        cv2.imshow(window, out)
        key = cv2.waitKey(1) & 0xFF

        if key in (27, ord("q")):
            break
        if key == ord("s"):
            fname = f"ascii_frame_{frame_id:05d}.png"
            cv2.imwrite(fname, out)
            print(f"Сохранено: {fname}")
        if key == ord("["):
            cols = max(20, cols - 10)
        if key == ord("]"):
            cols = min(400, cols + 10)
        if key == ord("g"):
            colorize = not colorize
        if key == ord("i"):
            invert = not invert
        if key == ord("1"):
            ascii_set_id = 0
        if key == ord("2"):
            ascii_set_id = 1

        frame_id += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
