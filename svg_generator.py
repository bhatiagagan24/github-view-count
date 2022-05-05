import redis, os

class Svg_Generator:
    svg_button = '''
            <svg
            xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" rx="1" ry="1" width="120" height="10" style="fill:{color};stroke:black;stroke-width:1;opacity:0.5" /><text x="15" y="25" fill="{text}">Profile Views: {views}</text>
            </svg>'''
    
    def __init__(self, view_obj):
        self.view_ops_obj = view_obj
    def svg_generator(self, text_fill, bg_fill):
        views = self.view_ops_obj.fetch_views()
        return self.svg_button.format(text=text_fill, color=bg_fill, views=views)



class View_Ops:
    def __init__(self):
        self.conn = redis.Redis(
            host = os.environ.get('HOST'),
            port = '33015',
            password = os.environ.get('PASSWORD'),
            ssl = True
        )
    def increase_views(self):
        curr_views = self.conn.get('views').decode('utf-8')
        if curr_views == None:
            self.conn.set('views', 1)
        self.conn.set('views', int(curr_views) + 1)
    def fetch_views(self):
        return self.conn.get('views').decode('utf-8')
