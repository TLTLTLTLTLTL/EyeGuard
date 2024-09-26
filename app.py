import streamlit as st
import pandas as pd
from PIL import Image
from ultralytics import YOLO

st.set_page_config(layout='wide')
st.markdown("""
    <style>
    .big-font {
        font-size:22px !important;
    }
    </style>
    """, unsafe_allow_html=True)
# Load the model
@st.cache_resource
def models():
	mod = YOLO('best.pt')
	return mod
# tabs to change pages in app
tab1, tab2, tab3 = st.tabs(["Home", "Scan", "About Me"])

# tab 1 code
with tab1:
    # title and centering
    st.markdown("<h1 style='text-align: center;'>EyeGuard</h1>", unsafe_allow_html=True)

    # cataract description and header with image
    st.header("What is a Cataract?:eye:")

    st.markdown("""<p class="big-font">A cataract is a clouding of the eye's lens, which is typically clear. Seeing through cloudy lenses is like looking through a frosty or fogged-up window for people with cataracts. Clouded vision caused by cataracts can make it more difficult to read, drive a car at night, or see the expression on a friend's face. Most cataracts develop slowly and don't disturb eyesight early on. But with time, cataracts will eventually affect vision. At first, stronger lighting and eyeglasses can help deal with cataracts. However, if impaired vision affects usual activities, cataract surgery might be needed. Fortunately, cataract surgery is generally a safe, effective procedure.</p>""", unsafe_allow_html=True)

    #st.write("A cataract is a clouding of the eye's lens, which is typically clear. Seeing through cloudy lenses is like looking through a frosty or fogged-up window for people with cataracts. Clouded vision caused by cataracts can make it more difficult to read, drive a car at night, or see the expression on a friend's face. Most cataracts develop slowly and don't disturb eyesight early on. But with time, cataracts will eventually affect vision. At first, stronger lighting and eyeglasses can help deal with cataracts. However, if impaired vision affects usual activities, cataract surgery might be needed. Fortunately, cataract surgery is generally a safe, effective procedure.")
    st.image("eyesite-tampabay-cataract-vision.jpg", caption="Difference between normal and cataract lens")

    st.divider()

    # cataract symptoms and header with image
    col1, col2 = st.columns(2)

    with col1:
        st.header("Symptoms of Cataract")

        st.markdown("""<p class="big-font">
        <ul>
            <li class="big-font">Clouded, blurred, or dimmed vision</li>
            <li class="big-font">Trouble seeing at night</li>
            <li class="big-font">Sensitivity to light and glare</li>
            <li class="big-font">Need for brighter light for reading and other activities</li>
            <li class="big-font">Seeing "halos" around lights</li>
            <li class="big-font">Frequent changes in eyeglass or contact lens prescription</li>
            <li class="big-font">Fading or yellowing of color</li>
            <li class="big-font">Double vision in one eye</li>
        </ul>
        </p>""", unsafe_allow_html=True)
        
    with col2: 
        st.image("cataract-symptoms.jpg", caption="Normal vision versus clouded vision", width=400)

    st.divider()

    # cataract stats
    st.header("Cataract Prevalence:chart_with_upwards_trend:")
    st.markdown("""<p class="big-font">Cataracts affect more than 20.5 million Americans age 40 or older, and around 3.5 million cataract surgeries are performed each year.</p>""", unsafe_allow_html=True)
    

    # dictionary to create stat table for prevalance
    cat_dict = {
        "Age": ["40-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"],
        "Male Prevalance": ["2.77%", "4.9%", "8.12%", "13.45%", "21.53%", "32.27%", "44.81%", "63.14%"],
        "Female Prevalance": ["2.25%", "5.52%", "10.09%", "17.30%", "27.58%", "40.06%", "53.09%", "71.24%"]
                }
    
    # st.table(cat_dict)
    # url = "https://www.neovisioneyecenters.com/what-age-do-cataracts-develop/#:~:text=According%20to%20the%20NIH%2C%20in,cataracts%20at%20a%20higher%20rate."
    # st.write("Source: [What Age Do Cataracts Start Developing?](%s)" % url)

    col1, col2 = st.columns(2)

    with col1:
        df_cat = pd.DataFrame(cat_dict)
        st.dataframe(df_cat, width=700)
        url = "https://www.neovisioneyecenters.com/what-age-do-cataracts-develop/#:~:text=According%20to%20the%20NIH%2C%20in,cataracts%20at%20a%20higher%20rate."
        st.write("Source: [What Age Do Cataracts Start Developing?](%s)" % url)

    with col2:
        st.image("https://www.neovisioneyecenters.com/wp-content/uploads/2023/05/smiling-seniors-jpg.webp", width=500)
    


with tab2:
    st.header("Eye scanner")
    st.write("Please drag or upload the picture of your eye into the scanner.")
    img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
    analyse = st.button('Analyze')
                
    if analyse:
	    if img is not None:
		    img = Image.open(img)
		    st.markdown('Image Visualization')
		    st.image(img)
		    st.subheader('Your eye has been affected by:')
		    model = models()
		    res = model.predict(img)
		    label = res[0].probs.top5
		    conf = res[0].probs.top5conf
		    conf = conf.tolist()
		    st.write('Disease: ' + str(res[0].names[label[0]].title()))
		    st.write('Confidence level: ' + str(conf[0]))

with tab3:
	st.title("About Me :bulb:")
	col3, col4 = st.columns([8, 4])
	with col3:
		st.header("Introduction :star:")
		st.markdown("""
		<style>
		.big-font {
		    font-size:25px !important;
		}
		</style>
		""", unsafe_allow_html=True)
		
		st.markdown('<p class="big-font">My name is Jaiveer Bagga, and I am the creator of this app. I enjoy doing projects with AI and code, which I use to help people in need. As a junior in high school, I am aiming to constantly learn new skills and ideas that will help me make a larger change in the world. I was always fascinated by the development of AI and how it can be utilized in order to help the general public, which is the reason I have created this app.</p>', unsafe_allow_html=True)
		
		st.header("Motivation :white_check_mark:")
		st.markdown('<p class="big-font">I wrote this program to make sure people get their cataract treated as soon as possible in order to keep the disease from worsening over time. I believe it is better if someone with cataract gets treated earlier, so they would not have future troubles regarding their eyesight when they put off getting an operation done. A large amount of Americans struggle with this eye disease, yet it is not talked about too much. My goal is to be able to spread awareness and help people in need who suffer from disease to get more insight and be able to detect whether they do have a cataract.</p>', unsafe_allow_html=True)
		
	with col4:
		st.image("selfpic.jpg", width = 600)
