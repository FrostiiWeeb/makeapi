try:
	import jinja2
	from jinja2 import Environment, PackageLoader, select_autoescape
except ImportError:
	jinja2 = None

if not jinja2:
	raise ImportError("Jinja2 was not found.")

class JinjaTemplates(Environment):
	def __init__(self, application, reload : bool = False, *args, **kwargs):
		self.application = application
		super().__init__(loader=PackageLoader(application.title), auto_reload=reload, autoescape=select_autoescape(), *args, **kwargs)

	def render_template(self, template_name : str, *args, **kwargs):
		template = super().get_template(template_name)
		template = template.render(*args, **kwargs)
		return template