import streamlit as st

# Define icons (using FontAwesome for simplicity)
icons = {
    "WSP Modelling team SharePoint": '<i class="fas fa-book"></i>',
    "How to's": '<i class="fas fa-glasses"></i>',
    "Get My Utility": '<i class="fas fa-tools"></i>',
    "Get My Script": '<i class="fas fa-code"></i>'
}

# Define URLs
urls = {
    "WSP Modelling team SharePoint": "https://wsponline.sharepoint.com/sites/GLD-Santiago-GWModelingTeam/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FGLD%2DSantiago%2DGWModelingTeam%2FShared%20Documents%2FGeneral&viewid=cd6f08a2%2D478c%2D4970%2D8baa%2D5b0072bcea36",
    "How to's": "https://wsponline.sharepoint.com/sites/GLD-Santiago-GWModelingTeam/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FGLD%2DSantiago%2DGWModelingTeam%2FShared%20Documents%2FGeneral%2F05%20%2D%20Desarrollos%20de%20grupo%2F2024%2D04%5FGP%5FHow%20To&viewid=cd6f08a2%2D478c%2D4970%2D8baa%2D5b0072bcea36",
    "Get My Utility": "https://sites.google.com/ug.uchile.cl/getmyutility/inicio",
    "Get My Script": "https://get-my-script.streamlit.app/"
}

# Title of the web application
st.title("Tools for US")

# Load FontAwesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# Function to create an HTML link styled as a button
def create_button(label, url, icon):
    return f"""
    <a href="{url}" target="_blank" style="
        display: inline-block;
        padding: 0.5em 1em;
        margin: 0.5em 0;
        text-decoration: none;
        color: white;
        background-color: #007bff;
        border-radius: 5px;
        font-size: 16px;
    ">
        {icon} {label}
    </a>
    """

# Create buttons with icons for each URL
for label, url in urls.items():
    st.markdown(create_button(label, url, icons[label]), unsafe_allow_html=True)
