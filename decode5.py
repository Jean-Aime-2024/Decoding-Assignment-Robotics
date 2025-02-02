import cv2
import numpy as np
import zxing
from pyzbar.pyzbar import decode

reader = zxing.BarCodeReader()
image_path = "image5.jpg"
image = cv2.imread(image_path)

decoded = reader.decode(image_path)

if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")

    if decoded.points and isinstance(decoded.points, list):
        try:
            points = [tuple(map(int, p)) for p in decoded.points]
            cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

            x, y = points[0]  
            cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error processing bounding box points: {e}")


    output_file = "decoded_aztec.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")

    cv2.imshow("Aztec Code with Annotation", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

else:
    print("Failed to decode the Aztec code with ZXing. Trying pyzbar...")

    decoded_objects = decode(image)
    
    if decoded_objects:
        for obj in decoded_objects:
            print(f"Decoded Data: {obj.data.decode('utf-8')}")
            print(f"Barcode Format: {obj.type}")

            points = obj.polygon
            if points:
                points = [(p.x, p.y) for p in points]
                cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

        output_file = "decoded_aztec_code.png"
        cv2.imwrite(output_file, image)
        print(f"Annotated image saved as {output_file}")

        cv2.imshow("Decoded Image", image)
        cv2.waitKey(3000)  
        cv2.destroyAllWindows()
    else:
        print("Failed to decode the Aztec code with pyzbar as well.")