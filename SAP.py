import cv2
import numpy as np

ASCII_SETS = [
    " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
    " .:-=+*#%@",
]


def map_to_ascii(gray: np.ndarray, chars: str, invert: bool) -> np.ndarray:
    norm = gray.astype(np.float32) / 255.0
    if invert:
        norm = 1.0 - norm
    idx = (norm * (len(chars) - 1)).astype(np.int32)
    return np.array(list(chars), dtype="<U1")[idx]


def render_ascii(ascii_img: np.ndarray, color_small: np.ndarray,
                 font_scale: float, thickness: int, colorize: bool,
                 bg_color=(0, 0, 0), fg_color=(255, 255, 255)) -> np.ndarray:
    h, w = ascii_img.shape
    (cw, ch), base = cv2.getTextSize("M", cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    cell_w, cell_h = cw, ch + base
    canvas = np.full((h * cell_h, w * cell_w, 3), bg_color, dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            ch = ascii_img[y, x]
            if ch == " ":
                continue
            color = tuple(map(int, color_small[y, x])) if colorize else fg_color
            org = (x * cell_w, (y + 1) * cell_h - base)
            cv2.putText(canvas, ch, org, cv2.FONT_HERSHEY_SIMPLEX,
                        font_scale, color, thickness, cv2.LINE_AA)
    return canvas


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Не удалось открыть камеру")
        return

    ascii_set_id, cols = 1, 160
    colorize, invert = False, False
    font_scale, thickness = 0.45, 1
    frame_id = 0
    window = "ASCII Cam"
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        h, w = frame.shape[:2]
        rows = max(8, int((h / w) * cols / 2))
        small = cv2.resize(frame, (cols, rows), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        ascii_img = map_to_ascii(gray, ASCII_SETS[ascii_set_id], invert)
        out = render_ascii(ascii_img, small, font_scale, thickness, colorize)

        cv2.imshow(window, out)
        key = cv2.waitKey(1) & 0xFF

        if key in (27, ord("q")):
            break
        if key == ord("s"):
            name = f"ascii_frame_{frame_id:05d}.png"
            cv2.imwrite(name, out)
            print("Сохранено:", name)
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
        if key == ord("="):
            font_scale = min(2.0, font_scale + 0.05)
        if key == ord("-"):
            font_scale = max(0.2, font_scale - 0.05)
        if key == ord("t"):
            thickness = 1 if thickness > 2 else thickness + 1

        frame_id += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
