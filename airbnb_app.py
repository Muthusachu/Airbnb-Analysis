
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part
st.set_page_config(layout= "wide")


#creating Data Frame & Getting file from Github after compleating EDA process
df= pd.read_csv('https://raw.githubusercontent.com/Muthusachu/Airbnb-Analysis/main/Airbnb.csv')

col1,col2,col3=st.columns(3)

with col1:
  pass

with col2:
  st.title(":rainbow[**Airbnb Data Analysis**]")  

with col3:
  pass

st.header(":rainbow[]",  divider='rainbow')

select= option_menu(None, ["Price Analysis and Visualization","Availability Analysis by Season",
                            "Location-Based Insights", "Geospatial Visualization", "Top Chart"], 
                    icons=['house', 'cloud-upload', "list-task", 'gear', 'play'], menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={
        "container": {"padding": "0!important", "background-color": "#17202A"},
        "icon": {"color": "#9A7D0A", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#808080"},
        "nav-link-selected": {"background-color": "#808000"},
    })

if select == "Price Analysis and Visualization":  

  st.subheader(f":orange[{select}]")
  col1,col2,col3= st.columns(3)

  with col1:

    country= st.selectbox("Select the Country",df["country"].unique(), index=None, placeholder="Choose a Country")

    df1= df[df["country"] == country]
    df1.reset_index(drop= True, inplace= True)

  with col2:
    room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique(), index=None, placeholder="Select a room type")

    df2= df1[df1["room_type"] == room_ty]
    df2.reset_index(drop= True, inplace= True)

    df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
    df_bar.reset_index(inplace= True)

  with col3:
    proper_ty= st.selectbox("Select the Property type",df2["property_type"].unique(), index=None, placeholder="Choose a Property type")

    df4= df2[df2["property_type"] == proper_ty]
    df4.reset_index(drop= True, inplace= True)

    df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
    df_pie.reset_index(inplace= True)

  if country != None and room_ty != None and proper_ty != None:

    col1,col2= st.columns(2)

    with col1:
      fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY TYPES",
                      hover_data=["number_of_reviews","review_scores"],color= 'price',
                      width=600, height=500)
      st.plotly_chart(fig_bar)

    with col2:
      fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                      hover_data=["bedrooms"],
                      color= 'host_response_time',
                      title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                      width= 600, height= 500)
      st.plotly_chart(fig_pi)

  col1,col2= st.columns(2)

  with col1:

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    hostresponsetime= st.selectbox("Select the host response time",df4["host_response_time"].unique(),
                                    index=None, placeholder="Choose a host response time")

    df5= df4[df4["host_response_time"] == hostresponsetime]

    df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
    df_do_bar.reset_index(inplace= True)

  with col2:

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
    df_do_bar_2.reset_index(inplace= True)

  if hostresponsetime != None:
    col1,col2= st.columns(2)

    with col1:
      fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'],
      title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
      barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)

      st.plotly_chart(fig_do_bar_2)

    with col2:
      fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'],
      title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
      barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)

      st.plotly_chart(fig_do_bar)

if select == "Availability Analysis by Season":  

  st.subheader(f":orange[{select}]")

  col1,col2,col3= st.columns(3)

  with col1:

    country_a= st.selectbox("Select the Country",df["country"].unique(), index=None, placeholder="Choose Country")
    df1_a= df[df["country"] == country_a]
    df1_a.reset_index(drop= True, inplace= True)

  with col2:
    property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique(), index=None, placeholder="Choose a Property Type")
    df2_a= df1_a[df1_a["property_type"] == property_ty_a]
    df2_a.reset_index(drop= True, inplace= True)

  with col3:
    roomtype_a= st.selectbox("Select the Room Type", df2_a["room_type"].unique(), index=None, placeholder="Choose a Room Type")
    df3_a= df2_a[df2_a["room_type"] == roomtype_a]
    df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60",
                                                                    "availability_90","availability_365","price"]].sum())
    df_mul_bar_a.reset_index(inplace= True)

  if country_a != None and property_ty_a != None and roomtype_a != None:

    col1,col2= st.columns(2)

    with col1:

      df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"],
                                values="availability_30",width=600,height=500,title="Availability_30",
                                color_discrete_sequence=px.colors.sequential.Peach_r)
      st.plotly_chart(df_a_sunb_30)

    with col2:


      df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"],
                                values="availability_60",width=600,height=500,title="Availability_60",
                                color_discrete_sequence=px.colors.sequential.Blues_r)
      st.plotly_chart(df_a_sunb_60)

    col1,col2= st.columns(2)

    with col1:

      df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",
                                width=600,height=500,title="Availability_90",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
      st.plotly_chart(df_a_sunb_90)

    with col2:

      df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",
                                width=600,height=500,title="Availability_365",
                                color_discrete_sequence=px.colors.sequential.Greens_r)
      st.plotly_chart(df_a_sunb_365)



    fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time',
                              y=['availability_30', 'availability_60', 'availability_90', "availability_365"],
                              title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price", barmode='group',
                              color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

    st.plotly_chart(fig_df_mul_bar_a)


if select == "Location-Based Insights":  

  st.subheader(f":orange[{select}]")

  col1,col2,col3= st.columns(3)
  with col1:
    country_l= st.selectbox("Select the Country ",df["country"].unique(), index=None, placeholder="Choose Country ")

    df1_l= df[df["country"] == country_l]
    df1_l.reset_index(drop= True, inplace= True)      

  with col2:
    proper_ty_l= st.selectbox("Select the Property type ",df1_l["property_type"].unique(), index=None, placeholder="Choose a Property type ")

    df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
    df2_l.reset_index(drop= True, inplace= True)

  
    if country_l != None and proper_ty_l != None:
      def select_the_df(sel_val):
          if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

              df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
              df_val_30.reset_index(drop= True, inplace= True)
              return df_val_30

          elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):

              df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
              df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
              df_val_60_1.reset_index(drop= True, inplace= True)
              return df_val_60_1

          elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

              df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
              df_val_100.reset_index(drop= True, inplace= True)
              return df_val_100

      differ_max_min= df2_l['price'].max()-df2_l['price'].min()

  try:
    val_sel= st.radio("Select the Price Range",
      [str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),

      str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

      str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])

    df_val_sel= select_the_df(val_sel)

    df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
    df_val_sel_gr.reset_index(inplace= True)
  except:
    pass

  with col3:
    try:
      room_ty_l= st.selectbox("Select the Room Type ", df_val_sel["room_type"].unique(), index=None, placeholder="Choose a Room Type")
      df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]
    except:
      pass


    
  try:
    st.dataframe(df_val_sel)
  except:
    pass    


  try:
    fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
    st.plotly_chart(fig_1)
  except:
    pass

  try:
    if room_ty_l != None:
      try:
        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)
      except:
        pass
  except:
    pass

if select == "Geospatial Visualization":  

  st.subheader(f":orange[{select}]")

  fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                  color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                  zoom=1)
  fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
  st.plotly_chart(fig_4)


if select == "Top Chart":
  
  st.subheader(f":orange[{select}]")

  col1,col2,col3= st.columns(3)

  with col1:
    country_t= st.selectbox("Select the Country  ",df["country"].unique(), index=None, placeholder="Choose a Country  ")

    df1_t= df[df["country"] == country_t]

  with col2:
    property_ty_t= st.selectbox("Select the Property type  ",df1_t["property_type"].unique(), index=None, placeholder="Choose a  Property type  ")

    df2_t= df1_t[df1_t["property_type"] == property_ty_t]
    df2_t.reset_index(drop= True, inplace= True)

    df2_t_sorted= df2_t.sort_values(by="price")
    df2_t_sorted.reset_index(drop= True, inplace= True)


    df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
    df_price.reset_index(inplace= True)
    df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]

  with col3:
    room_type_t= st.selectbox("Select the Room Type  ",df2_t_sorted["room_type"].unique(), index=None, placeholder="Choose a  Room Type  ")

    df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

    df3_t_sorted_price= df3_t.sort_values(by= "price")

    df3_t_sorted_price.reset_index(drop= True, inplace = True)

    df3_top_50_price= df3_t_sorted_price.head(100)

  

  if country_t != None and property_ty_t != None:
    col1, col2= st.columns(2)
    with col1:

      fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                      title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
      st.plotly_chart(fig_price)

    with col2:

      fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                          title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
      st.plotly_chart(fig_price_2)

    col1, col2= st.columns(2)
    with col1:

        df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
        df_price_1.reset_index(inplace= True)
        df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]

        fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                            width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                            title= "PRICE BASED ON HOST_LOCATION")
        st.plotly_chart(fig_price_3)

    with col2:

        fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                            width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                            title= "AVERAGE PRICE BASED ON HOST_LOCATION")
        st.plotly_chart(fig_price_4)


  
  if room_type_t != None:      
    fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                              color_continuous_scale= "rainbow",
                            range_color=(0,df3_top_50_price["price"].max()),
                            title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                            width=1200, height= 800,
                            hover_data= ["minimum_nights","maximum_nights","accommodates"])

    st.plotly_chart(fig_top_50_price_1)
    
    fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                              color_continuous_scale= "greens",
                              title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                            range_color=(0,df3_top_50_price["price"].max()),
                            width=1200, height= 800,
                            hover_data= ["accommodates","bedrooms","beds","bed_type"])

    st.plotly_chart(fig_top_50_price_2)
