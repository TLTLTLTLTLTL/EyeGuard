import streamlit as st
import pandas as pd
from PIL import Image
from ultralytics import YOLO
import matplotlib.pyplot as plt	
import seaborn as sns

st.set_page_config(page_title="EyeGuard",page_icon="logo_bg.png", layout="wide")
st.markdown("""
    <style>
    .big-font {
        font-size:16px !important;
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
    st.sidebar.image("logo.png")

    if selection == "Introduction":
	    st.subheader("🌟 Cataract Information Portal")
	    column1, column2 = st.columns(2)
	    column2.image("https://drishtieye.org/wp-content/uploads/2024/06/Cataract-Hero-Image-2.jpg", use_column_width=True)

	    column1.markdown("""<p class="big-font">A cataract is a clouded or opaque area in the eye's lens, which is typically clear and essential for focusing light on the retina. The retina, a light-sensitive layer at the back of the eye, sends visual information to the brain.<br><br>When a cataract develops, proteins in the lens begin to break down and clump together, obstructing light from passing through the lens and reaching the retina effectively. This results in blurry or dull vision.<br><br>Cataracts usually develop gradually, often affecting both eyes, though not necessarily to the same degree. While commonly associated with aging, cataracts can also occur in infants, young children, or due to injury or medication.</p>""", unsafe_allow_html=True)

# Symptoms
    elif selection == "Symptoms":
	    st.subheader("👁️ Symptoms of Cataract")

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
	    st.subheader("📊 Statistics on Cataracts")
	    
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
	    st.subheader("📈 Age Groups Affected by Cataracts")
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
	    st.subheader("🔍 Early Detection in Cataract")

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
	    st.subheader("⏰ Consequences of Late Detection")
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
	    st.subheader("💰 Cost of Cataract Surgery")
	    st.markdown("""<p class="big-font">
     	    <ul>
	    <li class="big-font">The average cost of cataract surgery is <b>$3,500 per eye<b>, with prices potentially reaching up to <b>$7,000 per eye<b>.</li>
	    <li class="big-font"><b>Insurance typically covers the procedure<b>, but there are exceptions.</li>
	    <li class="big-font"><b>Health insurance<b> plans generally cover the traditional type of cataract surgery if it's considered "medically necessary".</li>
	    <li class="big-font"><b>Vision insurance<b> doesn't cover cataract surgery.</li>
	    <li class="big-font"><b>Out-of-pocket expenses<b> may include doctor fees, facility charges, or anesthesia.</li>
     	    </ul>
	    </p>""", unsafe_allow_html=True)
	    st.image("https://www.centreforsight.net/wp-content/uploads/2024/05/WhatsApp-Image-2024-05-17-at-6.07.03-PM.jpeg", width=800)

# Aftercare Post-Surgery
    elif selection == "Aftercare Post-Surgery":
	    st.subheader("📝 Aftercare Post-Surgery for Cataracts")

	    column1, column2 = st.columns(2)
	    column1.markdown("""<p class="big-font">To ensure proper healing after cataract surgery, follow these guidelines:
     	    <ul>
	    <li class="big-font">Follow your surgeon’s instructions for using eye drops.</li>
     	    <li class="big-font">Avoid getting water, shampoo, or soap in your eye.</li>
	    <li class="big-font">Do not rub or apply pressure to your eye.</li>
     	    <li class="big-font">Wear sunglasses outdoors to protect your eye.</li>
	    <li class="big-font">Use your eye shield while sleeping or as advised by your surgeon.</li>
     	    <li class="big-font">Limit strenuous physical activity.</li>
	    <li class="big-font">Protect your eye from irritants and potential trauma.</li>
     	    <li class="big-font">Avoid swimming and shower cautiously.</li>
	    <li class="big-font">Refrain from driving until your surgeon gives approval.</li>
     	    </ul>
            </p>""", unsafe_allow_html=True)
	    column2.image("https://www.sterilmedical.com/wp-content/uploads/2022/09/STERIL050615047aw1-600x600-1.jpeg")
    
with tab2:
    st.subheader("Eye scanner")
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
			    st.markdown(f'<h3>Disease: <span style="color:red">{str(res[0].names[label[0]].title())}</span></h3>', unsafe_allow_html=True)
			    # st.write()
			    st.markdown(f'<h4>Confidence level: {"{:.2f}".format(conf[0] * 100)}%</h4>', unsafe_allow_html=True)
			    st.write("""Your next steps should be to consult a doctor and, depending on your vision, either wear prescription glasses or plan surgery, which is common and highly effective.
       			    Make sure to maintain regular eye exams to monitor the disease and to ensure no other issues arise.""")
		    else:
			    st.write("No cataract detected")

with tab3:
	st.header("About Me :bulb:")
	col3, col4 = st.columns([8, 4])
	with col3:
		st.subheader("Introduction :star:")
		
		st.markdown("""<p class="big-font">My name is Jaiveer Bagga, and I am the creator of this app. As a high school junior with a passion for AI and coding, I am constantly seeking opportunities to apply my skills to make a positive impact. I have always been fascinated by the development and potential of AI and how it can be utilized to help the general public. My curiosity, along with the desire to help those in need, led me to develop this app.</p>""", unsafe_allow_html=True)
		
		st.subheader("Motivation :white_check_mark:")
		st.markdown("""<p class="big-font">My motivation to create this program stems from my commitment to ensure that people who have the disease are detected and treated early to prevent the condition from progressing. Many people are affected by cataracts, yet their issue often gets overlooked until the disease has worsened. Timely treatment can greatly help a patient's life by preventing future complications. With this app, my goal is to be able to spread awareness and help people in need who suffer from the disease to get more insight and be able to detect whether they do or do not have a cataract.</p>""", unsafe_allow_html=True)
		
	with col4:
		st.image("selfpic.jpg", width = 600)
