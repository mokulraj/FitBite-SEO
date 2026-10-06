from django import forms
from .models import EmailSubscriber, Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["name", "email", "phone", "preferred_meal_type", "city", "consent"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+91 98765 43210"}),
            "preferred_meal_type": forms.Select(attrs={"class": "form-select"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "Madurai"}),
            "consent": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {"consent": "I agree to receive FitBite marketing emails and understand I can unsubscribe."}

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

    def clean_consent(self):
        value = self.cleaned_data["consent"]
        if not value:
            raise forms.ValidationError("Marketing consent is required for this demo signup.")
        return value


class NewsletterForm(forms.ModelForm):
    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

    class Meta:
        model = EmailSubscriber
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
        }
