import import_path as imp

imp.import_path("components")

from components import home
from components import file_loader


pages = {
    "Home": home,
    "XML Edit": file_loader,
    # Add more pages as needed
}


def apply(st):
    page = st.sidebar.selectbox("Choose a page", list(pages.keys()))

    if page in pages:
        pages[page].apply(st)
