from pyzbar.pyzbar import decode
import cv2
import numpy as np

image = cv2.imread("image4.jpg")

barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")
   
   
    points = barcode.polygon
    points = [(point.x, point.y) for point in points]
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

    x, y = points[0]  
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green text

cv2.imshow("Barcode with Annotation", image)

key = cv2.waitKey(0)

output_file = "decoded_barcode.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

cv2.destroyAllWindows()