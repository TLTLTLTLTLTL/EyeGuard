import streamlit as st
import pandas as pd
from PIL import Image
from ultralytics import YOLO
import matplotlib.pyplot as plt	
import seaborn as sns

st.set_page_config(page_title="Cataract Scanner", layout="wide")
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
    # Sidebar with navigation
    st.sidebar.title("Navigation")
    sections = ["Introduction", "Symptoms", "Statistics", "Age Groups Affected", "Early Detection", "Consequences of Late Detection", "Cost of Surgery", "Aftercare Post-Surgery"]
    selection = st.sidebar.radio("Go to", sections)

    if selection == "Introduction":
	    st.title("🌟 Cataract Information Portal")
	    st.image("https://drishtieye.org/wp-content/uploads/2024/06/Cataract-Hero-Image-2.jpg", use_column_width=True)

	    st.markdown("""<p class="big-font"><b>A cataract<b> is a clouded or opaque area in the eye's lens, which is typically clear and essential for focusing light on the retina. The retina, a light-sensitive layer at the back of the eye, sends visual information to the brain.<br>When a cataract develops, proteins in the lens begin to break down and clump together, obstructing light from passing through the lens and reaching the retina effectively. This results in blurry or dull vision.<br>Cataracts usually develop gradually, often affecting both eyes, though not necessarily to the same degree. While commonly associated with aging, cataracts can also occur in infants, young children, or due to injury or medication.</p>""", unsafe_allow_html=True)

# Symptoms
    elif selection == "Symptoms":
	    st.title("👁️ Symptoms of Cataract")

	    column1, column2 = st.columns(2)
	    column1.markdown("""<p class="big-font">People with cataracts may experience the following symptoms:<br><ul class="big-font"><li class="big-font">Vision appears blurred or foggy</li><li class="big-font">Sensitivity to bright lights or glare</li>
     	    <li class="big-font">Difficulty seeing in dim lighting</li>
	    <li class="big-font">Colors appear less vibrant</li>
     	    <li class="big-font">Cloudy or hazy sight</li>
	    <li class="big-font">Lights create halos or glare</li>
     	    <li class="big-font">Struggles with vision at night</li>
	    <li class="big-font">Experiencing double vision</li>
            <li class="big-font"> Increased nearsightedness and frequent need for new eyeglasses</li></ul></p>""", unsafe_allow_html=True)

	    column2.image("https://www.drparthshah.com.au/wp-content/uploads/2022/10/ISX3Cc2DzH-1.jpg")

# Statistics
    elif selection == "Statistics":
	    st.title("📊 Statistics on Cataracts")
	    
	    st.markdown("""<p class="big-font"><ul>
            <li class="big-font">Each year, around <b>24 million Americans aged 40 and older<b> are affected by cataracts, making it one of the most common eye conditions in the U.S.</li>
	    <li class="big-font">Over <b>3.7 million cataract surgeries<b> are performed annually.</li></ul></p>""", unsafe_allow_html=True)
	    
	    # Create a sample dataframe for surgeries
	    surgery_data = pd.DataFrame({
	        'Year': [2020, 2021, 2022],
	        'Surgeries Performed': [3.5, 3.6, 3.7]
	    })
	    st.bar_chart(surgery_data.set_index('Year'))

# Age Groups Affected
    elif selection == "Age Groups Affected":
	    st.title("📈 Age Groups Affected by Cataracts")
	    st.markdown("<p class='big-font'>Cataract prevalence increases with age. Below is a table showing the rates by age and gender.</p>", unsafe_allow_html=True)
	
	    # Sample DataFrame (You can replace this with the actual data)
	    data = {
	        'Age': ['40-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+'],
	        'All_Female': [2.25, 5.52, 10.09, 17.3, 27.58, 40.06, 53.09, 71.24],
	        'All_Male': [2.77, 4.9, 8.12, 13.45, 21.53, 32.27, 44.81, 63.14]
	    }
	    df = pd.DataFrame(data)
	    st.table(df)
	
	    # Plotting
	    fig, ax = plt.subplots()
	    ax.plot(df['Age'], df['All_Female'], marker='o', label='All Female')
	    ax.plot(df['Age'], df['All_Male'], marker='o', label='All Male')
	    ax.set_xlabel('Age Group')
	    ax.set_ylabel('Prevalence Rate (%)')
	    ax.set_title('Cataract Prevalence by Age and Gender')
	    ax.legend()
	    st.pyplot(fig)

# Early Detection
    elif selection == "Early Detection":
	    st.title("🔍 Early Detection in Cataract")

	    column1, column2 = st.columns(2)
	    
	    column1.markdown("""<p class="big-font">
	    Cataracts are diagnosed similarly, regardless of age. However, if you're under 60, an eye care professional may be less likely to suspect cataracts.
	    <br>
	    <b>If you experience cataract symptoms, have a family history of early cataracts, or have health factors that increase your risk, it’s essential to inform your doctor during an eye exam.<b>
	    <br>
	    During your exam, your eye doctor will:
     	    <ul>
	    <li class="big-font">Take a detailed health and family history.</li>
	    <li class="big-font">Use dilation drops to examine your eyes more closely.</li>
	    <li class="big-font">Perform a retinal exam using a slit-lamp microscope to check for cataracts.</li>
	    <li class="big-font">Test your vision clarity through visual acuity and refraction tests.</li>
            </ul>
	    </p>""", unsafe_allow_html=True)
	    column2.image("https://www.reviewofoptometry.com/CMSImagesContent/2021/11/RO/11242021-phone-camera.jpg")

# Consequences of Late Detection
    elif selection == "Consequences of Late Detection":
	    st.title("⏰ Consequences of Late Detection")
	    st.markdown("""<p class="big-font">
	    Left untreated, cataracts can lead to vision loss over time. Symptoms like blurry, hazy, or faded vision may make it harder to read or perform daily tasks.
     	    <br>
	    <ul>
	    <li class="big-font">Cataracts are the <b>leading cause of age-related vision decline and preventable blindness<b>.</li>
	    <li class="big-font">The National Institute of Health predicts that the number of people with visual impairment will <b>double by 2050<b> due to the aging population.</li>
     	    </ul>
	    </p>""", unsafe_allow_html=True)
	    st.image("https://picjumbo.com/wp-content/uploads/old-alarm-clocks-analog-time-retro-free-stock-photo.jpg", width = 800)
	
	# Cost of Surgery
    elif selection == "Cost of Surgery":
	    st.title("💰 Cost of Cataract Surgery")
	    st.markdown("""<p class="big-font">
     	    <ul>
	    <li class="big-font">The average cost of cataract surgery is <b>$3,500 per eye<b>, with prices potentially reaching up to <b>$7,000 per eye<b>.</li>
	    <li class="big-font"><b>Insurance typically covers the procedure<b>, but there are exceptions.</li>
	    <li class="big-font"><b>Health insurance<b> plans generally cover the traditional type of cataract surgery if it's considered "medically necessary".</li>
	    <li class="big-font"><b>Vision insurance<b> doesn't cover cataract surgery.</li>
	    <li class="big-font"><b>Out-of-pocket expenses<b> may include doctor fees, facility charges, or anesthesia.</li>
     	    </ul>
	    </p>"""unsafe_allow_html=True)
	    st.image("https://www.medicareadvantage.com/sites/default/files/2019-09/Medicare-cataract-surgery-cost.jpg", use_column_width=True)

# Aftercare Post-Surgery
    elif selection == "Aftercare Post-Surgery":
	    st.title("📝 Aftercare Post-Surgery for Cataracts")
	    aftercare_steps = [
	        "Follow your surgeon’s instructions for using eye drops.",
	        "Avoid getting water, shampoo, or soap in your eye.",
	        "Do not rub or apply pressure to your eye.",
	        "Wear sunglasses outdoors to protect your eye.",
	        "Use your eye shield while sleeping or as advised by your surgeon.",
	        "Limit strenuous physical activity.",
	        "Protect your eye from irritants and potential trauma.",
	        "Avoid swimming and shower cautiously.",
	        "Refrain from driving until your surgeon gives approval."
	    ]
	    st.markdown("To ensure proper healing after cataract surgery, follow these guidelines:")
	    for step in aftercare_steps:
	        st.markdown(f"- {step}")

	
    # # title and centering
    # st.markdown("<h1 style='text-align: center;'>EyeGuard</h1>", unsafe_allow_html=True)

    # # cataract description and header with image
    # st.header("What is a Cataract?:eye:")

    # st.markdown("""<p class="big-font">A cataract is a clouding of the eye's lens, which is typically clear. Seeing through cloudy lenses is like looking through a frosty or fogged-up window for people with cataracts. Clouded vision caused by cataracts can make it more difficult to read, drive a car at night, or see the expression on a friend's face. Most cataracts develop slowly and don't disturb eyesight early on. But with time, cataracts will eventually affect vision. At first, stronger lighting and eyeglasses can help deal with cataracts. However, if impaired vision affects usual activities, cataract surgery might be needed. Fortunately, cataract surgery is generally a safe, effective procedure.</p>""", unsafe_allow_html=True)

    # #st.write("A cataract is a clouding of the eye's lens, which is typically clear. Seeing through cloudy lenses is like looking through a frosty or fogged-up window for people with cataracts. Clouded vision caused by cataracts can make it more difficult to read, drive a car at night, or see the expression on a friend's face. Most cataracts develop slowly and don't disturb eyesight early on. But with time, cataracts will eventually affect vision. At first, stronger lighting and eyeglasses can help deal with cataracts. However, if impaired vision affects usual activities, cataract surgery might be needed. Fortunately, cataract surgery is generally a safe, effective procedure.")
    # st.image("eyesite-tampabay-cataract-vision.jpg", caption="Difference between normal and cataract lens")

    # st.divider()

    # # cataract symptoms and header with image
    # col1, col2 = st.columns(2)

    # with col1:
    #     st.header("Symptoms of Cataract")

    #     st.markdown("""<p class="big-font">
    #     <ul>
    #         <li class="big-font">Clouded, blurred, or dimmed vision</li>
    #         <li class="big-font">Trouble seeing at night</li>
    #         <li class="big-font">Sensitivity to light and glare</li>
    #         <li class="big-font">Need for brighter light for reading and other activities</li>
    #         <li class="big-font">Seeing "halos" around lights</li>
    #         <li class="big-font">Frequent changes in eyeglass or contact lens prescription</li>
    #         <li class="big-font">Fading or yellowing of color</li>
    #         <li class="big-font">Double vision in one eye</li>
    #     </ul>
    #     </p>""", unsafe_allow_html=True)
        
    # with col2: 
    #     st.image("cataract-symptoms.jpg", caption="Normal vision versus clouded vision", width=400)

    # st.divider()

    # # cataract stats
    # st.header("Cataract Prevalence:chart_with_upwards_trend:")
    # st.markdown("""<p class="big-font">Cataracts affect more than 20.5 million Americans age 40 or older, and around 3.5 million cataract surgeries are performed each year.</p>""", unsafe_allow_html=True)
    

    # # dictionary to create stat table for prevalance
    # cat_dict = {
    #     "Age": ["40-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"],
    #     "Male Prevalance": ["2.77%", "4.9%", "8.12%", "13.45%", "21.53%", "32.27%", "44.81%", "63.14%"],
    #     "Female Prevalance": ["2.25%", "5.52%", "10.09%", "17.30%", "27.58%", "40.06%", "53.09%", "71.24%"]
    #             }
    
    # # st.table(cat_dict)
    # # url = "https://www.neovisioneyecenters.com/what-age-do-cataracts-develop/#:~:text=According%20to%20the%20NIH%2C%20in,cataracts%20at%20a%20higher%20rate."
    # # st.write("Source: [What Age Do Cataracts Start Developing?](%s)" % url)

    # col1, col2 = st.columns(2)

    # with col1:
    #     df_cat = pd.DataFrame(cat_dict)
    #     st.dataframe(df_cat, width=700)
    #     url = "https://www.neovisioneyecenters.com/what-age-do-cataracts-develop/#:~:text=According%20to%20the%20NIH%2C%20in,cataracts%20at%20a%20higher%20rate."
    #     st.write("Source: [What Age Do Cataracts Start Developing?](%s)" % url)

    # with col2:
    #     st.image("https://www.neovisioneyecenters.com/wp-content/uploads/2023/05/smiling-seniors-jpg.webp", width=500)
    


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
		    if str(res[0].names[label[0]].title()) == "Cataract":
			    st.write('Disease: ' + str(res[0].names[label[0]].title()))
			    st.write('Confidence level: ' + str(conf[0]))
			    st.write("See a doctor")
		    else:
			    st.write("No cataract detected")

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
