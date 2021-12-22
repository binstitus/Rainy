import plotly.express as px
nz=px.data.gapminder().query("country=='New Zealand'")
fig=px.bar(nz,x='year',y='pop')
#fig.show()
#print(fig)
#print(fig.layout)
fig.layout.title='popluation ovr time'
fig.update_layout(title_text='A new and better title',title_font_size=25,template='plotly_dark')
fig.show()
