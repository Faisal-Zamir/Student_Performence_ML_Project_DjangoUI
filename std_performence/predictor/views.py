from django.http import JsonResponse
from django.shortcuts import render
from predictor.ML_Files.std_performence_predict import predict_std_performence, get_model_performance
from .forms import StudentPerformanceForm
# New data
new_data = {
    "Hours Studied": 8,
    "Previous Scores": 170,
    "Extracurricular Activities Mapped": 1,
    "Sleep Hours": 6,
    "Sample Question Papers Practiced": 15
}


def homepage(request):
    prediction = None
    new_data = {}

    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        form = StudentPerformanceForm(request.POST)

        if form.is_valid():
            new_data = {
                "Hours Studied": float(request.POST.get("hours_studied")),
                "Previous Scores": float(request.POST.get("previous_scores")),
                "Extracurricular Activities Mapped": int(request.POST.get("extracurricular")),
                "Sleep Hours": float(request.POST.get("sleep_hours")),
                "Sample Question Papers Practiced": int(request.POST.get("sample_papers")),
            }
            # print("New data received from form:")
            # print(new_data)
            prediction = round(predict_std_performence(new_data), 2)
            return JsonResponse({"prediction": float(prediction)})

        else:
            print("Form is not valid")
    else:
        form = StudentPerformanceForm()

    if new_data:
        prediction = predict_std_performence(new_data)
    else:
        prediction = None

    various_metrics = get_model_performance()
    # Convert to percentage + round
    formatted_metrics = {
        key: f"{round(value * 100, 2)}" for key, value in various_metrics.items()
    }


    context = {
        "metrics": formatted_metrics,
        "form": form,
        "prediction": prediction,
               }
    return render(request, "predictor/index.html", context)