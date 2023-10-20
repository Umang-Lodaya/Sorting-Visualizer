import time
import random
import pandas as pd
import altair as alt

import streamlit as st

st.set_option("deprecation.showPyplotGlobalUse", False)
# st.set_option("runOnSave", True)
st.set_page_config(layout="wide", page_title="Sorting Visualizer")
st.title("Sorting Visualizer")


def getChart(data):
    return (
        alt.Chart(data)
        .mark_bar()
        .encode(
            alt.X("index"),
            alt.Y("value"),
            alt.Color("colour", legend=None),
            tooltip=["value"],
        )
        .interactive()
    )


print("\n*****************")

N_COL, R_COL, T_COL = st.columns(3, gap="large")
with N_COL:
    N = st.slider("Enter the Range of Numbers", 10, 100, 50, 5)
with R_COL:
    RANGE = st.slider("Enter the Range of Numbers", 1, 1000, [200, 900])
with T_COL:
    ALGO = st.selectbox("Algorithm", ["Bubble Sort", "Insertion Sort"])

df = pd.DataFrame([random.randint(*RANGE) for _ in range(N)], columns=["value"])
colours = [i for i in range(0xF0F00A, 0xF0F0FF)]
df["colour"] = df.value.apply(lambda x: colours[x // 10])
df.reset_index(inplace=True)

button = st.button("SORT!")
st.write("")
st.write("")
plot_spot = st.empty()
if button:
    if ALGO == "Bubble Sort":
        swapped = False
        for i in range(N - 1):
            for j in range(0, N - i - 1):
                arr = list(df.value)
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    df.value = arr
                    with plot_spot:
                        df["colour"] = df.value.apply(lambda x: colours[x // 10])
                        st.altair_chart(getChart(df), use_container_width=True)

                time.sleep(1 / N)

            if not swapped:
                break

    elif "Insertion Sort":
        arr = list(df.value)

        for i in range(1, N):
            while i > 0 and arr[i - 1] > arr[i]:
                arr = list(df.value)
                arr[i-1], arr[i] = arr[i], arr[i-1]
                i -= 1
                df.value = arr
                with plot_spot:
                    df["colour"] = df.value.apply(lambda x: colours[x // 10])
                    st.altair_chart(getChart(df), use_container_width=True)
                
                time.sleep(1 / N)

with plot_spot:
    df["colour"] = df.value.apply(lambda x: colours[x // 10])
    st.altair_chart(getChart(df), use_container_width=True)