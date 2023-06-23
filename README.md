# AI-project
-- 4학년 1학기 <인공지능> 수업에서 진행한 Team Project --
## Topic
Demo of Blind Data App Using Facial Detection & Image Captioning Models
## Outline
개인 정보가 중요해지고, 불특정 다수에게 자신의 얼굴을 공개하는 것이 꺼려지는 요즘 사회에서, 많은 소개팅 앱에서는 상대방과 매칭되기 위해 자신의 얼굴을 공개하고 평가를 받아야 한다. 이러한 문제 의식을 가지고 수업 시간에 배운 컴퓨터비전 분야의 모델들을 활용해 보기 위해 위와 같은 프로젝트 주제를 선택하게 되었다.
## Algorithm
1. 데이팅 앱의 사용자가 원하는 이상형의 피부색, 코 길이의 비율, 입술 길이의 비율을 입력한다.
2. Facial Detection Model을 통해 조건에 맞는 얼굴 이미지를 랜덤으로 추출한다. 이때, 사용자는 추출된 이미지를 볼 수 없다.
3. 추출된 이미지에 대하여 Image Captioning Model을 통해 이미지의 특징(옷, 수염 등)을 캡션으로 생성한다.
4. 사용자는 서로의 사진을 보지 않고 소개팅 매칭이 된다.
## Models
### Facial Detection Model Implementation
[예은] Faster R-CNN

[윤선] MTCNN
### Image Captioning Model Implementation
[예은] Transformer-based

[윤선] ResNet152-LSTM
## Reference
[1] A Method of Eye and Lip Region Detection using Faster R-CNN Face Image

https://koreascience.kr/article/JAKO201827041051649.pdf

[2] Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks

https://arxiv.org/ftp/arxiv/papers/1604/1604.02878.pdf

[3] Image Caption Generator Using RESNET-LSTM

https://www.ijres.org/papers/Volume-9/Issue-8/Series-1/L09086471.pdf

[4] End-to-End Transformer Based Model for Image Captioning (Yiyu Wang)

https://arxiv.org/pdf/2203.15350.pdf
