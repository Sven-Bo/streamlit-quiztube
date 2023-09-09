import random
import ast

import streamlit as st

def string_to_list(s):
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError) as e:
        st.error(f"Error: The provided input is not correctly formatted. {e}")
        st.stop()

def get_randomized_options(options):
    correct_answer = options[0]
    random.shuffle(options)
    return options, correct_answer