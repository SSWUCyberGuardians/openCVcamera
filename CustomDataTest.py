import cv2
import os
from ultralytics.engine.results import Results
from ultralytics import YOLO
import numpy as np

# YOLO 모델 불러오기
model = YOLO('YOLODetect/250epocCustomWeaponYOLOv8Best.pt')

def draw_text_with_opencv(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_thickness = 6
    color = (0, 0, 0)
    bg_color = (255, 255, 255)

    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = 10
    text_y = text_size[1] + 10

    cv2.rectangle(frame, (text_x - 5, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5), bg_color, -1)
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, font_thickness)

    return frame

def draw_boxes(frame, boxes, labels, names):
    for box, label in zip(boxes, labels):
        x1, y1, x2, y2 = map(int, box[:4])
        class_name = names[int(label)]
        color = (0, 255, 0)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        font_scale = 2.0
        frame = cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, 2)
        
    return frame

# 결과를 저장할 디렉토리 생성
results_dir = "results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# 카메라 시작
cap = cv2.VideoCapture(1)

# 창 이름 설정
window_name = "YOLO Detection"

while True:
    ret, frame = cap.read()  # 프레임 캡처
    if not ret:
        break

    results = model(frame)
    first_result = results[0]

    boxes = first_result.boxes.xyxy.cpu().numpy()
    labels = first_result.boxes.cls.cpu().numpy()

    if 0 in labels and 1 in labels and 2 in labels:
        frame = draw_text_with_opencv(frame, "A MASK PERSON with a WEAPON. ")
    elif 1 in labels and 2 in labels:
        frame = draw_text_with_opencv(frame, "A PERSON with a WEAPON. ")

    result_frame = draw_boxes(frame, boxes, labels, first_result.names)

    # 결과 프레임을 results 폴더에 저장
    result_filename = os.path.join(results_dir, "result_{:04d}.png".format(int(cap.get(cv2.CAP_PROP_POS_FRAMES))))
    cv2.imwrite(result_filename, result_frame)

    # 결과 프레임 표시
    cv2.imshow(window_name, result_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
