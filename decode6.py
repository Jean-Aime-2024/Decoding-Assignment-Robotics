import zxing
import cv2
import numpy as np

reader = zxing.BarCodeReader()

image_path = "image6.png"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image '{image_path}'. Check if the file exists and is readable.")
else:
    decoded = reader.decode(image_path)

    if decoded:
        print(f"Decoded Data: {decoded.parsed}")
        print(f"Barcode Format: {decoded.format}")

        if decoded.points and isinstance(decoded.points, list):
            try:
                points = [(int(p.x), int(p.y)) for p in decoded.points]
                cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

                x, y = points[0]
                cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            except Exception as e:
                print(f"Error processing bounding box points: {e}")

        output_file = "decoded_maxicode.png"
        success = cv2.imwrite(output_file, image)

        if success:
            print(f"Annotated image saved as {output_file}")
        else:
            print("Error: Failed to save the output file.")

        cv2.imshow("MaxiCode with Annotation", image)
        cv2.waitKey(3000)  
        cv2.destroyAllWindows()
    else:
        print("Failed to decode the MaxiCode.")