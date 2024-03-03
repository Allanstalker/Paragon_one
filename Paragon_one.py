import streamlit as st
import os
def externship_page(externship_number):
    st.title(f'Externship {externship_number}')

    if externship_number == 1:
        st.markdown("""
        **Augmented Reality Development and Digital Storytelling Externship**
        - Interest for Augmented Reality (AR)
        - Interest in using technology to create applications
        - Interest in Digital Storytelling
        - Creative Thinking and Problem-Solving Skills
        Learn More: https://www.paragonone.com/externships/snap-augmented-reality-development-and-digital-storytelling-externship
        """)
    elif externship_number == 2:
        st.markdown("""
        **Market Research Remote Externship**
        - Interest in market research
        - Interest in policymakers and policy influencers
        - Solve problems through research
        - Consulting
        Learn More: https://www.paragonone.com/externships/national-research-group-market-research-remote-externship
        """)
    elif externship_number == 3:
        st.markdown("""
        **Branding Strategy & Business Analytics Remote Externship**
        - Consumer analysis, market research
        - Analyze GenZ trends and, therefore, design better communication strategies
        - Passion for Consumer Marketing and Branding
        - Strong Analytical Skills
        - Learn More: https://www.paragonone.com/externships/beats-by-dr-dre-branding-strategy-business-analytics-remote-externship
        """)
    elif externship_number == 4:
        st.markdown("""
        **Asset Management & Deal Sourcing Remote Externship**
        - Has to be interested in sustainability and climate change
        - Interest in Finance and Investing
        - Learn More: https://paragonone.com/externships/colton-alexander-asset-management-deal-sourcing-remote-externship
        """)
    elif externship_number == 5:
        st.markdown("""
        **Competitive Strategy Remote Externship**
        - Interest in technology and blockchain, cybersecurity
        - Interest in User Behavior Analysis
        - Learn More: https://www.paragonone.com/externships/webacy-competitive-strategy-remote-externship
        """)
    elif externship_number == 6:
        st.markdown("""
        **Content Creation & Digital Marketing Remote Externship**
        - Interest in SEO
        - Perform strategies to maximize engagement and conversions
        - Interest in digital marketing, content
        - Learn more: https://www.paragonone.com/externships/content-creation-digital-marketing-remote-externship
        """)
def survey_page():
    st.title("Learn which externship is best suited for you!")
    

    # Question 1
    interests = {
        'Augmented reality': 1,
        'Market Research': 2,
        'Consumer marketing and branding': 3,
        'Sustainability': 4
    }
    answer_1 = st.selectbox('Which of the following spark your interest?', list(interests.keys()))
    st.write('You selected:', answer_1)

    # Question 2
    options_2 = {
        'Digital storytelling and creative problem-solving': 6,
        'Problem-solving through research and consulting': 2,
        'Analyzing consumer trends and market research': 3,
        'Competitive strategy and technology innovation': 5
    }
    answer_2 = st.selectbox('Which of the following would you like to learn more about?', list(options_2.keys()))
    st.write('You selected:', answer_2)

    # Question 3
    options_3 = {
        'Digital marketing and content creation': 6,
        'Design communication strategies': 3,
        'Financial management and investment': 4,
        'Exploring technologies like blockchain and cybersecurity': 5
    }
    answer_3 = st.selectbox('Which of the following intrigues you the most?', list(options_3.keys()))
    st.write('You selected:', answer_3)

    # Question 4
    options_4 = {
        'Creative thinking and problem-solving': 6,
        'Research and analysis skills': 2,
        'Analytical skills and data interpretation': 3,
        'Interest and knowledge in sustainability and finance': 4
    }
    answer_4 = st.selectbox('What skills do you feel the most confident in?', list(options_4.keys()))
    st.write('You selected:', answer_4)

    # Question 5
    options_5 = {
        'Innovating with technology and digital storytelling': 1,
        'Influencing policy decisions through research and consulting': 2,
        'Leading consumer marketing and branding initiatives ': 6,
        'Contributing to sustainable finance and investment strategies ': 4
    }
    answer_5 = st.selectbox('Which of the following do you see yourself doing in the future?', list(options_5.keys()))
    st.write('You selected:', answer_5)

    # Calculate and display the mean of selected answers
    selected_answers = [interests[answer_1], options_2[answer_2], options_3[answer_3], options_4[answer_4], options_5[answer_5]]
    mean_answer = sum(selected_answers) / len(selected_answers)

    # Display "Done" button
    if st.button("Done"):
        # Redirect to the appropriate externship page based on the mean answer
        externship_page_number = int(round(mean_answer))  # Assuming you want to round the mean
        externship_page(externship_page_number)
if __name__ == "__main__":
    survey_page()
