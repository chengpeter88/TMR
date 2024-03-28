import streamlit as st
my_variable = 'From Main App.py'

def  main():
    st.subheader('Main Page')
    st.title('Streamlit Multi Page')
    st.write(f' {my_variable}')

    choice = st.sidebar.selectbox( "Submenu",['Pandas', 'Numpy', 
                                            'Tensorflow', 'Pytorch'])
    if choice == 'Pandas':
        st.write('Pandas')
    elif choice == 'Numpy':
        st.write('Numpy')
    elif choice == 'Tensorflow':
        st.write('Tensorflow')

if __name__ == '__main__':
    main()  