# https://github.com/matthiask/html-sanitizer/tree/main
HTML_SANITIZERS = {
    "post_form_inputs": {
        "tags": (
            "h2",
            "h3",
            "strong",
            "p",
            "ul",
            "ol",
            "li",
            "br",
            "blockquote",
        ),
        "empty": {"br"},
        "separate": {"p", "li"},
        "attributes": {},
    },
}
