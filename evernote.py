import cv2, os
import numpy as np

img_path = "Resources/Kakao.jpg"
filename, txt = os.path.splitext(os.path.basename(img_path))
original_img = cv2.imread(img_path)

src = []

#src=input 좌표 dst=output 좌표
def mouse_handler(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONUP:
        img = original_img.copy()

        src.append([x, y])

        for xx, yy in src:
            cv2.circle(img, center=(xx, yy), radius = 5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)

        cv2.imshow("img", img)

        if len(src) == 4:
            src_np = np.array(src, dtype=np.float32)

            width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
            height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

            dst_np = np.array([
                [0, 0],
                [width, 0],
                [0, height],
                [width, height]
            ], dtype=np.float32)

            M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
            result = cv2.warpPerspective(original_img, M=M, dsize=(width,height))

            cv2.imshow('result', result)
            cv2.imwrite("./result/%s_result%s" % (filename, txt), result)


cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_handler)

cv2.imshow("img", original_img)
cv2.waitKey(0)

