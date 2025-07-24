import uvicorn
from fastapi import FastAPI
from joblib import load
import pandas as pd

app = FastAPI(
    title="Pet Adoption Likelihood Prediction API",
    description="API for predicting pet adoption likelihood based on various factors.",
    version="1.0"
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5016, reload=True)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Pet Adoption Likelihood Prediction API!"}


@app.post('/prediction', tags=["predictions"])
async def get_prediction(PetType:str,Breed:str,AgeMonths: int,Color: str, Size: str, WeightKg: float, Vaccinated: int, HealthCondition: int,
                         TimeInShelterDays: int, AdoptionFee: int, PreviousOwner: int  ):
    try:
        # Load model from best_model.pkl
        model = load('best_model_Rb_nobinned.pkl')
        print("Model loaded successfully")

        # Load columns from models/columns.pkl
        columns = load('columns_Rb_nobinned.pkl')
        print("Columns loaded successfully")

    except Exception as e:
        print(f"Error loading files: {str(e)}")
        return {"error": str(e)}

    try:
        # Create a dictionary with input data
        data = {
            'AgeMonths': [AgeMonths],
            'WeightKg': [WeightKg],
            'Vaccinated': [Vaccinated],
            'HealthCondition': [HealthCondition],
            'TimeInShelterDays': [TimeInShelterDays],
            'AdoptionFee': [AdoptionFee],
            'PreviousOwner': [PreviousOwner],
            'Breed_Golden Retriever': [1 if Breed == 'Golden Retriever' else 0],
            'Breed_Labrador': [1 if Breed == 'Labrador' else 0],
            'Breed_Parakeet': [1 if Breed == 'Parakeet' else 0],
            'Breed_Persian': [1 if Breed == 'Persian' else 0],
            'Breed_Poodle': [1 if Breed == 'Poodle' else 0],
            'Breed_Rabbit': [1 if Breed == 'Rabbit' else 0],
            'Breed_Siamese': [1 if Breed == 'Siamese' else 0],
            'Color_Black': [1 if Color == 'Black' else 0],
            'Color_Brown': [1 if Color == 'Brown' else 0],
            'Color_Gray': [1 if Color == 'Gray' else 0],
            'Color_Orange': [1 if Color == 'Orange' else 0],
            'Color_White': [1 if Color == 'White' else 0],
            'Size': [2 if Size == 'Large' else 1 if Size == 'Medium' else 0],

            'PetType_Bird': [1 if PetType == 'Bird' else 0],
            'PetType_Rabbit': [1 if PetType == 'Rabbit' else 0],
            'PetType_Dog': [1 if PetType == 'Dog' else 0],
            'PetType_Cat': [1 if PetType == 'Cat' else 0],
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(data)
        print("Dataframe created successfully:", input_df)

        # Align the input data with the training columns
        data_aligned = input_df.reindex(columns=columns, fill_value=1)
        print("Data aligned successfully:", data_aligned)

        # Predict the adoption likelihood
        y_pred = model.predict(data_aligned)
        print(f"Prediction: {y_pred}")

        return {"prediction": y_pred.tolist()}

    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return {"error": str(e)}
