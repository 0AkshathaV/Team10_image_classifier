img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array)

predicted_class = np.argmax(prediction)
print(f"Predicted class index: {predicted_class}")
return predicted_class
