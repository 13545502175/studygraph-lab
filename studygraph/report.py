import html, json
def render_html(items, title='StudyGraph Lab Review Plan'):
    rows=''.join(f"<tr><td>{html.escape(x['name'])}</td><td>{x['score']:.2f}</td><td>{x['mastery']:.0%}</td><td>{html.escape(x['explanation'])}</td></tr>" for x in items)
    return f'<!doctype html><meta charset="utf-8"><title>{title}</title><style>body{{font:16px system-ui;max-width:960px;margin:40px auto}}table{{width:100%;border-collapse:collapse}}td,th{{padding:10px;border-bottom:1px solid #ddd;text-align:left}}</style><h1>{title}</h1><p>按分数从高到低排列，分数越高越值得优先复习。</p><table><tr><th>知识点</th><th>优先级</th><th>掌握度</th><th>解释</th></tr>{rows}</table>'
