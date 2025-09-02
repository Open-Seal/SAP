import cv2
import numpy as np

ASCII_CHARS = " .:-=+*#%@"


def map_to_ascii(gray_small: np.ndarray, ascii_chars: str) -> np.ndarray:
    norm = gray_small.astype(np.float32) / 255.0
    idx = (norm * (len(ascii_chars) - 1)).astype(np.int32)
    lookup = np.array(list(ascii_chars))
    return lookup[idx]


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Не удалось открыть камеру :(")
        return

    cols = 80

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        h, w = frame.shape[:2]
        rows = max(8, int((h / w) * cols / 2.0))

        small = cv2.resize(frame, (cols, rows), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        ascii_img = map_to_ascii(gray, ASCII_CHARS)
        print("\033c", end="")
        for row in ascii_img:
            print("".join(row))

        key = cv2.waitKey(30) & 0xFF
        if key in (27, ord('q')):
            break

    cap.release()


if __name__ == "__main__":
    main()
