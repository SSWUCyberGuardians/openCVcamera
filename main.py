import cv2
import pytesseract
from webcam import init_webcam, release_webcam, read_from_webcam
from messagebox_util import show_messagebox

keywords = {
    1: {'weapon', 'neutral', 'person'},
    2: {'angry', 'weapon', 'person'},
    3: {'happy', 'weapon', 'person'},
    4: {'mask', 'weapon', 'person'}
}

cap = init_webcam()

frame_count = 0
resize_scale = 0.5
while True:
    try:
        ret, frame = read_from_webcam(cap)
        if not ret:
            break

        if frame_count % 5 == 0:
            frame_resized = cv2.resize(frame, (int(frame.shape[1]*resize_scale), int(frame.shape[0]*resize_scale)))
            text = pytesseract.image_to_string(frame_resized, config='--psm 6')
            for level, key_set in keywords.items():
                found_keywords = {keyword for keyword in key_set if keyword in text.lower()}
                if found_keywords == key_set:
                    if level == 1:
                        show_messagebox("Notice", "주의! 무기와 무표정의 사람 감지됨!", "info")
                    elif level == 2:
                        show_messagebox("Warning", "경고! 화난 표정의 사람이 무기를 소지하고 있습니다!", "warning")
                    elif level == 3:
                        show_messagebox("Danger!", "위험! 행복한 표정의 사람이 무기를 소지하고 있습니다!", "error")
                    elif level == 4:
                        show_messagebox("Catastrophe", "재난! 마스크 착용자와 무기, 사람 동시에 감지됨!", "error")
                    break

        frame_count += 1
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Error during video processing: {e}")
        break

release_webcam(cap)
