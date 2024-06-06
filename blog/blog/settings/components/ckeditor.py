CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    "default": {
        # 'skin': 'moono',
        # 'skin': 'office2013',
        "format_tags": "h2;h3;h4;p",
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {"name": "document", "items": ["Source"]},
            {"name": "styles", "items": ["Format"]},
            # {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            # {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #            'HiddenField']},
            # '/',
            {"name": "basicstyles", "items": ["Bold", "Italic", "Underline"]},
            # {'name': 'basicstyles',
            #  'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {
                "name": "paragraph",
                "items": ["NumberedList", "BulletedList", "-", "Blockquote"],
            },
            # {'name': 'paragraph',
            #  'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
            #            'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
            #            'Language']},
            {"name": "links", "items": ["Link", "Unlink"]},
            # {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            # {'name': 'insert',
            #  'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            # '/',
            {"name": "clipboard", "items": ["Undo", "Redo"]},
            # {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            # {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            # {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            # {'name': 'about', 'items': ['About']},
            "/",  # put this to force next toolbar on new line
            # {'name': 'yourcustomtools', 'items': [
            #     # put the name of your editor.ui.addButton here
            #     'Preview',
            #     'Maximize',
            # ]},
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
                "placeholder",
            ]
        ),
        "editorplaceholder": "blabla",
    },
    "cke_post_form_inputs": {
        "format_tags": "h2;h3;h4;p",
        "toolbar_YourCustomToolbarConfig": [
            {"name": "basicstyles", "items": ["Bold"]},
            {
                "name": "paragraph",
                "items": ["NumberedList", "BulletedList", "-", "Blockquote"],
            },
            {"name": "links", "items": ["Unlink"]},
            {"name": "styles", "items": ["Format"]},
            {"name": "clipboard", "items": ["Undo", "Redo"]},
        ],
        "toolbar": "YourCustomToolbarConfig",
        "width": "100%",
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "div",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
                "placeholder",
            ]
        ),
        "editorplaceholder": "",
    },
}
