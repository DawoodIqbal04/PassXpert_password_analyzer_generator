# Imports
import streamlit as st
import re
import random

# Streamlit Page Configuration
st.set_page_config(page_title="PassXpert", page_icon='🔐', layout="centered")

# Streamlit UI

# Password Strength Analyzer:
col0 ,col1, col2 = st.columns([3, 2, 7], vertical_alignment='center')

with col0:
    st.title('')
with col1:
    st.image('icons/padlock.png', width=100, clamp=True)
    st.write('')
with col2:
    st.title('PassXpert', anchor=False)

st.subheader('The Ultimate Password Strength Analyzer & Enhancer 🔐', divider=True)

st.markdown('###### Your first line of defense is a strong password! ⚡ PassXpert analyzes and strengthens your passwords in real time, keeping you ahead of cyber threats. Stay secure, stay smart! 🔐🚀')

st.write('')

password = st.text_input('Enter the minimum length of the password', type='password')

st.write('')

st.markdown('### Improvement Suggestions And Security Analyzer:')

suggestion = []

strength_score = 0

if password:
    if len(password) >= 8:
        strength_score += 1
    else :
        suggestion.append({st.warning('⚠ Password length should be at least 8 characters')})

    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength_score += 1
    else :
        suggestion.append({st.warning('⚠ Password should contain both uppercase and lowercase characters')})


    if re.search(r"[0-9]", password):
        strength_score += 1
    else :
        suggestion.append({st.warning('⚠ Password should contain at least one number')})


    if re.search(r"[!@#$%^&*()_+{}|:<>]", password):
        strength_score += 1
    else :
        suggestion.append({st.warning('⚠ Password should contain at least one special character')})

    st.markdown('#### OverAll Password Security 🩹')

    if strength_score == 4:
        suggestion.append({st.success('✅ Your Password is strong! 🔒')})

    elif strength_score == 3:
        suggestion.append({st.warning('⚠️ Your Password is moderate! It could be stronger.')})

    else:
        suggestion.append({st.error('❌ Your Password is weak! Needs to be stronger')})


else:
    st.error('⚠ Please enter a password to analyze!')


st.subheader('', divider=True)


# Password Generator:

char_set_1 = r'abcdefghijklmnopqrstuvwxyz'
char_set_2 = r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_set_3 = r'0123456789'
char_set_4 = r'!@#$%^&*()_+{}|:<>'

st.write('')

st.header('Let **PassXpert**🔐 Generate A Strong Password For You! 🚀')

st.write('')

length = st.slider('Select the length of the password', min_value=12, max_value=32)

col1, col2 = st.columns(2)

with col1:
    char_set_1 = st.text_input('Small Letters', value=char_set_1)

    char_set_2 = st.text_input('Capital Letters', value=char_set_2)

with col2:
    char_set_3 = st.text_input('Numbers/ Digits', value=char_set_3)

    char_set_4 = st.text_input('Special Characters', value=char_set_4)


password_space = char_set_1 + char_set_2 + char_set_3 + char_set_4

def generate_password(space, length):
    for _ in range(length):
        yield random.SystemRandom().choice(space)

st.write('')

st.code(''.join(generate_password(password_space, length)), language='python')

st.title('')

cola, colb, colc = st.columns([1, 6 , 1])

with cola:
    st.write('')

with colb:
    st.markdown('#### Developed With ❤️ By [Muhammad Dawood](https://www.linkedin.com/in/muhammad-dawood-bb469b29a/) 🚀')

with colc:
    st.write('')