## ตรวจจับและค้นหาเหรียญจากภาพ วิดีโอ กล้องแบบเรียลไทม์ด้วย Python + OpenCV
![image](https://github.com/kongruksiamza/Coin-Segmentation/blob/be9b2b38ca5707a632e248f7a228ad9fb9985cf8/coin-assets-docs/02.png)
## ไลบราลี่
- opencv-python
- numpy

## หลักการและทฤษฎี
อาศัยหลักการประมวลผลภาพกับรูปร่างและโครงสร้างของภาพโดยนำ **คณิตสัณฐานวิทยา (MM : Mathematical Morphology)** เพื่อประมวลผลภาพตามหลักทฤษฎีแลตติช เป็นเทคนิคสำหรับการวิเคราะห์และประมวลผลโครงสร้างทางเรขาคณิตบนพื้นฐานของทฤษฎีเซต ทฤษฎีตาข่าย โครงสร้างของเครือข่ายและฟังก์ชั่นแบบสุ่ม นิยมนำมาใช้งานกับภาพดิจิตอลเพื่อวิเคราะห์พื้นผิว ขนาด รูปร่าง พื้นที่นูน เป็นต้น

การประมวลผลภาพกับรูปร่างและโครงสร้างภาพ เป็นเทคนิคของการประมวลผลภาพที่ขึ้นอยู่กับรูปร่าง ค่าของ Pixels ในภาพ Output ขึ้นอยู่กับการเปรียบเทียบของ Pixels ที่สอดคล้องกันในภาพ Input กับพื้นที่ใกล้เคียง โดยเลือกขนาดและรูปร่างของพื้นที่ใกล้เคียงมาสร้างการดำเนินการทางรูปร่างและโครงสร้างของภาพต่อไปซึ่งประกอบไปด้วย

### อ่านภาพจากวิดีโอ & กล้อง
![image](https://github.com/kongruksiamza/Coin-Segmentation/blob/be9b2b38ca5707a632e248f7a228ad9fb9985cf8/coin-assets-docs/08.png)
### Gaussian Blur & Threshold
![image](https://github.com/kongruksiamza/Coin-Segmentation/blob/be9b2b38ca5707a632e248f7a228ad9fb9985cf8/coin-assets-docs/10.png)
### Morphological Closing
![image](https://github.com/kongruksiamza/Coin-Segmentation/blob/be9b2b38ca5707a632e248f7a228ad9fb9985cf8/coin-assets-docs/12.png)
### แสดงรูปร่างและกรองพื้นที่เหรียญ
![image](https://github.com/kongruksiamza/Coin-Segmentation/blob/be9b2b38ca5707a632e248f7a228ad9fb9985cf8/coin-assets-docs/13.png)

## 🎓 คอร์สเรียนที่น่าสนใจ [![Udemy](https://img.shields.io/badge/Udemy-A435F0?logo=udemy&logoColor=fff)](https://www.udemy.com/user/kong-ruksiam/)
- [สร้างแอพพลิเคชั่นด้วยภาษา Python (Real-World Projects)](https://www.udemy.com/course/python-real-world-projects/?referralCode=4D6784B6C4CF2CBB1892)
- [สร้าง GUI Application ด้วย Python](https://www.udemy.com/course/python-gui-projects/?referralCode=CFE6A91D21C759EF13E1)
- [พัฒนาเว็บด้วย Django Framework 4.x](https://www.udemy.com/course/django-framework-real-world-projects/?referralCode=63ED08A516BE8C4A93F7)
- [พัฒนาระบบร้านค้าออนไลน์ด้วย Django Framework 4.x](https://www.udemy.com/course/django-framework-e-commerce/?referralCode=AFDB5F462F46815300C1)
- [พัฒนา REST API ด้วย Django REST Framework](https://www.udemy.com/course/rest-api-django-rest-framework/?referralCode=3E81004F9DAE23131BC4)
