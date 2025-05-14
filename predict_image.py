def predict_image(img_path):
    model = load_model(MODEL_PATH)
    img = load_img(img_path, target_size,=IMG_SIZE)
    img_array = img_to_array(img)/255.0
