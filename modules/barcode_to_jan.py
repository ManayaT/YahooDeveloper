import cv2

def get_janCode(target_path):
    try:
        img = cv2.imread(target_path)
        bd = cv2.barcode.BarcodeDetector()

        retval, decoded_info, decoded_type, points = bd.detectAndDecodeMulti(img)
        if retval:
            return decoded_info[0]
        else:
            return None
        
    except Exception as e:
        return None
