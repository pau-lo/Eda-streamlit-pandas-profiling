import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def main():
    PAGES = {
        "EDA": render_eda,
        "About": render_about,
    }

    st.title("Streamlit")
    st.sidebar.header("Options")
    page = st.sidebar.selectbox(
        "Upload your data to create an Exploratory Data Analysis",
        options=list(PAGES.keys())
    )
    PAGES[page]()


def render_eda():
    st.title("Create a Complete Report of your data.")
    st.subheader("Exploratory Data Analysis using pandas profiling.")
    st.write("""All you need to do is upload a dataset and get a quick
            sense of your data.""")
    data = st.file_uploader("Upload Dataset", type=["csv", "txt"])
    if data is not None:
        df = pd.read_csv(data)
        # to adjust profile report check this link
        # https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/index.html
        # use --> (minimal=True) setting for large datasets
        pr = ProfileReport(df, explorative=True)
        st.title("Pandas Profiling Report in Streamlit")
        st.write(df)
        st_profile_report(pr)
        pr.to_file("Output.html")
        st.write("Your report has been saved!")


def render_about():
    st.subheader("About")
    st.write(
        """An App facilitating exploratory data analysis by using
        pandas profiling for streamlit."""
    )
    st.markdown(
        """Thank you [okld](
            https://github.com/okld/streamlit-pandas-profiling) for
            creating the pandas profiling component for streamlit.
            Check out the [pandas-profiling](
            https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/index.html)
            main page for more ways to configure your exploratory analysis.
        """
    )


if __name__ == "__main__":
    main()
