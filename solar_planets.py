import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,0,0)
)

cv2.putText(img,
    "Mercury",
    (200,400),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Venus",
    (350,500),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Earth",
    (500,500),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Mars",
    (650,500),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Jupiter",
    (800,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Saturn",
    (950,320),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Uranus",
    (1100,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)
cv2.putText(img,
    "Neptune",
    (1250,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.2,
    (255,255,255)
)

cv2.imshow("output", img)
cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.waitkey(0)