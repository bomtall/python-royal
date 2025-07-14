# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np
import plotly.express as px
import polars as pl
import streamlit as st
from streamlit.hello.utils import show_code
import glob
import os


def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text(f"{i}% complete")
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Rerun")


def toms_plot():
    df = pl.read_csv("C:/code/ep25/europython2025/data/bkg.csv")
    df2 = pl.read_csv("C:/code/ep25/europython2025/data/steel.csv")
    csv_files = glob.glob(os.path.join("C:/code/ep25/europython2025/data", "*.csv"))
    df_all = pl.concat([pl.read_csv(f) for f in csv_files], how="horizontal")
    return [df, df2, df_all]


def create_metrics(df, df2, df_all):
    st.metric(
        label="dgk Total number of rows",
        value=f"{df.shape[0]:,}",
        # delta=f"{df.shape[0] - 1000:,}",
    )
    st.metric(
        label="dgk Max",
        value=f"{df[list(df.columns)[0]].max():,}",
        # delta=f"{df.shape[1] - 10:,}",
    )
    st.metric(
        label="dgk Min",
        value=f"{df[list(df.columns)[0]].min():,}",
        # delta=f"{df.shape[1] - 10:,}",
    )
    st.metric(
        label="dgk Mean",
        value=f"{df[list(df.columns)[0]].mean():,}",
    )
    
    plot = px.histogram(
        df2,
        x=list(df2.columns)[0],
        # y=list(df2.columns)[0],
        title="Histogram of steel data",
        # labels={list(df2.columns)[0]: "X", list(df2.columns)[1]: "Y"},
        nbins=100,
    )
    st.plotly_chart(plot, use_container_width=True)

    



    # create a plotly line chart with all columns over just an x axis of index
    plot_all = px.line(
        df_all,
        # x=df_all.index,
        y=df_all.columns,
        title="Line chart of all data",
        labels={col: col for col in df_all.columns},
    )
    st.plotly_chart(plot_all, use_container_width=True)



if __name__ == "__main__":
    
    
    st.set_page_config(page_title="Plotting demo", page_icon=":material/show_chart:")
    st.title("Plotting demo")
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
        Streamlit. We're generating a bunch of random numbers in a loop for around
        5 seconds. Enjoy!
        """
    )
    plotting_demo()
    show_code(plotting_demo)
    # Call the toms_plot function to get the dataframes
    dfs = toms_plot()
    # Create metrics using the dataframes
    create_metrics(dfs[0], dfs[1], dfs[2])

