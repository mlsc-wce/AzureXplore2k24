import logging
import azure.functions as func
from PIL import Image
import io


def main(myblob: func.InputStream, outputBlob: func.Out[bytes]):
    logging.info(
        f"Processing blob\n Name: {myblob.name}\n Size: {myblob.length} bytes")

    try:

        image = Image.open(myblob)

        resized_image = image.resize((100, 100))
        img_byte_arr = io.BytesIO()
        resized_image.save(img_byte_arr, format=image.format)
        img_byte_arr = img_byte_arr.getvalue()
        outputBlob.set(img_byte_arr)
        logging.info("Image resized successfully.")

    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
