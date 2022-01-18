import streamlit as st
from learntools.deep_learning_intro.dltools import animate_sgd
from dataclasses import dataclass

class Page:
    

    def main(self):
        st.title("Learn Stochastic Gradient Descent with Linear Regression :rocket:")

        st.sidebar.header("Hyper Paramters")
        self.learning_rate = st.sidebar.number_input("Learning Rate", max_value=1.0, min_value=0.01)
        self.batch_size = st.sidebar.number_input("Batch Size", max_value=500, min_value=25)
        self.epochs = st.sidebar.number_input("Epochs", max_value=1000, min_value=50)
        self.iterations = st.sidebar.number_input("Iterations / Training Steps", max_value=100, min_value=25)

        st.sidebar.header("Data Paramters")
        self.weight = st.sidebar.number_input("Slope of the data")
        self.bias = st.sidebar.number_input("Bias of the data")
        self.num_examples = st.sidebar.number_input("Amount of datapoints", max_value=1000, min_value=20)
        st.latex('\Huge{y = wx + b}')
        st.sidebar.button("Submit", on_click=self.train_model)
        _, self.column_middle, _ = st.columns(3)


    def train_model(self):
            animation = animate_sgd(
                learning_rate=self.learning_rate,
                batch_size=self.batch_size,
                num_examples=self.num_examples,
                steps=self.iterations, 
                true_w=self.weight,
                true_b=self.bias, 
            )
            animation.save('visualization.gif')
            
            
            with self.column_middle:
                st.download_button(
                    label="Download Model", 
                    data=open('visualization.gif', 'rb').read(),
                    mime='image/gif',
                )

            

               

if __name__ == '__main__':
    webpage = Page().main()