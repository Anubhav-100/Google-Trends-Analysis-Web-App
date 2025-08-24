import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import geopandas as gpd
import streamlit as st

# ----------------- Responsive helper functions -----------------
def scale_height(base=900):
    screen_width = st.session_state['screen_width']
    if screen_width < 480:
        return int(base*0.61) 
    if screen_width < 768:
        return int(base*0.7) 
    elif screen_width < 900:
        return int(base*0.8) 
    else:
        return base

def scale_font(base=20):
    screen_width = st.session_state['screen_width']
    if screen_width < 769:
        return int(base*0.72)
    elif screen_width < 900:
        return int(base*0.85)
    else:
        return base

def scale_marker(base=20):
    screen_width = st.session_state['screen_width']
    if screen_width < 769:
        return int(base*0.5)
    elif screen_width < 900:
        return int(base*0.8)
    else:
        return base

# ----------------- Charts -----------------
def plot_bar(region_data, primary):
    top15 = region_data.sort_values(by=primary, ascending=False).head(10)
    fig = px.bar(
        top15,
        x=primary,
        y="geoname",
        orientation='h',
        color=primary,
        color_continuous_scale="viridis",
        hover_name="geoname",
    )
        
    fig.update_layout(
        hoverlabel=dict(bgcolor="#8be0ea", font_size=13, font_color="black", bordercolor="orange"),
        title={'text': f"Top Locations by Interest in '{primary.title()}'",
               'y': 0.97, 'x': 0.5, 'xanchor': 'center','yanchor': 'top'},
        height=scale_height(),
        title_font=dict(size=scale_font(24), color='white', family='Arial Black'),
        paper_bgcolor='black',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Segoe UI", size=scale_font(14), color='white'),
        coloraxis_showscale=False
    )
    
    fig.update_yaxes(autorange="reversed",
                     title='LOCATIONS', title_font=dict(size=scale_font(20), color='white'),
                     tickmode='array', tickvals=[],
                     tickfont=dict(size=scale_font(16)))
    
    fig.update_xaxes(title=primary.upper(), title_font=dict(size=scale_font(20), color='white'),
                     tickfont=dict(size=scale_font(16)))
    return fig

def plot_donut(time_data, keywords):
    time_data.columns = time_data.columns.str.lower()
    keywords = [kw.lower() for kw in keywords]
    avg_dict = {kw: time_data[kw].mean() for kw in keywords}
    avg_df = pd.DataFrame(list(avg_dict.items()), columns=["Keyword", "Average"])
    avg_df["Percentage"] = 100 * avg_df["Average"] / avg_df["Average"].sum()
    colors = ['gold', 'skyblue', 'lightcoral', 'mediumseagreen', 'orchid', 'tomato', 'aqua']
    color_cycle = colors[:len(avg_df)]
    fig = go.Figure(data=[go.Pie(
        labels=avg_df["Keyword"],
        values=avg_df["Percentage"],
        hole=0.5,
        marker=dict(colors=color_cycle, line=dict(color='black', width=2)),
        pull=[0.05]*len(avg_df),
        textinfo='percent+label',
        insidetextorientation='radial',
        textfont=dict(size=scale_font(20), color='black'),
        showlegend=False
    )])
    fig.update_layout(
        hoverlabel=dict(bgcolor="#e77e7e", font_size=13, font_color="black", bordercolor="orange"),
        title={'text': "Average Search Interest", 'y': 0.97, 'x': 0.5,
               'xanchor': 'center', 'yanchor': 'top',
               'font': dict(size=scale_font(22), color='white', family='Arial Black')},
        paper_bgcolor="black",
        plot_bgcolor='black',
        height=scale_height()
    )
    return fig

def plot_map(region_data, selected_keyword, selected_geo):
    if selected_geo == '':
        gdf = gpd.read_file("data/ne_110m_admin_0_countries.shp")
        gdf = gdf.rename(columns={"ADMIN": "geoname"})
    else:
        gdf = gpd.read_file("data/ne_10m_admin_1_states_provinces.shp")
        gdf = gdf[gdf["iso_a2"] == selected_geo]
        gdf = gdf.rename(columns={"name": "geoname"})
    merged = gdf.merge(region_data, on="geoname", how="left"
    )
    
    fig = px.choropleth(
        merged,
        geojson=merged.geometry,
        hover_name="geoname",
        template="plotly_dark",
        locations=merged.index,
        color=selected_keyword,
        projection="equirectangular",
        color_continuous_scale="Viridis",
    )
    
    fig.update_geos(fitbounds="locations",
                    showcoastlines=True, coastlinecolor="Black",
                    showland=True, landcolor="rgb(217, 217, 217)",
                    showocean=True, oceancolor="lightblue",
                    showlakes=True, lakecolor="blue",
                    showframe=True,
                    lonaxis=dict(showgrid=True, gridcolor="gray", dtick=20),
                    lataxis=dict(showgrid=True, gridcolor="gray", dtick=10)
    )
    
    fig.update_layout(
        hoverlabel=dict(bgcolor="#a3e9ad",font_size=13,font_color="black",bordercolor="orange"),
        title={'text': "Search Interest by Locations", 'y':0.98,'x':0.5,'xanchor':'center','yanchor':'top'},
        height=scale_height(),
        title_font=dict(size=scale_font(24), color='white', family='Arial Black'),
        paper_bgcolor='black',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Segoe UI", size=scale_font(14), color='white'),
        coloraxis_colorbar=dict(orientation="h", y=-0.1, x=0.5, xanchor="center", thickness=20, len=1,
                                tickfont=dict(size=scale_font(14), color='white'),
                                title=dict( text="", font=dict(size=scale_font(16), color='white')),
                            )
    )
    return fig

def plot_line(time_data, primary):
    df = time_data
    fig = px.line(df, x='date', y=primary, markers=True, hover_name='date', render_mode='webgl', template='seaborn')
    fig.update_traces(marker=dict(size=scale_marker(10), color="red", symbol="circle",
                                  line=dict(width=2, color="darkblue")))
    fig.update_layout(
        hoverlabel=dict(bgcolor="#aac5f8", font_size=13, font_color="black", bordercolor="orange"),
        title={'text': f"Trend Over Time: {primary.upper()}", 'y':0.98,'x':0.5,'xanchor':'center','yanchor':'top'},
        height=scale_height(),
        paper_bgcolor='black',
        font=dict(color='white'),
        title_font=dict(size=scale_font(24), color='white'),
        margin=dict(t=60,b=50,l=60,r=30)
    )
    
    fig.update_yaxes(title=primary.upper(), title_font=dict(size=scale_font(20), color='white'),
                     tickfont=dict(size=scale_font(16)))
    fig.update_xaxes(title='DATE', title_font=dict(size=scale_font(20), color='white'),
                     tickfont=dict(size=scale_font(16)))
    return fig

def plot_allline(time_data, selected_keywords):
    df = time_data
    fig = px.line(df, x='date', y=selected_keywords, markers=True)
    for trace in fig.data:
        trace.update(marker=dict(size=scale_marker(8), color=trace.line.color,
                                 symbol="circle", line=dict(width=1, color="black")))
    fig.update_layout(
        hoverlabel=dict(bgcolor="#eea0dd", font_size=13, font_color="black", bordercolor="orange"),
        title={'text': "Keywords Search Interest Over Time", 'y':0.98,'x':0.5,'xanchor':'center','yanchor':'top'},
        height=scale_height(),
        paper_bgcolor='black',
        font=dict(color='white', size=scale_font(14)),
        title_font=dict(size=scale_font(24), color='white'),
        margin=dict(t=60,b=50,l=60,r=30),
        showlegend=False
    )
    
    fig.update_yaxes(title='SEARCH INTEREST', title_font=dict(size=scale_font(20), color='white'),
                     tickfont=dict(size=scale_font(16)))
    fig.update_xaxes(title='DATE', title_font=dict(size=scale_font(20), color='white'),
                     tickfont=dict(size=scale_font(16)))
    fig.update_traces(mode="lines", fill="tonexty")
    return fig

def plot_scatter(region_data, keywords):
    df = region_data[["geoname"] + [kw.lower() for kw in keywords]]
    df = df.melt(id_vars="geoname", var_name="Keyword", value_name="Interest")
    fig = px.scatter(df, y="geoname", x="Interest", color="Keyword", hover_name="geoname")
    
    fig.update_layout(
        hoverlabel=dict(bgcolor="#ddec9d", font_size=13, font_color="black", bordercolor="orange"),
        title={'text': "Scatter Plot of Search Interest by Location", 'y':0.98,'x':0.5,'xanchor':'center','yanchor':'top'},
        height=scale_height(),
        paper_bgcolor='black',
        font=dict(color='white', size=scale_font(14)),
        title_font=dict(size=scale_font(24), color='white'),
        margin=dict(t=60,b=50,l=60,r=30),
        showlegend=False
    )
    
    fig.update_xaxes(title='SEARCH INTEREST', title_font=dict(size=scale_font(20)), tickfont=dict(size=scale_font(16)))
    fig.update_yaxes(title='LOCATIONS', title_font=dict(size=scale_font(20)), tickmode='array', tickvals=[], tickfont=dict(size=scale_font(16)))
    return fig
