from sympy import false
from ultralytics import YOLO
from PIL import Image

#Model yükleme
model=YOLO("best.pt")

# modeli kullanarak video görüntüsünden nesne tahmini yapma
sonuc=model.predict(source="car.mp4",show=False,save=True)
