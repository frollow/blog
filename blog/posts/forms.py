from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Clean label='' for all fields
        for field_name, field in self.fields.items():
            if field_name != "published":
                field.label = ""

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["author", "feature", "pub_date", "paid"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "100",
                    "placeholder": "Title",
                    "label": "",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "50",
                    "placeholder": "Slug",
                }
            ),
            "short_text": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "250",
                    "placeholder": "Short description",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "input w-input",
                    "maxlength": "4000",
                    "placeholder": "Body",
                }
            ),
            "group": forms.Select(
                attrs={
                    "class": "w-commerce-commercecheckoutshippingcountryselector input medium last",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Comment title"}
        help_text = {"text": "Comment"}

        # widgets = {
        #     "name": forms.TextInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "maxlength": "200",
        #             "placeholder": "Жесткий свет",
        #             "data-count": "100",
        #         }
        #     ),
        #     "slug": forms.TextInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "maxlength": "50",
        #             "placeholder": "zhestkij-svet",
        #         }
        #     ),
        #     "description": CourseFormCKEditorWidget(
        #         config_name="cke_front_course_form_inputs",
        #         attrs={
        #             "class": "form_textarea w-input",
        #         },
        #     ),
        #     "image": forms.ClearableFileInput(
        #         attrs={
        #             "class": "custom-image-upload-class",
        #             "accept": "image/*",
        #         }
        #     ),
        #     "link": forms.TextInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "maxlength": "256",
        #             "placeholder": "https://vebinaroom.ru/",
        #         }
        #     ),
        #     "start_date": forms.TextInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "placeholder": "Дата начала обучения",
        #             "id": "datepicker",
        #         }
        #     ),
        #     "classes_count": forms.NumberInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "max": "999999999",
        #         }
        #     ),
        #     "length": forms.NumberInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "max": "999999999",
        #         }
        #     ),
        #     "length_metric": forms.Select(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "certificate": forms.CheckboxInput(
        #         attrs={
        #             "data-name": "certificate",
        #             "style": "opacity:0;position:absolute;z-index:-1",
        #         }
        #     ),
        #     "free": forms.CheckboxInput(
        #         attrs={
        #             "data-name": "free",
        #             "style": "opacity:0;position:absolute;z-index:-1",
        #         }
        #     ),
        #     "request_price": forms.CheckboxInput(
        #         attrs={
        #             "data-name": "request_price",
        #             "style": "opacity:0;position:absolute;z-index:-1",
        #         }
        #     ),
        #     "price": forms.NumberInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "max": "999999999",
        #         }
        #     ),
        #     "price_per_month": forms.NumberInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "max": "999999999",
        #         }
        #     ),
        #     "price_new": forms.NumberInput(
        #         attrs={
        #             "class": "form_input w-input",
        #             "max": "999999999",
        #         }
        #     ),
        #     "group": forms.Select(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "topic": forms.SelectMultiple(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "language": forms.SelectMultiple(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "level": forms.Select(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "school": forms.Select(
        #         attrs={
        #             "class": "form_selector w-select",
        #         }
        #     ),
        #     "tag_group_author": forms.CheckboxInput(
        #         attrs={
        #             "data-name": "visible",
        #             "style": "opacity:0;position:absolute;z-index:-1",
        #         }
        #     ),
        #     "visible": forms.CheckboxInput(
        #         attrs={
        #             "data-name": "visible",
        #             "style": "opacity:0;position:absolute;z-index:-1",
        #         }
        #     ),
        # }
