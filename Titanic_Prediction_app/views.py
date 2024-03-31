from django.shortcuts import render
import joblib
from sklearn.preprocessing import LabelEncoder

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def predict_survival(request):
    if request.method == 'POST':
        model = joblib.load("C:\\data science\\CodeAlpha\\Titanic_Predicition_Project\\Titanic_Prediction_app\\models\\model1.pk1")

        Pclass = int(request.POST['Pclass'])
        Sex = int(request.POST['Sex'])
        Age = float(request.POST['Age'])
        SibSp = int(request.POST['SibSp'])
        Parch = int(request.POST['Parch'])
        Fare = float(request.POST['Fare'])
        Embarked =int(request.POST['Embarked'])  # No need to convert to int

        # Load the LabelEncoders for Sex and Embarked
        #sex_encoder = joblib.load("C:\\data science\\CodeAlpha\\Titanic_Predicition_Project\\Titanic_Prediction_app\\models\\sex_encoder.pk1")
        #embarked_encoder = joblib.load("C:\\data science\\CodeAlpha\\Titanic_Predicition_Project\\Titanic_Prediction_app\\models\\embarked_encoder.pk1")

        # Encode Sex and Embarked
        #Sex = sex_encoder.transform([Sex])[0]
        #Embarked = embarked_encoder.transform([Embarked])[0]

        input_data = [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]
        prediction = model.predict(input_data)[0]

        if prediction > 0.5:
            prediction_text = "Yes"
        else:
            prediction_text = "No"
        
        return render(request,'result.html',{'prediction':prediction_text})
    else:
        return render(request,'prediction.html')
