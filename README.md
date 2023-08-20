## 3.4 OCR 기능 활용 다중 경고 등급 시스템 인터페이스 구현

### 3.4.1 OCR을 활용한 실시간 키워드 인식 시스템

OCR(광학 문자 인식)은 디지털 이미지나 스캔된 문서 내의 문자를 자동으로 인식하여 기계가 읽을 수 있는 텍스트 데이터로 변환하는 기술입니다. 웹캠에서 실시간으로 스트리밍되는 영상 내에서 특정 키워드를 인식하는 시스템을 개발하였습니다. 이 시스템은 영상에서 감지된 키워드에 관련된 정보나 경고를 사용자에게 즉시 제공합니다.

### 3.4.2 경고 메시지 체계 - 다중 경고 등급 분류

다양한 위험 상황에 따라 사용자에게 경고 메시지를 다르게 전달합니다.

- **주의 단계**:  
  **구성요소**: 무기 소지 + 무표정 + 사람  
  무기와 유사한 물체 감지, 하지만 주변 인원은 평온합니다.

- **경고 단계**:  
  **구성요소**: 무기 소지 + 화난 표정 + 사람  
  무기를 든 사람이 화가 난 표정입니다.

- **경계 단계**:  
  **구성요소**: 무기 소지 + 행복한 표정 + 사람  
  무기를 든 사람이 행복한 표정입니다.

- **재난 단계**:  
  **구성요소**: 무기 소지 + 마스크 착용 + 사람  
  마스크를 착용하고 무기를 든 사람입니다.

### 3.4.3 시스템 최적화 및 효율성

- **Frame Skipping**: 5 프레임마다 OCR을 수행하여 처리 시간 단축.
- **이미지 리사이징**: 이미지 크기를 조절하여 처리 시간을 줄임.
- **Tesseract Configuration**: Tesseract OCR 최적화 설정 적용.
- **키워드 매칭 로직**: 추출된 텍스트에서 키워드를 식별하고 사용자에게 메시지 출력.

https://www.youtube.com/watch?v=fDAlVDkUd5I&list=PLDlvsX6-adcuqU35leuLXI-I_b-neJ_ww&index=1
https://www.youtube.com/watch?v=ND_lsFbqjes&list=PLDlvsX6-adcuqU35leuLXI-I_b-neJ_ww&index=2
