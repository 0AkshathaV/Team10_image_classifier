img_array = np.expand_dims(img_array, axis=0)
prediction = model.predict(img_array)
