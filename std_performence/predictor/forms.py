from django import forms

class StudentPerformanceForm(forms.Form):
    hours_studied = forms.FloatField(
        label="Hours Studied",
        min_value=0,
        max_value=24,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Hours per day", "step": "0.5"})
    )
    previous_scores = forms.FloatField(
        label="Previous Scores",
        min_value=0,
        max_value=200,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Average score"})
    )
    extracurricular = forms.ChoiceField(
        label="Extracurricular Activities",
        choices=[("0", "No"), ("1", "Yes")],
        widget=forms.RadioSelect
    )
    sleep_hours = forms.FloatField(
        label="Sleep Hours",
        min_value=0,
        max_value=12,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Hours per night", "step": "0.5"})
    )
    sample_papers = forms.IntegerField(
        label="Sample Question Papers Practiced",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of papers"})
    )
