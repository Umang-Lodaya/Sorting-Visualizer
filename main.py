import time
import random

import streamlit as st

st.set_option("deprecation.showPyplotGlobalUse", False)
# st.set_option("runOnSave", True)
st.set_page_config(layout="wide", page_title="Sorting Visualizer")
st.title("Sorting Visualizer")
st.markdown(
    "Made By: Umang Kirit Lodaya [GitHub](https://github.com/Umang-Lodaya/Sorting-Visualizer) | [LinkedIn](https://www.linkedin.com/in/umang-lodaya-074496242/) | [Kaggle](https://www.kaggle.com/umanglodaya)"
)
st.markdown("")

print("\n*****************")

ALGORITHMS = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"]
# ALGORITHMS.sort()

N_COL, T_COL = st.columns([3, 2], gap="large")
with N_COL:
    N = st.slider("Number of Elements: ", 10, 100, 50, 5)
    arr = [random.randint(1, 1000) for _ in range(N)]
with T_COL:
    ALGO = st.selectbox("Sorting Algorithm", ALGORITHMS)

A_COL, T_COL = st.columns([2.5, 2], gap="large")
button = False
with A_COL:
    st.markdown("####")
    if st.button("RANDOMIZE!", use_container_width=True):
        arr = [random.randint(1, 1000) for _ in range(N)]
with T_COL:
    SPEED = 0.1 / st.slider("Speed: ", 1, 10, 1)

button = False
button = st.button("SORT!", use_container_width=True)
st.markdown("###")

plot_spot = st.empty()
with plot_spot:
    st.bar_chart(arr)

if button:
    if ALGO == ALGORITHMS[0]:
        swapped = False
        for i in range(N - 1):
            for j in range(0, N - i - 1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    with plot_spot:
                        st.bar_chart(arr)

                time.sleep(SPEED)

            if not swapped:
                break

    elif ALGO == ALGORITHMS[1]:
        for i in range(1, N):
            while i > 0 and arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1
                with plot_spot:
                    st.bar_chart(arr)

                time.sleep(SPEED)

    elif ALGO == ALGORITHMS[2]:
        for i in range(N - 1):
            min_i = i
            for j in range(i + 1, N):
                if arr[j] < arr[min_i]:
                    min_i = j

            arr[min_i], arr[i] = arr[i], arr[min_i]
            with plot_spot:
                st.bar_chart(arr)

            time.sleep(SPEED)

    elif ALGO == ALGORITHMS[3]:

        def merge_sort(array, left_index, right_index):
            if left_index >= right_index:
                return
            middle = (left_index + right_index) // 2
            merge_sort(array, left_index, middle)
            merge_sort(array, middle + 1, right_index)
            merge(array, left_index, right_index, middle)


        def merge(array, left_index, right_index, middle):
            left_sublist = array[left_index : middle + 1]
            right_sublist = array[middle + 1 : right_index + 1]
            left_sublist_index = 0
            right_sublist_index = 0
            sorted_index = left_index
            while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
                if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
                    array[sorted_index] = left_sublist[left_sublist_index]
                    left_sublist_index = left_sublist_index + 1
                else:
                    array[sorted_index] = right_sublist[right_sublist_index]
                    right_sublist_index = right_sublist_index + 1
                
                with plot_spot:
                    st.bar_chart(array)
                time.sleep(SPEED)

                sorted_index = sorted_index + 1
            while left_sublist_index < len(left_sublist):
                array[sorted_index] = left_sublist[left_sublist_index]
                left_sublist_index = left_sublist_index + 1
                sorted_index = sorted_index + 1
                with plot_spot:
                    st.bar_chart(array)
                time.sleep(SPEED)

            while right_sublist_index < len(right_sublist):
                array[sorted_index] = right_sublist[right_sublist_index]
                right_sublist_index = right_sublist_index + 1
                sorted_index = sorted_index + 1
                with plot_spot:
                    st.bar_chart(array)
                time.sleep(SPEED)
        
        merge_sort(arr, 0, N - 1)


    elif ALGO == ALGORITHMS[4]:
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1

            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]
                    with plot_spot:
                        st.bar_chart(array)
                    time.sleep(SPEED)

            array[i + 1], array[high] = array[high], array[i + 1]
            with plot_spot:
                st.bar_chart(array)
            time.sleep(SPEED)

            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)
        
        quickSort(arr, 0, N - 1)

    with plot_spot:
        st.bar_chart(arr, color="#00FF00")
        time.sleep(0.5)

with plot_spot:
    st.bar_chart(arr)