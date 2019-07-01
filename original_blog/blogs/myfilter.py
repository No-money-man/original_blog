import markdown

md = markdown.Markdown()

@register.filters
@stringfilter
def mark2html(value):
    return md.convert(value)
