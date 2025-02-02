from pyzbar.pyzbar import decode
import cv2
import numpy as np

image_path = "image3.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image '{image_path}'. Check if the file exists.")
else:
    barcodes = decode(image)
    

    if not barcodes:
        print("No barcode found in the image.")
    else:
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            print(f"Barcode Data: {data}")

            points = barcode.polygon
            points = [(point.x, point.y) for point in points]
            cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

            x, y = points[0]
            cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        output_file = "decoded_barcode_code.png"
        success = cv2.imwrite(output_file, image)

        if success:
            print(f"Annotated image saved as {output_file}")
        else:
            print("Error: Could not save the annotated image.")

        cv2.imshow("Barcode with Annotation", image)
        cv2.waitKey(3000)  
        cv2.destroyAllWindows()