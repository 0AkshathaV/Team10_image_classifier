def predict_image(img_path):
    model = load_model(MODEL_PATH)
    img = load_img(img_path, target_size,=IMG_SIZE)
    img_array = img_to_array(img)/255.0

img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array)

predicted_class = np.argmax(prediction)
print(f"Predicted class index: {predicted_class}")
return predicted_class

