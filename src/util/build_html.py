from jinja2 import Environment, FileSystemLoader


def build_html(games_df):
  colors = {
      "steam": "#3A6391",
      "epic": "#313131",
      "gog": "#6E4295",
  }

  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template('./static/template.html')

  html_content = template.render(
    games=games_df.to_dict(orient="records"), colors=colors, count=len(games_df))
  with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
