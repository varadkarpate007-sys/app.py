# Decorator
def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "**" + result + "**"
    return wrapper


class Report:

    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add template
    @classmethod
    def add_template(cls, name, function):
        cls.templates[name] = function

    # Class method to get template
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method __call__
    def __call__(self, template_name):
        template = self.get_template(template_name)

        if template:
            return template(self.title, self.content)
        else:
            return "Template not found"

    # Magic method __str__
    def __str__(self):
        return self.title + ": " + self.content


# Simple template
def simple_template(title, content):
    return title + "\n" + content


# Fancy template using decorator
@bold_text
def fancy_template(title, content):
    return title + "\n" + content


# Add templates
Report.add_template("simple", simple_template)
Report.add_template("fancy", fancy_template)


# Create object
report = Report("Student Report", "Python OOP Experiment")


# Generate reports
print(report("simple"))

print()

print(report("fancy"))

print()

# __str__ method
print(report)