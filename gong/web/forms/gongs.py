BaseGongForm = model_form(
    models.Gong,
    FlaskForm,
    exclude=[
        "created_date",
        "updated_date",
    ],
    field_args={
        "title": {"label": "Title"},
        "first_name": {"label": "First Name"},
        "last_name": {"label": "Last Name"},
        "title_th": {"label": "Thai Title"},
        "first_name_th": {"label": "Thai First Name"},
        "last_name_th": {"label": "Thai Last Name"},
        "biography": {"label": "Biography"},
        "email": {"label": "Email"},
    },
)


class GongForm(BaseGongForm):
    pic = fields.FileField(
        "Picture", validators=[FileAllowed(["png", "jpg"], "allow png and jpg")]
    )
