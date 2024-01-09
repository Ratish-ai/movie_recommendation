import streamlit as st
import pickle
import pandas as pd
from recommender import *

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

st.title ("Movie Recommendation System")

selected= st.selectbox(
    "Select the Movie",
    sorted(movies['title'].values)
)

selected_id = id(selected)

if st.button("Recommend"):
    st.header(selected)
    st.caption(year(selected_id)+" - "+run_time(selected_id))
    nc1,nc2 = st.columns(2)
    with nc1:
        st.image(img_path(selected_id),selected,200)
    with nc2:
        st.write(f"Ratings : {vote(selected_id)}\n\nBudget : {budget(selected_id)}\n\nBox Office : {box_office(selected_id)}\n\nOver View :\n\n{overview(selected_id)}")
    st.header("Recommended Details")
    values = recommend(selected)
    ids,movie = list(values.keys()),list(values.values())
    with st.sidebar:
        st.header("Recommendations")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.image(img_path(ids[0]),"Movie 1")
        with col2:
            st.image(img_path(ids[1]),"Movie 2")
        with col3:
            st.image(img_path(ids[2]),"Movie 3")
        col4,col5,col6 = st.columns(3)
        with col4:
            st.image(img_path(ids[3]),"Movie 4")
        with col5:
            st.image(img_path(ids[4]),"Movie 5")
        with col6:
            st.image(img_path(ids[5]),"Movie 6")
        col7,col8,col9 = st.columns(3)
        with col7:
            st.image(img_path(ids[6]),"Movie 7")
        with col8:
            st.image(img_path(ids[7]),"Movie 8")
        with col9:
            st.image(img_path(ids[8]),"Movie 9")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9= st.tabs([
        "Movie 1",
        "Movie 2",
        "Movie 3",
        "Movie 4",
        "Movie 5",
        "Movie 6",
        "Movie 7",
        "Movie 8",
        "Movie 9"])
    with tab1:
        st.subheader(movie[0])
        st.caption(year(ids[0])+" - "+run_time(ids[0]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[0]),movie[0],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[0])}\n\nBudget : {budget(ids[0])}\n\nBox Office : {box_office(ids[0])}\n\nOver View :\n\n{overview(ids[0])}")

    with tab2:
        st.subheader(movie[1])
        st.caption(year(ids[1])+" - "+run_time(ids[1]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[1]),movie[1],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[1])}\n\nBudget : {budget(ids[1])}\n\nBox Office : {box_office(ids[1])}\n\nOver View :\n\n{overview(ids[1])}")

    with tab3:
        st.subheader(movie[2])
        st.caption(year(ids[2])+" - "+run_time(ids[2]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[2]),movie[2],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[2])}\n\nBudget : {budget(ids[2])}\n\nBox Office : {box_office(ids[2])}\n\nOver View :\n\n{overview(ids[2])}")
    with tab4:
        st.header(movie[3])
        st.caption(year(ids[3])+" - "+run_time(ids[3]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[3]),movie[3],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[3])}\n\nBudget : {budget(ids[3])}\n\nBox Office : {box_office(ids[3])}\n\nOver View :\n\n{overview(ids[3])}")

    with tab5:
        st.subheader(movie[4])
        st.caption(year(ids[4])+" - "+run_time(ids[4]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[4]),movie[4],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[4])}\n\nBudget : {budget(ids[4])}\n\nBox Office : {box_office(ids[4])}\n\nOver View :\n\n{overview(ids[4])}")

    with tab6:
        st.subheader(movie[5])
        st.caption(year(ids[5])+" - "+run_time(ids[5]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[5]),movie[5],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[5])}\n\nBudget : {budget(ids[5])}\n\nBox Office : {box_office(ids[5])}\n\nOver View :\n\n{overview(ids[5])}")

    with tab7:
        st.subheader(movie[6])
        st.caption(year(ids[6])+" - "+run_time(ids[6]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[6]),movie[6],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[6])}\n\nBudget : {budget(ids[6])}\n\nBox Office : {box_office(ids[6])}\n\nOver View :\n\n{overview(ids[6])}")

    with tab8:
        st.subheader(movie[7])
        st.caption(year(ids[7])+" - "+run_time(ids[7]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[7]),movie[7],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[7])}\n\nBudget : {budget(ids[7])}\n\nBox Office : {box_office(ids[7])}\n\nOver View :\n\n{overview(ids[7])}")

    with tab9:
        st.subheader(movie[8])
        st.caption(year(ids[8])+" - "+run_time(ids[8]))
        col1,col2 = st.columns(2)
        with col1:
            st.image(img_path(ids[8]),movie[8],width=200)
        with col2:
            st.write(f"Ratings : {vote(ids[8])}\n\nBudget : {budget(ids[8])}\n\nBox Office : {box_office(ids[8])}\n\nOver View :\n\n{overview(ids[8])}")
