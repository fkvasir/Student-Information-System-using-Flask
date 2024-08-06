import cloudinary.uploader

def upload_image(image_stream):
    try:
        result = cloudinary.uploader.upload(image_stream)
        return result['secure_url']
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None
