from jinja2 import Environment,\
                   FileSystemLoader,\
                   select_autoescape

def generate_markdown_document(id:str,\
                               title:str,\
                               description: str,\
                               img:str,\
                               content:str):
        env = Environment(
        loader=FileSystemLoader("/code"),
        autoescape=select_autoescape()
        )


        t = env.get_template("template.md")

        render = t.render(title=title, img=img, description=description, content=content)
        with open(f"/code/videos/{id.lower()}.md","w") as f:
            f.write(render)