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

# Logo and title section
with st.container():
	col = st.columns([4,1,4,3],vertical_alignment="center")
	col[1].image('logo.png')
	col[2].markdown("<h1 style='text-align: center; color: white;'>EyeGuard</h1>", unsafe_allow_html=True)

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
	    st.subheader("🌟 Eye Disease Information Portal")
	    column1, column2 = st.columns(2)
	    column2.image("https://drishtieye.org/wp-content/uploads/2024/06/Cataract-Hero-Image-2.jpg", use_container_width=True)

	    column1.markdown("""<p class="big-font">A cataract is a clouded or opaque area in the eye's lens, which is typically clear and essential for focusing light on the retina.
     	    The retina, a light-sensitive layer at the back of the eye, sends visual information to the brain.<br><br>When a cataract develops, proteins in the lens begin to break down and clump together,
	    obstructing light from passing through the lens and reaching the retina effectively. This results in blurry or dull vision.<br><br>Cataracts usually develop gradually, often affecting both eyes, though not necessarily to the same degree.
   	    While commonly associated with aging, cataracts can also occur in infants, young children, or due to injury or medication.<br><br><br><br>Glaucoma is a group of eye conditions that damage the optic nerve, which is crucial for transmitting visual signals from the retina to the brain. 
	    This damage is often linked to elevated intraocular pressure (IOP) within the eye.<br><br>As pressure builds, it can compress and gradually deteriorate the optic nerve fibers, leading to blind spots in the visual field. 
     	    If left untreated, glaucoma can cause irreversible vision loss or even complete blindness.<br><br>Glaucoma typically develops slowly and without noticeable symptoms until significant damage has occurred. 
     	    Although it is more common in older adults, anyone—including infants—can be affected. Early detection and treatment are key to preserving vision.<br><br><br><br>
	    Diabetic Retinopathy is a diabetes-related complication that affects the blood vessels of the retina, the light-sensitive tissue at the back of the eye responsible for capturing images. 
     	    High blood sugar levels can cause these tiny retinal blood vessels to swell, leak, or close off entirely, disrupting normal blood flow.<br><br>In more advanced stages, abnormal new vessels may form, increasing the risk of bleeding and retinal detachment. 
	    Diabetic retinopathy often progresses without early warning signs, making regular eye exams critical for people with diabetes. Without timely diagnosis and intervention, it can lead to severe vision impairment or blindness.</p>""", unsafe_allow_html=True)

# Symptoms
    elif selection == "Symptoms":
	    st.subheader("👁️ Symptoms of Cataract")

	    column1, column2 = st.columns(2)
	    with column1:
		    column1.markdown("""<p class="big-font">People with cataracts may experience the following symptoms:<br><ul class="big-font"><li class="big-font">Vision appears blurred or foggy</li><li class="big-font">Sensitivity to bright lights or glare</li>
	     	    <li class="big-font">Difficulty seeing in dim lighting</li>
		    <li class="big-font">Colors appear less vibrant</li>
	     	    <li class="big-font">Cloudy or hazy sight</li>
		    <li class="big-font">Lights create halos or glare</li>
	     	    <li class="big-font">Struggles with vision at night</li>
		    <li class="big-font">Experiencing double vision</li>
	            <li class="big-font"> Increased nearsightedness and frequent need for new eyeglasses</li></ul></p>""", unsafe_allow_html=True)
		    
		    st.subheader("Symptoms of Glaucoma")
		    column1.markdown("""<p class="big-font">People with cataracts may experience the following symptoms:<br><ul class="big-font"><li class="big-font">Vision appears blurred or foggy</li><li class="big-font">Sensitivity to bright lights or glare</li>
	     	    <li class="big-font">Gradual loss of peripheral vision</li>
		    <li class="big-font">Tunnel vision in advanced stages</li>
	     	    <li class="big-font">Blurred vision, especially during pressure spikes</li>
		    <li class="big-font">Severe eye pain</li>
	     	    <li class="big-font">Eye redness</li>
		    <li class="big-font">Nausea and vomiting</li>
      		    <li class="big-font">Halos around lights</li></ul></p>""", unsafe_allow_html=True)
		    
		    st.subheader("Symptoms of Diabetic Retinopathy")
		    column1.markdown("""<p class="big-font">People with cataracts may experience the following symptoms:<br><ul class="big-font"><li class="big-font">Vision appears blurred or foggy</li><li class="big-font">Sensitivity to bright lights or glare</li>
	     	    <li class="big-font">Blurred or fluctuating vision</li>
		    <li class="big-font">Impaired color perception</li>
	     	    <li class="big-font">Dark spots or strings in the field of vision</li>
		    <li class="big-font">Sudden vision loss</li>
	     	    <li class="big-font">Seeing flashes of light</li>
		    <li class="big-font">Difficulty seeing at night</li>
      		    <li class="big-font">Trouble reading or recognizing faces</li></ul></p>""", unsafe_allow_html=True)
		    

	    with column2:
	    	column2.image("https://www.drparthshah.com.au/wp-content/uploads/2022/10/ISX3Cc2DzH-1.jpg", use_container_width=True)

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

	    st.subheader("Age Groups Affected by Glaucoma")

	    g_data = {
    		'Age': ['40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89'],
    		'Estimated_Prevalence_%': [0.2, 0.3, 0.5, 0.9, 1.4, 2.0, 2.8, 3.5, 4.0, 4.3]
	    }

	    g_df = pd.DataFrame(g_data)
	    st.table(g_df)


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
	    column2.image("https://www.reviewofoptometry.com/CMSImagesContent/2021/11/RO/11242021-phone-camera.jpg", use_container_width=True)

# Consequences of Late Detection
    elif selection == "Consequences of Late Detection":
	    st.subheader("⏰ Consequences of Late Detection")
	    st.markdown("""<p class="big-font">
	    Left untreated, these ocular diseases can lead to vision loss over time. Symptoms like blurry, hazy, or faded vision may make it harder to read or perform daily tasks.
     	    <br>
	    <ul>
	    <li class="big-font">These eye diseases are the <b>leading cause of age-related vision decline and preventable blindness<b>.</li>
	    <li class="big-font">The National Institute of Health predicts that the number of people with visual impairment will <b>double by 2050<b> due to the aging population.</li>
     	    </ul>
	    </p>""", unsafe_allow_html=True)
	    st.image("https://picjumbo.com/wp-content/uploads/old-alarm-clocks-analog-time-retro-free-stock-photo.jpg", width = 800, use_container_width=True)
	
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

	    
	    st.subheader("💰 Cost of Glaucoma Surgery")
	    st.markdown("""<p class="big-font">
     	    <ul>
	    <li class="big-font">The average annual cost of glaucoma treatment ranges from <b>$1,000 to $2,500<b> per patient, depending on the severity and treatment method.</li>
	    <li class="big-font">Prescription eye drops are often the first line of treatment and can cost <b>$150–$300<b> per month without insurance.</li>
	    <li class="big-font">Laser therapy and surgical procedures like trabeculectomy or shunt implantation may cost <b>$1,000 to $5,000<b> or more.</li>
	    <li class="big-font">Health insurance typically covers medically necessary glaucoma treatments, including surgery.</li>
     	    </ul>
	    </p>""", unsafe_allow_html=True)

	    
	    st.subheader("💰 Cost of Diabetic Retinopathy Surgery")
	    st.markdown("""<p class="big-font">
     	    <ul>
	    <li class="big-font">Treatment costs for diabetic retinopathy can vary widely but typically range from $1,500 to over $5,000 per year, depending on stage and treatment type.</li>
	    <li class="big-font">Anti-VEGF injections (e.g., Avastin, Eylea, Lucentis) can cost $50 to $2,000 per injection, with multiple injections often needed each year.</li>
	    <li class="big-font">Laser photocoagulation procedures usually cost $1,000 to $2,500 per session.</li>
	    <li class="big-font">Health insurance generally covers diabetic retinopathy treatments when deemed medically necessary.</li>
     	    <li class="big-font">Patients may incur out-of-pocket costs for imaging tests, injections, or specialist visits, especially if not fully covered.</li>
     	    </ul>
	    </p>""", unsafe_allow_html=True)
	    
	    st.image("https://www.centreforsight.net/wp-content/uploads/2024/05/WhatsApp-Image-2024-05-17-at-6.07.03-PM.jpeg", width=800, use_container_width=True)

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
	    column2.image("https://www.sterilmedical.com/wp-content/uploads/2022/09/STERIL050615047aw1-600x600-1.jpeg", use_container_width=True)
    
with tab2:
    st.subheader("Eye scanner")
    st.write("This application detects cataracts by analyzing fundus images using convolutional neural networks (CNNs). It specifically employs the YOLO (You Only Look Once) algorithm, which leverages CNNs to quickly process images and identify features indicative of cataracts. The CNN within YOLO scans the entire image in a single pass to detect and localize cataract regions efficiently. This approach enables rapid and accurate detection, assisting healthcare professionals in diagnosis and treatment planning.")
    st.subheader('Steps to use the app')
    st.markdown('''
    - Take a clear fundus image of the eye
    - Upload the image
    - Analyze the image''')
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
		st.image("selfpic.jpg", width = 600, use_container_width=True)
