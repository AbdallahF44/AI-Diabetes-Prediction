import pickle


def loadModel(fileName):
    try:
        with open(fileName, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print("Model file not found.")
    except Exception as e:
        print("Error while loading the model.", str(e))
        return None  # Return None if loading fails


# model = loadModel(r"/model/model.pkl")
model = loadModel("model/model.pkl")

# input_data = [[6, 147, 72, 35, 0, 33.6, 0.627, 50]]  # Example input data
# predictions = model.predict(input_data)
# print(predictions)
# Check if model is loaded successfully before using it
if model is not None:
    input_data = [[6, 147, 72, 35, 0, 33.6, 0.627, 50]]  # Example input data
    predictions = model.predict(input_data)
    print(predictions)
else:
    print("Failed to load model. Predictions cannot be made.")
