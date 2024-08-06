from app import create_app
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv('.env')

app = create_app()
config = cloudinary.config(secure=True)


if __name__ == '__main__':
   app.run(debug=True)

